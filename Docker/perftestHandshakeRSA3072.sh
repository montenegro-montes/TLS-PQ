#!/bin/sh
set -e

# Optionally set KEM to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
if [ "x$KEM_ALG" == "x" ]; then
	export DEFAULT_GROUPS=kyber512
else
        export DEFAULT_GROUPS=$KEM_ALG
fi

echo "Running  GENKEY CA"

openssl genpkey -algorithm rsa-pss  -pkeyopt rsa_keygen_bits:3072 -pkeyopt rsa_pss_keygen_mgf1_md:sha256 -pkeyopt rsa_pss_keygen_md:sha256 -pkeyopt rsa_pss_keygen_saltlen:32   -out /opt/test/CA.key
openssl req -x509 -new -key /opt/test/CA.key  -out /opt/test/CA.crt  -nodes -subj "/CN=oqstest CA" -days 365 -config /opt/oqssa/ssl/openssl.cnf

echo "Running  GENKEY SERVER"

openssl genpkey -algorithm rsa-pss  -pkeyopt rsa_keygen_bits:3072  -pkeyopt rsa_pss_keygen_mgf1_md:sha256 -pkeyopt rsa_pss_keygen_md:sha256   -pkeyopt rsa_pss_keygen_saltlen:32   -out /opt/test/server.key
openssl req -new -key /opt/test/server.key  -out /opt/test/server.csr   -nodes -subj "/CN=localhost" 

openssl x509 -req -in /opt/test/server.csr -out /opt/test/server.crt -CA /opt/test/CA.crt -CAkey /opt/test/CA.key -CAcreateserial -days 365
    

echo "Running   SERVER"
# Start a TLS1.3 test server based on OpenSSL accepting only the specified KEM_ALG
# The env var DEFAULT_GROUPS activates the required Group via the system openssl.cnf:
# we put it on the command line to check for possible typos otherwise silently discarded:
openssl s_server -cert /opt/test/server.crt -key /opt/test/server.key -groups $DEFAULT_GROUPS  -www -tls1_3 -accept localhost:4433 -verify 1 -verifyCAfile /opt/test/CA.crt&

# Give server time to come up first:
sleep 1

# Run handshakes for $TEST_TIME seconds
# The env var DEFAULT_GROUPS activates the required Group via the system openssl.cnf:
openssl s_client -connect localhost:4433 -state -servername localhost  -CAfile /opt/test/CA.crt -showcerts

#!/bin/sh
set -e

# Optionally set KEM to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
if [ "x$KEM_ALG" == "x" ]; then
	export DEFAULT_GROUPS=kyber768
else
   export DEFAULT_GROUPS=$KEM_ALG
fi

# Optionally set SIG to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
if [ "x$SIG_ALG" == "x" ]; then
	export SIG_ALG=secp384r1
fi


# Optionally set server certificate alg to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
# The root CA's signature alg remains as set when building the image
if [ "x$SIG_ALG" != "x" ]; then
    cd /opt/oqssa/bin

    openssl ecparam -out /opt/test/CA.key  -name $SIG_ALG -genkey
    openssl req -x509 -new -key /opt/test/CA.key  -out /opt/test/CA.crt  -sha384 -nodes -subj "/CN=oqstest CA" -days 365 -config /opt/oqssa/ssl/openssl.cnf


    # generate new server CSR using pre-set CA.key & cert
    openssl ecparam -out /opt/test/server.key  -name $SIG_ALG -genkey
    openssl req -new -key /opt/test/server.key  -out /opt/test/server.csr  -sha384 -nodes -subj "/CN=localhost"

    #openssl req -new -newkey $SIG_ALG -keyout /opt/test/server.key -out /opt/test/server.csr -nodes -subj "/CN=localhost"


    if [ $? -ne 0 ]; then
       echo "Error generating keys - aborting."
       exit 1
    fi
    # generate server cert
    openssl x509 -req -in /opt/test/server.csr -out /opt/test/server.crt -CA /opt/test/CA.crt -CAkey /opt/test/CA.key -CAcreateserial -days 365
    if [ $? -ne 0 ]; then
       echo "Error generating cert - aborting."
       exit 1
    fi

fi

echo "Running $0 with SIG_ALG=$SIG_ALG and KEM_ALG=$KEM_ALG"


# Start a TLS1.3 test server based on OpenSSL accepting only the specified KEM_ALG
# The env var DEFAULT_GROUPS activates the required Group via the system openssl.cnf:
# we put it on the command line to check for possible typos otherwise silently discarded:
openssl s_server -cert /opt/test/server.crt -key /opt/test/server.key -groups $DEFAULT_GROUPS -www -tls1_3 -accept localhost:4433 -verify 1 -verifyCAfile /opt/test/CA.crt &

# Give server time to come up first:
sleep 1

# Run handshakes for $TEST_TIME seconds
# The env var DEFAULT_GROUPS activates the required Group via the system openssl.cnf:
openssl s_client -connect localhost:4433 -state -servername localhost  -CAfile /opt/test/CA.crt -showcerts



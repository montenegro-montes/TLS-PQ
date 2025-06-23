#!/bin/sh

# ---------------------------
# Set network DELAY and LOSS
# ---------------------------
set -e

# Optionally set SIG to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
if [ -z "$SIG_ALG" ]; then
	export SIG_ALG=mldsa44
fi


# ---------------------------
# Create certificates 
# ---------------------------
# Optionally set server certificate alg to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
# The root CA's signature alg remains as set when building the image

if [ -z "$CERT_PATH" ]; then
   CERT_PATH=/opt/test/
   mkdir -p $CERT_PATH
fi

if [ -n "$SIG_ALG" ]; then
    echo "Creating certificates"
    cd /opt/oqssa/bin

   
    case "$SIG_ALG" in
    secp*) 
        echo "Using ECDSA procedure for $SIG_ALG"
        # Procedimiento para secp...

            openssl ecparam -out $CERT_PATH/CA.key  -name $SIG_ALG -genkey
            openssl req -x509 -new -key $CERT_PATH/CA.key  -out $CERT_PATH/CA.crt  -sha384 -nodes -subj "/CN=oqstest CA" -days 365 -config /opt/oqssa/ssl/openssl.cnf


            # generate new server CSR using pre-set CA.key & cert
            openssl ecparam -out $CERT_PATH/server.key  -name $SIG_ALG -genkey
            openssl req -new -key $CERT_PATH/server.key  -out $CERT_PATH/server.csr  -sha384 -nodes -subj "/CN=localhost"


            if [ $? -ne 0 ]; then
               echo "Error generating keys - aborting."
               exit 1
            fi
            # generate server cert
            openssl x509 -req -in $CERT_PATH/server.csr -out $CERT_PATH/server.crt -CA $CERT_PATH/CA.crt -CAkey $CERT_PATH/CA.key -CAcreateserial -days 365
            if [ $? -ne 0 ]; then
               echo "Error generating cert - aborting."
               exit 1
            fi


            # generate new user CSR using pre-set CA.key & cert
            openssl ecparam -out $CERT_PATH/user.key  -name $SIG_ALG -genkey
            openssl req -new -key $CERT_PATH/user.key  -out $CERT_PATH/user.csr  -sha384 -nodes -subj "/CN=user"


            if [ $? -ne 0 ]; then
               echo "Error generating keys - aborting."
               exit 1
            fi
            # generate server cert
            openssl x509 -req -in $CERT_PATH/user.csr -out $CERT_PATH/user.crt -CA $CERT_PATH/CA.crt -CAkey $CERT_PATH/CA.key -CAcreateserial -days 365
            if [ $? -ne 0 ]; then
               echo "Error generating cert - aborting."
               exit 1
            fi
        ;;
    rsa*)
          echo "Using RSA procedure for $SIG_ALG"
          openssl genpkey -algorithm rsa-pss  -pkeyopt $SIG_KEY -pkeyopt $SIG_RSA_MD -pkeyopt $SIG_RSA_MD2  -pkeyopt rsa_pss_keygen_saltlen:32   -out /opt/test/CA.key
          openssl req -x509 -new -key /opt/test/CA.key  -out /opt/test/CA.crt  -nodes -subj "/CN=oqstest CA" -days 365 -config /opt/oqssa/ssl/openssl.cnf

          
          # generate new server CSR using pre-set CA.key & cert
          openssl genpkey -algorithm rsa-pss  -pkeyopt $SIG_KEY -pkeyopt $SIG_RSA_MD -pkeyopt $SIG_RSA_MD2  -pkeyopt rsa_pss_keygen_saltlen:32   -out /opt/test/server.key
          openssl req -new -key /opt/test/server.key  -out /opt/test/server.csr   -nodes -subj "/CN=localhost" 
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

          # generate new user CSR using pre-set CA.key & cert
          openssl genpkey -algorithm rsa-pss  -pkeyopt $SIG_KEY -pkeyopt $SIG_RSA_MD -pkeyopt $SIG_RSA_MD2  -pkeyopt rsa_pss_keygen_saltlen:32   -out /opt/test/user.key
          openssl req -new -key /opt/test/user.key  -out /opt/test/user.csr   -nodes -subj "/CN=user" 
          if [ $? -ne 0 ]; then
             echo "Error generating keys - aborting."
             exit 1
          fi
          # generate server cert
          openssl x509 -req -in /opt/test/user.csr -out /opt/test/user.crt -CA /opt/test/CA.crt -CAkey /opt/test/CA.key -CAcreateserial -days 365
          if [ $? -ne 0 ]; then
             echo "Error generating cert - aborting."
             exit 1
          fi
        ;;     
    *)  
        echo "Using default procedure for $SIG_ALG"
        # Procedimiento original...
        
             
         openssl req -x509 -new -newkey $SIG_ALG -keyout $CERT_PATH/CA.key -out $CERT_PATH/CA.crt -nodes -subj "/CN==oqstest CA" -days 365 -config /opt/oqssa/ssl/openssl.cnf

         # generate new server CSR using pre-set CA.key & cert
         openssl req -new -newkey $SIG_ALG -keyout $CERT_PATH/server.key -out $CERT_PATH/server.csr -nodes -subj "/CN==localhost"
         if [ $? -ne 0 ]; then
                   echo "Error generating keys - aborting."
                   exit 1
         fi
         # generate server cert
         openssl x509 -req -in $CERT_PATH/server.csr -out $CERT_PATH/server.crt -CA $CERT_PATH/CA.crt -CAkey $CERT_PATH/CA.key -CAcreateserial -days 365
         if [ $? -ne 0 ]; then
                   echo "Error generating cert - aborting."
                   exit 1
         fi

         # generate new key CSR using pre-set CA.key & cert
         openssl req -new -newkey $SIG_ALG -keyout $CERT_PATH/user.key -out $CERT_PATH/user.csr -nodes -subj "/CN==user"
         if [ $? -ne 0 ]; then
                   echo "Error generating keys - aborting."
                   exit 1
         fi
         # generate user cert
         openssl x509 -req -in $CERT_PATH/user.csr -out $CERT_PATH/user.crt -CA $CERT_PATH/CA.crt -CAkey $CERT_PATH/CA.key -CAcreateserial -days 365
         if [ $? -ne 0 ]; then
                   echo "Error generating cert - aborting."
                   exit 1
         fi
         ;;
   esac

      
fi



echo "Running $0 with SIG_ALG=$SIG_ALG and certificates created"
echo


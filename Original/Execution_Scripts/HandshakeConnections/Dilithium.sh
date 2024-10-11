#!/bin/bash

docker run  -e TEST_TIME=10 -e KEM_ALG=P-384     -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber768  -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestServer.sh

docker run  -e TEST_TIME=10 -e KEM_ALG=P-521      -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber1024  -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestServer.sh

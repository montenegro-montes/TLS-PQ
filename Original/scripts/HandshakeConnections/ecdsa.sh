#!/bin/bash

docker run -e TEST_TIME=10 -e KEM_ALG=P-384    -e SIG_ALG=secp384r1 -it oqs-curlv331 perftestECDSA.sh
docker run -e TEST_TIME=10 -e KEM_ALG=kyber768 -e SIG_ALG=secp384r1 -it oqs-curlv331 perftestECDSA.sh
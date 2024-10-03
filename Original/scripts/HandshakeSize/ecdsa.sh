#!/bin/bash

docker run -e KEM_ALG=P-384 -e SIG_ALG=secp384r1 -it oqs-curlv331 perftestHandshakeECDSA.sh
docker run -e KEM_ALG=kyber768 -e SIG_ALG=secp384r1 -it oqs-curlv331 perftestHandshakeECDSA.sh
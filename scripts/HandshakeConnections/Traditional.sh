#!/bin/bash

docker run  -e TEST_TIME=10  -e KEM_ALG=X25519   -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10  -e KEM_ALG=P-256    -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10  -e KEM_ALG=kyber512 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh


docker run  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=ed448 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10  -e KEM_ALG=kyber1024 -e SIG_ALG=ed448 -it oqs-curlv331 perftestServer.sh
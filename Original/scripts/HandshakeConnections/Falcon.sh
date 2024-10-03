#!/bin/bash

docker run  -e TEST_TIME=10 -e KEM_ALG=X25519   -e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=P-256    -e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber512 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh

docker run  -e TEST_TIME=10 -e KEM_ALG=X25519   -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=P-256    -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber512 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestServer.sh


docker run  -e TEST_TIME=10 -e KEM_ALG=P-521     -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber1024 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestServer.sh

docker run  -e TEST_TIME=10 -e KEM_ALG=P-521     -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=kyber1024 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestServer.sh

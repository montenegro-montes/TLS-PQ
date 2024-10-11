#!/bin/bash

docker run -e KEM_ALG=kyber512 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber768 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber1024 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=kyber512 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber768 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber1024 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=kyber512 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber768 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber1024 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=kyber512 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber768 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=kyber1024 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh

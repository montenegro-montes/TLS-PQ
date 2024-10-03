#!/bin/bash

docker run  -e KEM_ALG=kyber512 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=kyber768 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=kyber1024 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh

docker run  -e KEM_ALG=kyber512 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=kyber768 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=kyber1024 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
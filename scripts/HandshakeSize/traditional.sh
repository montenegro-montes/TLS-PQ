#!/bin/bash

docker run -e KEM_ALG=X25519 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestHandshakeServer.sh


docker run -e KEM_ALG=X25519 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=ed448 -it oqs-curlv331 perftestHandshakeServer.sh

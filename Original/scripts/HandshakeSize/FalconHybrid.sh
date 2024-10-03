#!/bin/bash

docker run -e KEM_ALG=X25519 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=falcon512 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=falconpadded512 -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=falconpadded1024 -it oqs-curlv331 perftestHandshakeServer.sh
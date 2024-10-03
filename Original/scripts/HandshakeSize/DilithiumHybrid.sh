#!/bin/bash

docker run -e KEM_ALG=X25519 -e SIG_ALG=dilithium2 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=dilithium2 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=dilithium2 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=dilithium2 -it oqs-curlv331 perftestHandshakeServer.sh


docker run -e KEM_ALG=X25519 -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=dilithium3 -it oqs-curlv331 perftestHandshakeServer.sh


docker run -e KEM_ALG=X25519 -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=dilithium5 -it oqs-curlv331 perftestHandshakeServer.sh
#!/bin/bash

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake128fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake128fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake128ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake128ssimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake192fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake192ssimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake256fsimple -it oqs-curlv331 perftestHandshakeServer.sh

docker run -e KEM_ALG=X25519 -e SIG_ALG=sphincsshake256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=sphincsshake256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-384 -e SIG_ALG=sphincsshake256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=P-521 -e SIG_ALG=sphincsshake256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
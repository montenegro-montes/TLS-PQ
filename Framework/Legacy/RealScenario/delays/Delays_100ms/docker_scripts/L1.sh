#!/bin/bash

echo "RSA"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=X25519   -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256  -it oqs-curlv331_tc perftestServerRSA.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-256    -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256  -it oqs-curlv331_tc perftestServerRSA.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=mlkem512 -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256  -it oqs-curlv331_tc perftestServerRSA.sh

echo "ed25519"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=X25519   -e SIG_ALG=ed25519 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-256    -e SIG_ALG=ed25519 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=mlkem512 -e SIG_ALG=ed25519 -it oqs-curlv331_tc perftestServer.sh

echo "falcon512"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=X25519   -e SIG_ALG=falcon512 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=P-256    -e SIG_ALG=falcon512 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=mlkem512 -e SIG_ALG=falcon512 -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2128fsimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%   -e TEST_TIME=10  -e KEM_ALG=X25519   -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%   -e TEST_TIME=10  -e KEM_ALG=P-256    -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%   -e TEST_TIME=10  -e KEM_ALG=mlkem512 -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2128ssimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%	-e TEST_TIME=10  -e KEM_ALG=X25519   -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-256    -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%	-e TEST_TIME=10  -e KEM_ALG=mlkem512 -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331_tc perftestServer.sh

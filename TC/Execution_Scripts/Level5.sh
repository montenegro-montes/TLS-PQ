#!/bin/bash

echo "ed448"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=ed448 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=kyber1024 -e SIG_ALG=ed448 -it oqs-curlv331_tc perftestServer.sh

echo "dilithium5"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10 -e KEM_ALG=P-521      -e SIG_ALG=dilithium5 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10 -e KEM_ALG=kyber1024  -e SIG_ALG=dilithium5 -it oqs-curlv331_tc perftestServer.sh

echo "falcon1024"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10 -e KEM_ALG=P-521     -e SIG_ALG=falcon1024 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10 -e KEM_ALG=kyber1024 -e SIG_ALG=falcon1024 -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2256fsimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=kyber1024 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2256ssimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms -e TC_LOSS=0.25%  -e TEST_TIME=10  -e KEM_ALG=kyber1024 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331_tc perftestServer.sh

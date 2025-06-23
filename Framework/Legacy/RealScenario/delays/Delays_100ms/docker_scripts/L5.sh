#!/bin/bash

echo "secp521r1"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=secp521r1 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=mlkem1024 -e SIG_ALG=secp521r1 -it oqs-curlv331_tc perftestServer.sh

echo "mldsa87"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=P-521      -e SIG_ALG=mldsa87 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=mlkem1024  -e SIG_ALG=mldsa87 -it oqs-curlv331_tc perftestServer.sh

echo "falcon1024"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=P-521     -e SIG_ALG=falcon1024 -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10 -e KEM_ALG=mlkem1024 -e SIG_ALG=falcon1024 -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2256fsimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2256ssimple"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=P-521     -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331_tc perftestServer.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=100ms  -e TC_LOSS=0%  -e TEST_TIME=10  -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331_tc perftestServer.sh

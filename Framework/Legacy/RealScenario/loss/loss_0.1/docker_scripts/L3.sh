#!/bin/bash

echo "secp384r1"

docker run --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10 -e KEM_ALG=P-384    -e SIG_ALG=secp384r1 -it oqs-curlv331_tc perftestServerECDSA.sh
docker run --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10 -e KEM_ALG=mlkem768 -e SIG_ALG=secp384r1 -it oqs-curlv331_tc perftestServerECDSA.sh

echo "mldsa65"

docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10 -e KEM_ALG=P-384     -e SIG_ALG=mldsa65 -it oqs-curlv331_tc perftestServer.sh
docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10 -e KEM_ALG=mlkem768  -e SIG_ALG=mldsa65 -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2192fsimple"

docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10  -e KEM_ALG=P-384    -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331_tc perftestServer.sh
docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10  -e KEM_ALG=mlkem768 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331_tc perftestServer.sh

echo "sphincssha2192ssimple"

docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10  -e KEM_ALG=P-384    -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331_tc perftestServer.sh
docker run  --cap-add=NET_ADMIN  -e TC_DELAY=0ms -e TC_LOSS=0.1%   -e TEST_TIME=10  -e KEM_ALG=mlkem768 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331_tc perftestServer.sh


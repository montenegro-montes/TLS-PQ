#!/bin/bash

#ecdsa
docker run -e KEM_ALG=P-384 	-e SIG_ALG=secp384r1 	-it oqs-curlv331 perftestHandshakeServerECDSA.sh
docker run -e KEM_ALG=mlkem768 	-e SIG_ALG=secp384r1 	-it oqs-curlv331 perftestHandshakeServerECDSA.sh

# ML-DSA-65-ipd
docker run -e KEM_ALG=P-384 	-e SIG_ALG=mldsa65	-it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=mlkem768 	-e SIG_ALG=mldsa65 	-it oqs-curlv331 perftestHandshakeServer.sh


#sphincs192f
docker run  -e KEM_ALG=P-384 	-e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=mlkem768 -e SIG_ALG=sphincssha2192fsimple -it oqs-curlv331 perftestHandshakeServer.sh

#sphincs192s
docker run  -e KEM_ALG=P-384 	-e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=mlkem768 -e SIG_ALG=sphincssha2192ssimple -it oqs-curlv331 perftestHandshakeServer.sh


# ML-DSA-65-ipd
docker run -e KEM_ALG=P-384 	-e SIG_ALG= ML-DSA-65-ipd 	-it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=mlkem768 	-e SIG_ALG= ML-DSA-65-ipd 	-it oqs-curlv331 perftestHandshakeServer.sh


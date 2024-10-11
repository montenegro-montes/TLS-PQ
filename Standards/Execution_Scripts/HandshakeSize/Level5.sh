#!/bin/bash


#secp521r1
docker run  -e KEM_ALG=P-521 			-e SIG_ALG=secp521r1 -it oqs-curlv331 perftestHandshakeServerECDSA.sh
docker run  -e KEM_ALG=mlkem1024		-e SIG_ALG=secp521r1 -it oqs-curlv331 perftestHandshakeServerECDSA.sh


#mldsa87
docker run -e KEM_ALG=P-521 	-e SIG_ALG=mldsa87 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=mlkem1024 -e SIG_ALG=mldsa87 -it oqs-curlv331 perftestHandshakeServer.sh


docker run -e KEM_ALG=P-521 		-e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh
docker run -e KEM_ALG=mlkem1024 	-e SIG_ALG=falcon1024 -it oqs-curlv331 perftestHandshakeServer.sh


#sphincs256f
docker run  -e KEM_ALG=P-521 	 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestHandshakeServer.sh


#sphincs256s
docker run  -e KEM_ALG=P-521 	 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh
docker run  -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestHandshakeServer.sh

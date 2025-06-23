#!/bin/bash


#secp521r1
docker run  -e TEST_TIME=10 -e KEM_ALG=P-521 			-e SIG_ALG=secp521r1 -it oqs-curlv331 perftestServerECDSA.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=mlkem1024		-e SIG_ALG=secp521r1 -it oqs-curlv331 perftestServerECDSA.sh


#mldsa87
docker run -e TEST_TIME=10 -e KEM_ALG=P-521 	-e SIG_ALG=mldsa87 -it oqs-curlv331 perftestServer.sh
docker run -e TEST_TIME=10 -e KEM_ALG=mlkem1024 -e SIG_ALG=mldsa87 -it oqs-curlv331 perftestServer.sh


#falcon1024
docker run -e TEST_TIME=10 -e KEM_ALG=P-521 		-e SIG_ALG=falcon1024 -it oqs-curlv331 perftestServer.sh
docker run -e TEST_TIME=10 -e KEM_ALG=mlkem1024 	-e SIG_ALG=falcon1024 -it oqs-curlv331 perftestServer.sh


#sphincs256f
docker run  -e TEST_TIME=10 -e KEM_ALG=P-521 	 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256fsimple -it oqs-curlv331 perftestServer.sh


#sphincs256s
docker run  -e TEST_TIME=10 -e KEM_ALG=P-521 	 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestServer.sh
docker run  -e TEST_TIME=10 -e KEM_ALG=mlkem1024 -e SIG_ALG=sphincssha2256ssimple -it oqs-curlv331 perftestServer.sh

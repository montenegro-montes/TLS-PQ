#!/bin/bash

#RSA
docker run -e KEM_ALG=X25519   -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_mgf1_md:sha256 -e SIG_RSA_MD2=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestServerRSA.sh
docker run -e KEM_ALG=P-256    -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_mgf1_md:sha256 -e SIG_RSA_MD2=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestServerRSA.sh
docker run -e KEM_ALG=mlkem512 -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_mgf1_md:sha256 -e SIG_RSA_MD2=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestServerRSA.sh

#ed25519
docker run -e KEM_ALG=X25519 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=P-256 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=mlkem512 -e SIG_ALG=ed25519 -it oqs-curlv331 perftestServer.sh

#FALCON
docker run -e KEM_ALG=X25519 	-e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=P-256 	-e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=mlkem512 	-e SIG_ALG=falcon512 -it oqs-curlv331 perftestServer.sh


#Sphincssha2128fsimple
docker run -e KEM_ALG=X25519    -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=P-256     -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=mlkem512  -e SIG_ALG=sphincssha2128fsimple -it oqs-curlv331 perftestServer.sh


#Sphincssha2128simple
docker run -e KEM_ALG=X25519    -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=P-256     -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestServer.sh
docker run -e KEM_ALG=mlkem512  -e SIG_ALG=sphincssha2128ssimple -it oqs-curlv331 perftestServer.sh





#!/bin/bash

docker run -e KEM_ALG=X25519   -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestHandshakeRSA3072.sh
docker run -e KEM_ALG=P-256    -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestHandshakeRSA3072.sh
docker run -e KEM_ALG=kyber512 -e SIG_KEY=rsa_keygen_bits:3072  -e SIG_MD=rsa_pss_keygen_md:sha256 -it oqs-curlv331 perftestHandshakeRSA3072.sh


docker run -e KEM_ALG=x448    -e SIG_KEY=rsa_keygen_bits:4096  -e SIG_MD=rsa_pss_keygen_md:sha384  -it oqs-curlv331 perftestHandshakeRSA4096.sh






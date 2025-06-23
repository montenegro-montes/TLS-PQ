ARG LIBOQS_TAG=0.12.0
ARG OQSPROVIDER_TAG=0.8.0
#ARG OPENSSL_TAG=openssl-3.3.1
ARG OPENSSL_TAG=openssl-3.4
ARG MAKE_DEFINES="-j 4"     
ARG LIBOQS_BUILD_DEFINES="-DOQS_DIST_BUILD=ON"
ARG BASEDIR=/opt
ARG INSTALLDIR=${BASEDIR}/oqssa
ARG LIBOQSDIR=${BASEDIR}/liboqs
ARG OPENSSLDIR=${BASEDIR}/openssl
ARG OQSPROVIDERDIR=${BASEDIR}/oqs-provider
ARG LIBDIR

# --------------------------------------
# Stage 1: Install all necessary tools
# --------------------------------------
FROM ubuntu:24.10 AS base

# Install required build tools and system dependencies.
RUN apt update && apt install -y --no-install-recommends \
    cmake gcc ninja-build libunwind-dev \
    pkg-config build-essential \
    cargo git wget ca-certificates \
    openssl libssl-dev \  
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# --------------------------------------
# Stage 2: Download all necessary sources
# --------------------------------------
FROM base AS download
ARG BASEDIR
ARG LIBOQS_TAG
ARG OPENSSL_TAG
ARG OQSPROVIDER_TAG
ARG OPENSSLDIR

# Download and prepare source files needed for the build process.
WORKDIR $BASEDIR
RUN [ ! -d "${LIBOQSDIR}" ] && \ 
    mkdir liboqs && \  
    git clone --recursive --depth 1 --branch ${LIBOQS_TAG} https://github.com/open-quantum-safe/liboqs.git 
RUN [ ! -d "${OPENSSLDIR}" ] && \ 
    mkdir openssl && \
    git clone --depth 1 --branch ${OPENSSL_TAG} https://github.com/montenegro-montes/openssl.git

# Modificar límites en speed.c
WORKDIR ${OPENSSLDIR}
RUN sed -i 's/#define MAX_SIG_NUM .*/#define MAX_SIG_NUM 512/' ./apps/speed.c && \
    sed -i 's/#define MAX_KEM_NUM .*/#define MAX_KEM_NUM 512/' ./apps/speed.c


WORKDIR $BASEDIR    
RUN [ ! -d "${OQSPROVIDERDIR}" ] && \ 
    mkdir oqs-provider && \
    git clone --depth 1 --branch ${OQSPROVIDER_TAG} https://github.com/open-quantum-safe/oqs-provider.git 


# --------------------------------------
# Stage 3: Build the tools
# --------------------------------------
FROM download AS build
ARG MAKE_DEFINES     
ARG LIBOQS_BUILD_DEFINES
ARG INSTALLDIR
ARG LIBOQSDIR
ARG OPENSSLDIR
ARG OQSPROVIDERDIR
ARG LIBDIR

# Build and install liboqs
WORKDIR ${LIBOQSDIR}/build
#RUN cmake -G"Ninja" .. ${LIBOQS_BUILD_DEFINES} -DCMAKE_INSTALL_PREFIX=${INSTALLDIR} && \
RUN cmake -G"Ninja" .. ${LIBOQS_BUILD_DEFINES} && \
    ninja -j"$(nproc)" && \
    ninja install

FROM build AS build_1
ARG MAKE_DEFINES     
ARG LIBOQS_BUILD_DEFINES
ARG INSTALLDIR
ARG LIBOQSDIR
ARG OPENSSLDIR
ARG OQSPROVIDERDIR
ARG LIBDIR

# Install required build tools and system dependencies.
RUN apt update && apt install -y --no-install-recommends python3 golang-go python3-pip && \ 
    pip install jinja2 tabulate pyyaml --break-system-packages 


# Build OpenSSL3. Necessary to check device architecture to get correct openssl library path
WORKDIR ${OPENSSLDIR}
RUN LIBDIR=$(uname -m | grep -q x86_64 && echo "lib64" || echo "lib") && \ 
    LDFLAGS="-Wl,-rpath -Wl,${INSTALLDIR}/${LIBDIR}" ./config shared --prefix=${INSTALLDIR} && \
    make ${MAKE_DEFINES} && make install_sw install_ssldirs;



# --------------------------------------
# Stage 4: Configure the tools
# --------------------------------------
FROM build_1 AS configure
ARG INSTALLDIR
ARG OQSPROVIDERDIR
ARG LIBOQSDIR

# set path to use 'new' openssl. Dyn libs have been properly linked in to match
ENV PATH="${INSTALLDIR}/bin:${PATH}"

# Configure oqs-provider to activate all algorithms
WORKDIR ${OQSPROVIDERDIR}
RUN sed -i "s/false/true/g" oqs-template/generate.yml && \ 
    LIBOQS_SRC_DIR=${LIBOQSDIR} python3 oqs-template/generate.py

# Build OQS provider and copy it in the right location
WORKDIR ${OQSPROVIDERDIR}
RUN ln -s ../openssl . && \
    cmake -DOPENSSL_ROOT_DIR=${INSTALLDIR} -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=${INSTALLDIR} -S . -B _build && \
    cmake --build _build 

RUN LIBDIR=$(uname -m | grep -q x86_64 && echo "lib64" || echo "lib") && \ 
    cp _build/lib/oqsprovider.so ${INSTALLDIR}/${LIBDIR}/ossl-modules/


# Modify the openssl configuration file to use the OQS provider
RUN sed -i "s/default = default_sect/default = default_sect\noqsprovider = oqsprovider_sect/g" ${INSTALLDIR}/ssl/openssl.cnf && \
    sed -i "s/\[default_sect\]/\[default_sect\]\nactivate = 1\n\[oqsprovider_sect\]\nactivate = 1\n/g" ${INSTALLDIR}/ssl/openssl.cnf && \
    sed -i "s/providers = provider_sect/providers = provider_sect\nssl_conf = ssl_sect\n\n\[ssl_sect\]\nsystem_default = system_default_sect\n\n\[system_default_sect\]\nGroups = \$ENV\:\:DEFAULT_GROUPS\n/g" ${INSTALLDIR}/ssl/openssl.cnf && \ 
    sed -i "s/\# Use this in order to automatically load providers/\# Set default KEM groups if not set via environment variable\nKDEFAULT_GROUPS = $DEFAULT_GROUPS\n\n# Use this in order to automatically load providers/g" ${INSTALLDIR}/ssl/openssl.cnf && \
    sed -i "s/HOME\t\t\t= ./HOME\t\t= .\nDEFAULT_GROUPS\t= ${DEFAULT_GROUPS}/g" ${INSTALLDIR}/ssl/openssl.cnf

# --------------------------------------
# Stage 2: Runtime - Create a lightweight image with essential binaries and configurations.
# --------------------------------------
FROM ubuntu:24.10 AS runtime
ARG INSTALLDIR
ARG OQSPROVIDERDIR

# set path to use 'new' openssl and link it with the OQS provider
ENV PATH="${INSTALLDIR}/bin:${PATH}"
ENV OPENSSL=${INSTALLDIR}/bin/openssl
ENV OPENSSL_CNF=${INSTALLDIR}/ssl/openssl.cnf

RUN apt-get update && \ 
    apt-get install -y --no-install-recommends ca-certificates iproute2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy necessary files from the build stage
COPY --from=configure ${INSTALLDIR} ${INSTALLDIR}
COPY --from=configure ${OQSPROVIDERDIR}/_build/lib/oqsprovider.so /tmp

# Copy openssl and oqs files in default location just in case
RUN cp $INSTALLDIR/ssl/openssl.cnf $(openssl version -m | cut -d '"' -f2) && \
    LIBDIR=$(uname -m | grep -q x86_64 && echo "lib64" || echo "lib") && \ 
    cp ${INSTALLDIR}/${LIBDIR}/ossl-modules/* $(openssl version -d | cut -d '"' -f2)

# Copy local files into the machine
COPY scripts/*.sh ${INSTALLDIR}/bin

WORKDIR ${INSTALLDIR}/bin

CMD ["/bin/bash"]

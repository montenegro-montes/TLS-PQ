#!/bin/sh
set -e

if [ "x$TYPE" = "x" ]; then
  export TYPE="PERFORMANCE" #PERFORMANCE / HANDSHAKE
fi

if [ "x$AUTH" = "x" ]; then
  export AUTH="SINGLE"     #SINGLE / MUTUAL
fi

if [ "x$NUM_RUNS" = "x" ]; then
  export NUM_RUNS=50
fi

if [ "x$TC_DELAY" = "x" ]; then
    TC_DELAY="0ms"
fi    

if [ "x$TC_LOSS" = "x" ]; then
    TC_LOSS="0%"
fi 

echo "tc"
tc qdisc add dev lo root netem delay $TC_DELAY loss $TC_LOSS

echo "Showing qdisc status for the interface: lo"
tc -s qdisc show dev lo

if [ "x$KEM_ALG" = "x" ]; then
  export DEFAULT_GROUPS=kyber512
else
  export DEFAULT_GROUPS=$KEM_ALG
fi

# Optionally set SIG to one defined in https://github.com/open-quantum-safe/oqs-provider#algorithms
if [ "x$SIG_ALG" = "x" ]; then
  export SIG_ALG=dilithium2
fi

# Optionally set TEST_TIME
if [ "x$TEST_TIME" = "x" ]; then
  export TEST_TIME=1
fi

mkdir /opt/test/

./doCert.sh "$SIG_ALG"


echo "Running $0 with SIG_ALG=$SIG_ALG and KEM_ALG=$KEM_ALG"
echo

# Start a TLS1.3 test server based on OpenSSL accepting only the specified KEM_ALG

if [ "$AUTH" = "MUTUAL" ]; then
  openssl s_server -cert /opt/test/server.crt -key /opt/test/server.key -groups $DEFAULT_GROUPS -www -tls1_3 -verify 1 -verifyCAfile /opt/test/CA.crt -accept localhost:4433&
else 
  openssl s_server -cert /opt/test/server.crt -key /opt/test/server.key -groups $DEFAULT_GROUPS -www -tls1_3 -accept localhost:4433 &
fi

SERVER_PID=$!

# Give server time to come up first:
sleep 1


if [ "$TYPE" = "HANDSHAKE" ]; then


    if [ "$AUTH" = "MUTUAL" ]; then
          openssl s_client -connect localhost:4433 -state -servername localhost -CAfile /opt/test/CA.crt -showcerts -cert /opt/test/user.crt -key /opt/test/user.key
        else 
          openssl s_client -connect :4433 -state -servername localhost  -CAfile /opt/test/CA.crt -showcerts
    fi


else
      
      i=1
      while [ $i -le $NUM_RUNS ]
      do
        echo "Execution $i"

        if [ "$AUTH" = "MUTUAL" ]; then
          openssl s_time -connect :4433 -new -time $TEST_TIME -verify 1 -CAfile /opt/test/CA.crt -cert /opt/test/user.crt -key /opt/test/user.key | grep connections
        else 
          openssl s_time -connect :4433 -new -time $TEST_TIME -verify 1 -CAfile /opt/test/CA.crt  | grep connections
        fi

        i=$((i + 1))

      done
fi

kill $SERVER_PID






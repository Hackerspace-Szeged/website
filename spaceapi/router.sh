#!/bin/sh
machash=$(echo -n $3 | sha256sum | cut -d" " -f1)
if [ $2 = "AP-STA-CONNECTED" ]; then
wget -q -O /dev/null --post-data="device=$machash" https://api.szeged.hacker-space.hu/connect
elif [ $2 = "AP-STA-DISCONNECTED" ]; then
wget -q -O /dev/null --post-data="device=$machash" https://api.szeged.hacker-space.hu/disconnect
fi

+++
title = "Space-bridge"
author = "D3v"
+++

<center>![blueprint](/img/relay-net.svg)</center>

Sokszor vetődik fel az a kérdés, hogy milyen chat platformot használjunk. Egyesek ragaszkodnak az IRC-hez, mások a Telegram-hoz. Én személy szerint szeretem a discord-ot, mert az utóbbi időben a tanáraim ott tartották az órákat.
Levi hozta fel és üzemelte be a matterbridge nevű szoftvert, amely tükrüzte az üzeneteket a Discord és az IRC között. Miután készítettünk egy Telegram csatornát is, azt is beleintegráltuk az egészbe. Így lett a Hackerspace Relay Network, Space-bridge.

Itt látható a jelenlegi konfig:
<center>![config](/img/matterbridge-config.svg)</center>

Illetve a docker-compose.yml fájl tartalma:
<center>![config](/img/docker-config.svg)</center>
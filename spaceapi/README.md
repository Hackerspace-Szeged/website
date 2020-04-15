# Spaceapi backend

### Routeren:

Futtatása (ha több interface van, akkor mindegyiken futtassuk):
```
hostapd_cli -a router.sh -i wlan0
```

Openwrt-n szükséges csomagok:
```
hostapd-utils (https api esetén ssl/tls támogatás)
```

### A szerveren:

Futtatása:
```
python3 spaceapi.py
```

Ajánlott reverse proxy mögött futtatni. Konténerben is működik.
Ha újraindítjuk elfelejti az összes pillanatnyilag csatlakozott eszközt.
Megadhatunk fix hozzárendeléseket a devices.txt-ben:
```
MAC-cím hash:Név:Eszköznév
```

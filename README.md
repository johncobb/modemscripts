
<h2>Modem Scripts:</h2>
<b>enablehardware.py</b>

Scripts used to enable and crontrol the Janus-RC modem.
Running this command will powerup the onboard Janus-RC (Telit Modem)
It does not enumerate the serial port for commands.
This allows you to test the PPP dialer using pon and poff commands to establish
a PPP session.

Example:
Login to the pi on three separate terminals

1st Terminal (Logging):
```
tail -f /var/log/ppp/log
```

2nd Terminal (Enalbe Hardware)
```
cd ~/apps/modemscripts
sudo python enablehardware.py
```

3rd Terminal (PPP Dialer)
```
sudo pon hspa-kore # launch hspa-kore script
sudo poff hspa-kore # kill hspa-kore script
```
4th Add route so we can ssh through the ppp0 connection
(This can be added to /etc/ppp/ip-up.d/addroute)
```
sudo route add default dev ppp0
```
<b>enablemodem.py</b>

Script used to enable the modem hardware and start (pon) the PPP dialer. This establishes
a PPP connection to the cellular provider allowing application level TCP
access without the complexities of interfacing with the modem. 

Example:
```python
sudo enablemodem.py -p hspa-kore
```


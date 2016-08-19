
<h2>Modem Scripts:</h2>
<b>enablehardware.py</b>

Scripts used to enable and crontrol the Janus-RC modem.
Running this command will powerup the onboard Janus-RC (Telit Modem)
It does not enumerate the serial port for commands.
This allows you to test the PPP dialer using pon and poff commands to establish
a PPP session.

Provisioning Steps:
First we need to enable serial0. By default the current version of Raspbian comes with this disabled. This needs to be modified in two places.

# 1.) Make a backup pf cmdline.txt
```
cp cmdline.txt cmdline_bak.txt
```
# 2.) Modify the console parameter from serial0 to tty1
```
console=tty1
```
# 3.) Make a backup of config.txt
```
cp config.txt config_bak.txt
```
# 4.) Add the enable_uart parameter
```
enable_uart=1
```
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
sudo python enablemodem.py -p hspa-kore
```


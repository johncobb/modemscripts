enablehardware.py

sudo python enablehardware.py

Running this command will powerup the onboard Janus-RC (Telit Modem)
It does not enumerate the serial port for commands.
This allows you to test the PPP dialer using pon and poff commands to establish
a PPP session.

Example:
Login to the pi on three separate terminals

1st Terminal (Logging):
tail -f /var/log/ppp/log

2nd Terminal (Enalbe Hardware)
cd ~/apps/modemscripts
sudo python enablehardware.py

3rd Terminal (PPP Dialer)
sudo pon hspa-kore # launch hspa-kore script
sudo poff hspa-kore # kill hspa-kore script

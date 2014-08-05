import time
import os
import signal
import subprocess


def auto_ping():
	
	host = 'cphandheld.com'
	
	print "Pinging host: " + host
	
	proc = subprocess.Popen(['ping', host],stdout=subprocess.PIPE)
	
	response = proc.communicate()
	
	print "Results:"
	print response[0]

def auto_ip_show():
	

	netdev = 'eth0'
	
	print 'Querying ' + netdev + ':'
	
	proc = subprocess.Popen(['ip', 'addr', 'show','dev', netdev] , stdout=subprocess.PIPE)
	
	response = proc.communicate()
	
	print "Results:"
	print response[0]


def add_route():
	
	### Static route with route add
	# route add -host 72.3.250.113 dev ppp0
	
	#pppd = subprocess.Popen(['route', 'call', 'verizon'])
	
	routeIp = '23.253.112.132'
	
	print "Adding static route: " + routeIp

	proc = subprocess.Popen(['route', 'add', '-host', routeIp, 'dev', 'ppp0'],stdout=subprocess.PIPE)
	#proc = subprocess.Popen(['route add', '-host', routeIp, 'dev', 'ppp0'],stdout=subprocess.PIPE)
	
	#print "Process Id: %d" % proc.pid
	
def auto_pppd():
	
	command = 'verizon'
	#command = 'att'
	print "Calling pppd: " + command

	proc = subprocess.Popen(['pppd', 'call', command],stdout=subprocess.PIPE)
	
	#response = proc.communicate()
	
	#print "Results:"
	#print response[0]
	
def auto_pon():
	

	provider = 'verizon'
	
	print 'pon ' + provider + ':'
	
	proc = subprocess.Popen(['pon', provider] , stdout=subprocess.PIPE)
	
	response = proc.communicate()
	
	print "Results:"
	print response[0]
	
	
def auto_poff():
	

	provider = 'verizon'
	
	print 'poff ' + provider + ':'
	
	proc = subprocess.Popen(['poff', provider] , stdout=subprocess.PIPE)
	
	response = proc.communicate()
	
	print "Results:"
	print response[0]

	

if __name__ == '__main__':
	add_route()
	#auto_ping()
	#auto_ip_show()
	#auto_route()
	
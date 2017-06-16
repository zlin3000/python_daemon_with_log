#!/usr/bin/env python

########################################################################################################
# Modified from source:
#	https://gist.github.com/mvliet/7649806
#	https://www.electricmonk.nl/log/2011/08/14/redirect-stdout-and-stderr-to-a-logger-in-python/
#	https://github.com/serverdensity/python-daemon/blob/master/daemon.py
########################################################################################################



import sys, time, os, logging
from daemon import Daemon
from streamtologger import StreamToLogger

def printSome(some):
	while True:
		print some
		time.sleep(1)

def initial_logger():
	stdout_logger = logging.getLogger('STDOUT')
	sl = StreamToLogger(stdout_logger, logging.INFO)
	sys.stdout = sl

	stderr_logger = logging.getLogger('STDERR')
	sl = StreamToLogger(stderr_logger, logging.ERROR)
	sys.stderr = sl


class MyDaemon(Daemon):
	def run(self):
		initial_logger()
		printSome(os.getcwd()) 

if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        
	logging.basicConfig(
  	level=logging.DEBUG,
   	format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
   	filename="out.log",
   	filemode='a'
	)

	if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)

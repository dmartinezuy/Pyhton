import time
import sys
def do_task():
	time.sleep(1)
def example_1(n):
	for i in range(n):
		do_task()
		print '\b.',
		sys.stdout.flush()
	print ' Listo!'
	
print 'Iniciando',
example_1(10)
from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep

board = Arduino('/dev/ttyACM0', baudrate = 250000)
sleep(5)
it = util.Iterator(board)
it.start()

class Sensor:
	def __init__(self, pin, valor):
		self.pin = pin
		self.valor = valor
	def status(self):
		pino = board.get_pin('a:'pin':i')
		pin1.enable_reporting
		if(pino.read() > 0.500):
			return 1
		else
			return 0
		
sensor = Sensor(2,500)
while 1:
	print(sensor.status())
	sleep(1)


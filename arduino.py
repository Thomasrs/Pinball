class Sensor:
	def __init__(self, pin, valor):
		self.pin = board.get_pin('d:{0}:i'.format(pin))
		self.valor = valor
		self.pin.enable_reporting
		sleep(0.05)
	def status(self):
		if(self.pin.read() == 1:
			return 1
		else:
			return 0
		
#sensor = Sensor(2,500)
#while 1:
#	print(sensor.status())
#	sleep(0.05)

	

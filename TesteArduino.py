from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep

board = Arduino('/dev/ttyACM0')
sleep(5)

print("inicio")
it = util.Iterator(board)
it.start()
pin1 = board.get_pin('a:2:i')
pin1.enable_reporting
sleep(1)

pontuacao = 0
while 1:
	
	if(pin1.read() > 500):
		pontuacao += 1
		sleep(0.05)
		print(pontuacao)
	


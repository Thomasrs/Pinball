from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep

board = Arduino('/dev/ttyACM0')
sleep(5)

print("inicio")
it = util.Iterator(board)
it.start()
pin1 = board.get_pin('d:9:i')
pin1.enable_reporting
sleep(1)
while 1:
	if(pin1.read())
	
class Player:
	
	def __init__(self): #Atributos do player
		self.vidas = 3 #Número de vidas
		self.pontuacao = 0 #Pontos
		
	def pontuar(self, pontos): #Aumentar pontuação
		self.pontuação += pontos
		#Se a pontuação exceder x tocamos uma músicas ou exibimos algo na tela
		#COCOCOCCOOMBOBREAKER
		
	def morrer(self): #Perder uma vida
		self.vidas -= 1
		if (self.vidas==0):
			self.nomear()
			self.__init__()
		

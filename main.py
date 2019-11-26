from pyfirmata import Arduino, util, INPUT, OUTPUT
from time import sleep
from player import Player
from arduino import Sensor

#Setup
board = Arduino('/dev/ttyACM0', baudrate = 250000)
sleep(5)
it = util.Iterator(board)
it.start()

#Declaração de variáveis
player = Player()
sens_inicio = Sensor()
sens_morte = Sensor()
sens0 = Sensor()
sens1 = Sensor()
sens2 = Sensor()
sens3 = Sensor()
sens4 = Sensor()
sens5 = Sensor()
sens6 = Sensor()
sens7 = Sensor()

#Execução do jogo
while True:
  telaInicial()#Exibe tela inicial até o lançamento da bola
  telaJogo()
  while True:
    if (sens0.status() == 1):
      player.pontuar(sens0.valor)
      telaJogo()
    if (sens1.status() == 1):
      player.pontuar(sens1.valor)
      telaJogo()
    if (sens2.status() == 1):
      player.pontuar(sens2.valor)
      telaJogo()
    if (sens3.status() == 1):
      player.pontuar(sens3.valor)
      telaJogo()
    if (sens4.status() == 1):
      player.pontuar(sens4.valor)
      telaJogo()
    if (sens5.status() == 1):
      player.pontuar(sens5.valor)
      telaJogo()
    if (sens6.status() == 1):
      player.pontuar(sens6.valor)
      telaJogo()
    if (sens7.status() == 1):
      player.pontuar(sens7.valor)
      telaJogo()
    if (sens_morte.status() == 1):
      player.morrer()
      if (player.vidas == 0):
        break
      else:
        telaTransicao(self.vidas)
  telaFinal()
  
def telaInicial():  
  while (sens_inicio.status() == 0):
    #Plotar gráficos da tela inicial
    
def telaJogo():
  
def telaTransicao(vidas):
  
def telaFinal():
  
      

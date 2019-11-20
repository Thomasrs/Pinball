#Setup
Player = player()
sensorInicio #Sensor de início de jogo
sensorPontuacao #Sensor genérico de pontuação
sensorPontuacao1
sensorPontuacao2
sensorPontuacao3

#Execução do jogo
while True:
  telaInicial()#Exibe tela inicial até o lançamento da bola
  
  
def telaInicial():  
  while sensorInicio=="inativo":
    #Plotar gráficos da tela inicial
      

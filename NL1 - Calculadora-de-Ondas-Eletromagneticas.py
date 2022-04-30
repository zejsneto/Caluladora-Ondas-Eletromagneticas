import math

#1
def calc_f():
  f = float(input('Entre o valor de f(Hz): '))

  lamb=(3*(10**8))/f
  
  k=2*math.pi/lamb
  
  w=(3*(10**8))*k
  
  print('\nO valor de lambda é: {:.2e} (m).'.format(lamb))
  print('O valor de k é: {:.2e} (rad/m).' .format(k))
  print('O valor de ω é: {:.2e} (rad/s).\n' .format(w))

#2
def calc_lambda():
  lamb = float(input('Entre o valor de lambda(m): '))
  
  k=2*math.pi/lamb
  
  w=(3*(10**8))*k
  
  f=(3*(10**8))/lamb
  
  print('\nO valor de f é: {:.2e} (Hz).'.format(f))
  print('O valor de k é: {:.2e} (rad/m).' .format(k))
  print('O valor de ω é: {:.2e} (rad/s).\n' .format(w))

#3
def calc_k():
  k = float(input('Entre o valor de k(rad/m): '))
  
  lamb=2*math.pi/k
  
  w=(3*(10**8))*k
  
  f=(3*(10**8))/lamb
  
  print('\nO valor de f é: {:.2e} (Hz).'.format(f))
  print('O valor de lambda é: {:.2e} (m).' .format(lamb))
  print('O valor de ω é: {:.2e} (rad/s).\n' .format(w))

#4
def calc_w():
  w = float(input('Entre o valor de w(rad/s): '))

  k=w/(3*(10**8))
  
  lamb=2*math.pi/k
  
  f=(3*(10**8))/lamb
  
  print('\nO valor de f é: {:.2e} (Hz).'.format(f))
  print('O valor de lambda é: {:.2e} (m).' .format(lamb))
  print('O valor de k é: {:.2e} (rad/m).\n' .format(k))
  
#5
def calc_em():
  bm = float(input('Entre o valor de Bm(T): '))

  em=bm*(3*(10**8))
  
  print('\nO valor de Em é: {:.2e} (V/m).\n'.format(em))

#6
def calc_bm():
  em = float(input('Entre o valor de Em(V/m): '))

  bm=em/(3*(10**8))
  
  print('\nO valor de Bm é: {:.2e} (T).\n'.format(bm))

#7
def calc_aEletro():
  bo = float(input('Entre o valor de Bo(T): '))

  eo=bo*(3*(10**8))
  
  print('\nO valor de Eo é: {:.2e} (V/m).\n'.format(eo))

#8
def calc_aMagnet():
  eo = float(input('Entre o valor de Eo(V/m): '))

  bo=eo/(3*(10**8))
  
  print('\nO valor de Bo é: {:.2e} (T).\n'.format(bo))

def main():
  while True:
    print("---***---\n")
    print("Escolha uma opção (0 a 8):\n")
    print("0 - Encerrar \n")
    print("1 - Inserir o valor de f (Hz)")
    print("2 - Inserir o valor de lambda (m)")
    print("3 - Inserir o valor de k (rad/m)")
    print("4 - Inserir o valor de w (rad/s)")
    print("5 - Inserir o valor de Bm (T)")
    print("6 - Inserir o valor de Em (V/m) ")
    print("7 - Calcular a amplitude do campo elétrico (V/m)/ (Entre: Bo)")
    print("8 - Calcular a amplitude do campo magnético (T)/ (Entre: Eo)\n")
    print("---***---\n")
    
    seletor = int(input("Digite a opção: "))
    if (seletor == 1):
      calc_f()
    if (seletor == 2):
      calc_lambda()
    if (seletor == 3):
      calc_k()
    if (seletor == 4):
      calc_w()
    if (seletor == 5):
      calc_em()
    if (seletor == 6):
      calc_bm()
    if (seletor == 7):
      calc_aEletro()
    if (seletor == 8):
      calc_aMagnet()
    elif(seletor==0):
      break
      
main()
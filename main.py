import math as math

def Dividir(x, y):
  valor = x/y
  sobra = x%y
  return [int(valor), sobra]

def FazerDivisao(x, y, qntCasas):
  resultadoV = Dividir(x, y)
  valorResultado = str(resultadoV[0]) + ","

  for i in range(qntCasas):
    resultadoV = Dividir(resultadoV[1] * 10, y)
    valorResultado += str(resultadoV[0])

  return valorResultado

qntLados = 1000000000000000000000000.0
Angulo = math.radians(360.0 / qntLados)

medida = math.sin(Angulo) * math.cos(Angulo/2)

numeroPi = FazerDivisao(medida * qntLados, 2, 100)

print("Numero PI Real:" + str(math.pi))
print ("Numero Pi Encontrado: " + numeroPi)
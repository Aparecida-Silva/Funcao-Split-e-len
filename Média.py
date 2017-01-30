nota1 = eval(input("Digite a sua primeira nota: "))
nota2 = eval(input("Digite a sua segunda nota: "))
print("")

if (nota1 <= 60 and nota2 <= 60):
  valor1 = nota1 * (100 / 100)
  print("O valor da sua primeira nota: ")
  print(valor1)
  valor2 = nota2 * (80 / 100)
  print("O valor da sua segunda nota: ")
  print(valor2)
  notafinal = valor1 + valor2
  print("")
  print("Sua média final foi: ", notafinal)
else:
  print("O valor da nota deve ser menor que 60!")

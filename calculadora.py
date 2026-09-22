def calcular(num1, num2, operacao):
  if oeracao == "+":
    return num1 + num2
  elif operacao == "-":
    return numm1 - num2
  elif operacao == "*":
    return num1 * num2
  elif operacao == "/":
    if num2 == 0:
      return "Não é possível dividir por zero."
    return num1 / num2
  else:
    return"Operação Inválida"
print("====== CALCULADORA PYTHON =====")
while True:
  try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha uma operação(+,-,*,/):")
    resultado = Calcular(num1, num2, operacao)
      print(f"Resultado:{resultado}")
  except ValueErro:
    print("Digite apenas números válidos")
    continuar = input("Deseja fazer outra operação? (s/n): ").lower()
    if continuar != "S":
      print("Calculadora Encerrada.")
      break

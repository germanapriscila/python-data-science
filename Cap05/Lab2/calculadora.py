print("\n******************* Calculadora em Python *******************"
      "\n\nSelecione o número da operação desejada:"
      "\n1 - Adição"
      "\n2 - Subtração"
      "\n3 - Multiplicação"
      "\n4 - Divisão")

opcao = input("\n\nDigite a opção desejada: ")

if opcao == "1":
    num1 = float(input("\n\nDigite o primeiro número: "))
    num2 = float(input("\n\nDigite o segundo número: "))
    print(f"\n\nResultado: {num1 + num2}")

elif opcao == "2":
    num1 = float(input("\n\nDigite o primeiro número: "))
    num2 = float(input("\n\nDigite o segundo número: "))
    print(f"\n\nResultado: {num1 - num2}")

elif opcao == "3":
    num1 = float(input("\n\nDigite o primeiro número: "))
    num2 = float(input("\n\nDigite o segundo número: "))
    print(f"\n\nResultado: {num1 * num2}")

elif opcao == "4":
    num1 = float(input("\n\nDigite o primeiro número: "))
    num2 = float(input("\n\nDigite o segundo número: "))
    print(f"\n\nResultado: {num1 / num2}")

else:
    print("\n\nOpção inválida")
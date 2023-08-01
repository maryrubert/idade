def idade_pessoa(nascimento, nome):
  idade = 2022 - nascimento
  if 1922<=nascimento<=2021:
   return print(idade)
  else:
    while True:
      try:
        nome = input("Digite seu nome completo:    ")
        nascimento = int(input("Digite o ano do nascimento:      "))

        idade = str(2022 - nascimento)
      except Exception as err:
        print(err)
        continue
      else:
        return print("Sua idade "+ nome +", hj é " + idade )

idade_pessoa(nascimento, nome)

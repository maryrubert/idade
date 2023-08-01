def idade_pessoa(nascimento, nome, idade):
  idade = 2022 - nascimento
  if 1922<=nascimento<=2021:
   return print(nome, nascimento)
  else:
    raise Exception("inválido") 
  
  while True:
    try:
      nome = input("Digite seu nome completo:    ")
      nascimento = int(input("Digite o ano do nascimento:      ")) 

      idade_pessoa(nascimento, nome, idade)
    except Exception as err:
      print(err)
      continue
    else:
      return print("Esse ano você completou {idade} anos")
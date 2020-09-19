#Jean Silas
#Paulo Kim
# Gabriel TKACZ

import random


heroi = {}
vilao ={}

heroi["nome"] = "Bob"
vilao["nome"] = "Patrick"

heroi["armadura_fisica"] = 10
vilao["armadura_fisica"] = 10

heroi["armadura_magica"] = 10
vilao["armadura_magica"] = 10

heroi["ataque"] = 4
vilao["ataque"] = 12

heroi["arma"] = 10
vilao["arma"] = 10


heroi["vida"] = 100
vilao["vida"] = 250

pocao = 3

def magia(vida_heroi,vida_vilao):
    magia=random.randint(1,10)
    if magia==1:
        vida_heroi-=5
    elif magia<=3:
        return vida_heroi,vida_vilao
    elif magia<=8:
        vida_vilao-=5
    else:
        vida_vilao-=10
    return vida_heroi,vida_vilao

def magia_negra(vida_heroi,vida_vilao):
    magia=random.randint(1,10)
    if magia==1:
        vida_vilao-=5
    elif magia<=3:
        return vida_heroi,vida_vilao
    elif magia<=8:
        vida_heroi-=5
    else:
        vida_heroi-=10
    return vida_heroi,vida_vilao


while heroi["vida"]>0 and vilao["vida"]>0:
    print("Para jogar, digite: atacar, magia, pocao ou upgrade")
    resposta = input('O que você deseja fazer nessa rodada? ')
    try:
        if resposta.lower()== 'upgrade':
            upgrade=input("Armadura ou arma? ")
            if upgrade.lower()=='arma':
                if heroi["arma"]==10:
                    print("Voce recebeu a espada de ferro.")
                    heroi["arma"]=15
                elif heroi["arma"]==15:
                    print("Voce recebeu a espada de diamante.")
                    heroi["arma"]=20
                elif heroi["arma"]==20:
                    print("Você já tem a melhor arma, escolha outra ação.")
                    continue
            if upgrade.lower()=='armadura':
                opcao_armadura = input('Magica ou fisica? ')
                if opcao_armadura.lower() == "fisica":
                    if heroi["armadura_fisica"]==10:
                        print("Voce recebeu a armadura fisica de ferro.")
                        heroi["armadura_fisica"]=15
                    elif heroi["armadura_fisica"]==15:
                        heroi["armadura_fisica"]=20
                        print("Voce recebeu a armadura fisica de diamante.")
                    elif heroi["armadura_fisica"]==20:
                        print("Você já tem a melhor armadura fisica, escolha outra ação.")
                        continue
                if opcao_armadura.lower() == "magica":
                    if heroi["armadura_magica"]==10:
                        print("Voce recebeu a armadura magica de ferro.")
                        heroi["armadura_magica"]=15
                    elif heroi["armadura_magica"]==15:
                        print("Voce recebeu a armadura magica de diamante.")
                        heroi["armadura_magica"]=20
                    elif heroi["armadura_magica"]==20:
                        print("Você já tem a melhor armadura magica, escolha outra ação.")
                        continue
        elif resposta.lower() == 'atacar':
            dano = random.randint(1, (heroi['ataque'] + heroi['arma']))
            vilao['vida'] -= dano
            print("Voce deu ", dano, "de dano.")

        elif resposta.lower() == 'magia':
            inicial_h=heroi['vida']
            inicial_v=vilao['vida']
            heroi['vida'],vilao['vida'] = magia(heroi['vida'],vilao['vida'])
            dano_h=inicial_h-heroi['vida']
            dano_v=inicial_v-vilao['vida']
            if dano_h != 0:
                print("Voce se deu ",dano_h," de dano com magia.")
            elif dano_v != 0:
                print("Voce deu ",dano_v," de dano no vilao com magia.")
                
        elif resposta.lower() == 'pocao':
            heroi['vida'] += 5
            pocao-=1
            print("Voce recuperou 5 de vida e esta com ", heroi['vida'])
            print("Voce tem ",pocao," pocoes.")

        vilao_acoes = ["atacar","magia","upgrade"]
        vilao_acao = random.choice(vilao_acoes)

        if vilao_acao == 'atacar':
            dano = random.randint(1,(vilao['ataque'] + vilao['arma']))
            heroi['vida'] -= dano
            print("O vilao te deu: ",dano," de dano.")
        elif vilao_acao == 'magia':
            inicial_h=heroi['vida']
            inicial_v=vilao['vida']
            heroi['vida'],vilao['vida'] = magia_negra(heroi['vida'],vilao['vida'])
            dano_h=inicial_h-heroi['vida']
            dano_v=inicial_v-vilao['vida']
            if dano_h != 0:
                print("O vilao te deu ",dano_h," de dano com magia.")
            elif dano_v != 0:
                print("O vilao se deu ",dano_v," de dano com magia.")
        elif vilao_acao == 'upgrade':
            if vilao['arma'] < 20:
                vilao["arma"] += 5
                print("O vilao melhorou sua arma.")
            elif vilao['armadura_fisica'] < 20:
                vilao['armadura_fisica']+=5
                print("O vilao melhorou sua armadura fisica.")
            elif vilao['armadura_magica'] < 20:
                vilao['armadura_magica']+=5
                print("O vilao melhorou sua armadura magica.")
        print("Vida do heroi: ",heroi['vida'])
        print("Vida do vilao: ",vilao['vida'])
    except(NameError):
        print("Digite uma ação válida.")
        continue
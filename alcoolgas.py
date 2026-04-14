from math import trunc

valorA=1.90
valorG=2.50
descontoA1=0.03
descontoA2=0.05
descontoG1=0.04
descontoG2=0.06
print("O valor da gasolina é R$",valorG,"por litro, com um desconto de",trunc(descontoG1*100),"% por litro até 20 litros ou",trunc(descontoG2*100),"% por litro acima disso.")
print("O valor do álcool é R$", valorA,"por litro, com um desconto de",trunc(descontoA1*100),"% por litro até 20 litros ou",trunc(descontoA2*100),"% por litro acima disso.")
escolha= str(input("Qual combustível você gostaria? A para álcool e G para gasolina."))
resposta={"a","g","A","G"}
while escolha not in resposta:
    print("Opcão inválida")
    escolha = str(input("Qual combustível você gostaria? A para álcool e G para gasolina."))
if escolha=="g" or escolha=="G":
    gas=float(input("Quantos litros de gasolina você deseja?"))
    while gas<=0:
        print("O valor é inválido.")
        gas = float(input("Quantos litros de gasolina você deseja?"))
    if 0<gas<=20:
        valorF=gas*valorG*(1-descontoG1)
        print("Para",gas,"litros de gasolina, você deve pagar R$",format(round(valorF,2)),".")
    elif gas>20:
        valorF=gas*valorG*(1-descontoG2)
        print("Para",gas,"litros de gasolina, você deve pagar R$",format(round(valorF,2)),".")
elif escolha=="a" or escolha=="A":
    alc=float(input("Quantos litros de álcool você deseja?"))
    while alc<=0:
        print("O valor é inválido.")
        alc = float(input("Quantos litros de álcool você deseja?"))
    if 0<alc<=20:
        valorF=alc*valorA*(1-descontoA1)
        print("Para",alc,"litros de álcool, você deve pagar R$",format(round(valorF,2)),".")
    elif alc>20:
        valorF=alc*valorA*(1-descontoA2)
        print("Para",alc,"litros de álcool, você deve pagar R$",format(round(valorF,2)),".")
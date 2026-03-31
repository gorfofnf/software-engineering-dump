num= int(input("Informe um número maior que 0 e menor que 1000."))
if 0<num<1000:
    centena= int(num/100)
    dezena= int((num-centena*100)/10)
    unidade= int(num-centena*100-dezena*10)
    print("O número tem",centena,"centena(s),",dezena,"dezenas(s) e",unidade,"unidade(s).")
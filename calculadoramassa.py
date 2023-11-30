concluir=False

numero1=[]
operacao=[]
numero2çç=[]

while(not concluir):
 numero1=int(input("digite o primeiro número da operação: "))
 operacao= str(input("digite o simbolo da operação matematica que você deseja usar: "))
 numero2çç= int(input("digite o segundo número da operação: "))
 concluir=False
 if operacao== "+": 
    resultado= numero1 + numero2çç
 elif operacao== "-":
    resultado= numero1 - numero2çç
 elif operacao== "*":
    resultado= numero1 * numero2çç
 elif operacao== "/":
    resultado= numero1 / numero2çç
 else: print("essa operação não pode ser efetuada")

 print(f"{numero1} + {numero2çç} = {resultado}")

 continuar= input("Deseja continuar s/n? ")
 if continuar=="n" : break
 

 



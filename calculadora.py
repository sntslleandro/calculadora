class Calculadora:
    def __init__(self,primeiro_numero,segundo_numero) -> None:
        self.primeiro_numero=primeiro_numero
        self.segundo_numero=segundo_numero

    def somar(self):
        return primeiro_numero+segundo_numero
    def subtrair(self):
        return primeiro_numero-segundo_numero
    def multiplicar(self):
        return primeiro_numero*segundo_numero
    def dividir(self):
        return primeiro_numero/segundo_numero
    def exponencial(self):
        return primeiro_numero**segundo_numero
    def modular(self):
        return primeiro_numero%segundo_numero

def menu():
    if opcao == 1:
        print (f"O resultado da soma entre {primeiro_numero} e {segundo_numero} é: {Calculadora.somar(self=int)}")

    elif opcao == 2:
        print (f"O resultado da subtração entre {primeiro_numero} e {segundo_numero} é: {Calculadora.subtrair(self=int)}")

    elif opcao == 3:
        print (f"O resultado da multiplicação entre {primeiro_numero} e {segundo_numero} é: {Calculadora.multiplicar(self=int)}")

    elif opcao == 4:
        print (f"O resultado da divisão entre {primeiro_numero} e {segundo_numero} é: {Calculadora.dividir(self=int)}")

    elif opcao == 5:
        print (f"O resultado de {primeiro_numero} elevado a {segundo_numero} é: {Calculadora.exponencial(self=int)}")

    elif opcao == 6:
        print (f"O resultado do módulo entre {primeiro_numero} e {segundo_numero} é: {Calculadora.modular(self=int)}")
opcao= int(input("Insira o número correspondente a operação que deseja efetuar: \n[1] Soma, \n[2] Subtração, \n[3] Multiplicação, \n[4] Divisão, \n[5] Exponencial, \n[6] Módulo: \n>>> "))
primeiro_numero = int(input("Informe o primeiro numero: "))
segundo_numero = int(input("Informe o segundo numero: "))
# Chama a classe calculadora, passa os numeros para serem calculados com a operação escolhida   
Calculadora(primeiro_numero, segundo_numero) 
menu() # Chama a função menu 
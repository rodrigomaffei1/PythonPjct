import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    while True:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        senha = gerar_senha(tamanho)
        print("Senha Gerada:", senha)

        continuar = input("Deseja gerar outra senha? (s/n) ")
        if continuar.lower() != 's':
            break

    print("Programa encerrado.")

if __name__ == "main__":
    main()
import random
import string

# Funcao para gerar uma senha aleatoria
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits # Define os caracteres a serem usandos na senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho)) # Gera a senha concatenando caracteres aleatorios
    return senha

# Funcao principal
def main():
    while True:
        tamanho = int(input("Digite o tamanho da senha desejada: ")) # Solicita o tamanho da senha Desejada
        senha = gerar_senha(tamanho) # Gera a senha com o tamanho especificado
        print("Senha Gerada:", senha) # Exibe a senha gerada

        continuar = input("Deseja gerar outra senha? (s/n) ") # Pergunta se deseja gerar outra senha
        if continuar.lower() != 's': 
            break

    print("Programa encerrado.")


if  __name__ == "__main__":
    main()
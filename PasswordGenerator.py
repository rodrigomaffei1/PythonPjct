import random
import string

# Funcao para gerar uma senha aleatoria
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits #Define os caracteres a serem usados na senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))# Gera a senha concatenando caracteres aleatorios
    return senha

# Funcao principal
def main():
    print("Bem-vindo ao Gerador de Senhas!")

    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha desejada (no minimo 4 caracteres): "))
            if tamanho < 4:
                print("Por favor, Digite um tamanho valido.")
                continue

            senha = gerar_senha(tamanho) # Gera a senha com o tamanho especificado
            print("senha Gerada:", senha)

            continuar = input("Deseja gerar outra senha? (s/n) ") #pergunta se deseja gerar outra senha
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor, digite um numero valido apra o tamanho da senha.")

    print("Obrigado por usar o Gerador de Senhas. Programa encerrado.")

if __name__ == "__main__":
    main()


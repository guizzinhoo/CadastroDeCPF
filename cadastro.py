import time

def menu():
    while True:
        print('-' * 20)
        time.sleep(0.50)
        print("   SISTEMA GERENCIADOR DE CONTATOS   ")
        time.sleep(0.50)
        print('-' * 20)
        time.sleep(0.50)
        print("\n")
        time.sleep(0.50)
        print("         ESCOLHA UMA OPÇÃO           ")
        time.sleep(0.50)
        print("\n")
        print("         0 - SAIR                    ")
        time.sleep(0.50)
        print("         1 - CADASTRAR               ")
        time.sleep(0.5)
        print("         2 - PESQUISAR POR CPF       ")
        time.sleep(0.50)
        print("         3 - PESQUISAR POR NOME      ")
        time.sleep(0.50)
        print("         4 - EXCLUIR CPF      ")
        time.sleep(0.50)
        print("         5 - EDITAR CPF      ")
        time.sleep(0.50)
        print("\n")
        print('-' * 20)
        time.sleep(0.50)
        print("\n")

        try:
            resposta = int(input("DIGITE A OPÇÃO ESCOLHIDA: "))
            if resposta == 0:
                print("\n")
                print("SAINDO DO SISTEMA...")
                break
            elif resposta == 1:
                cadastro()
            elif resposta == 2:
                pesquisacpf()
            elif resposta == 3:
                pesquisanome()
            elif resposta == 4:
                excluir()
            elif resposta == 5:
                editar()
            else:
                print("\n")
                print("ATENÇÃO: A OPÇÃO DIGITADA É INVÁLIDA.")
                print("\n")

        except ValueError:
            print("\n")
            print("ATENÇÃO: ERRO DE FORMATAÇÃO. DIGITE UM NÚMERO VÁLIDO.")
            print("\n")

def cadastro():
    cpf = input('Digite seu CPF: ')
    if existeCPF(cpf) != True:
        nome = input('Digite seu nome: ')
        data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        email = input('Digite seu email: ')
        wpp = input('Digite seu whatsapp: ')
        with open("contato.txt", "a") as arq:
            arq.write(f"{nome}??????{cpf}??????{data}??????{email}??????{wpp}\n")
        print('Dados cadastrados com sucesso!')

    else:
        print('\n')
        print('O CPF JÁ EXISTE NO NOSSO SISTEMA')
        print('\n')

def pesquisacpf():
    cpf = input('Digite o CPF que deseja pesquisar: ')

    try:
        with open('contato.txt', 'r') as arquivo:
            encontrado = False
            for linha in arquivo:
                dados = linha.strip().split("??????")
                if len(dados) != 5:
                    print(f"Linha mal formatada: {linha.strip()}")
                    continue
                if dados[1] == cpf:
                    print('-' * 20)
                    print("      RESULTADO DA PESQUISA")
                    print('-' * 20)
                    print(f'CPF: {dados[1]}')
                    print(f'Nome: {dados[0]}')
                    print(f'Data de nascimento: {dados[2]}')
                    print(f'E-mail: {dados[3]}')
                    print(f'Whatsapp: {dados[4]}')
                    encontrado = True
                    break
            if not encontrado:
                print("O CPF PESQUISADO NÃO EXISTE NA BASE DE DADOS.")
    except FileNotFoundError:
        print("ERRO: O arquivo de contatos não foi encontrado.")

def pesquisanome():
    nome = input('Digite o nome que deseja pesquisar: ')

    try:
        with open('contato.txt', 'r') as arquivo:
            encontrado = False
            for linha in arquivo:
                dados = linha.strip().split("??????")
                if len(dados) != 5:
                    print(f"Linha mal formatada: {linha.strip()}")
                    continue
                if dados[0].lower() == nome.lower():
                    print('-' * 20)
                    print("      RESULTADO DA PESQUISA")
                    print('-' * 20)
                    print(f'Nome: {dados[0]}')
                    print(f'CPF: {dados[1]}')
                    print(f'Data de nascimento: {dados[2]}')
                    print(f'E-mail: {dados[3]}')
                    print(f'Whatsapp: {dados[4]}')
                    encontrado = True
                    break
            if not encontrado:
                print("O NOME PESQUISADO NÃO EXISTE NA BASE DE DADOS.")
    except FileNotFoundError:
        print("ERRO: O arquivo de contatos não foi encontrado.")

def existeCPF(cpf):

    isCPF = False
    with open('contato.txt', 'r') as arq:
        for linha in arq:
            dados = linha.split('??????')
            if dados[1] == cpf:
                isCPF = True
    return isCPF  
def editar():
    print('\n')
    print('-'*20)
    cpf = input('DIGITE O CPF QUE DESEJA EDITAR: ')
    print('-'*20)
    if existeCPF(cpf) == True:

        linhas = []
        with open('contato.txt', 'r') as arq:
            linhas = arq.readlines()
            for linha in linhas:
                dados = linha.split('??????')
                if dados[1] == cpf:
                    print('\n')
                    print(f'CPF: {cpf}')
                    print(f'Nome: {dados[0]}')
                    print(f'Data de nascimento: {dados[2]}')
                    print(f'E-mail: {dados[3]}')
                    print(f'Whatsapp: {dados[4]}')
                    print('-'*20)
                    print('EDITE OS DADOS DO USUÁRIO')
                    print('\n')
                    break
        cpf = input('Digite seu CPF: ')
        nome = input('Digite seu nome: ')
        data = input('Digite sua data de nascimento (dd/mm/aaaa): ')
        email = input('Digite seu email: ')
        wpp = input('Digite seu whatsapp: ')
        with open('contato.txt', 'w') as arq:
            for linha in linhas:
                dados = linha.split('??????')
                if dados[1] != cpf:
                    arq.write(f"{nome}??????{cpf}??????{data}??????{email}??????{wpp}\n")

        print('-'*20)
        print('\n')
        print('CONTATO EDITADO COM SUCESSO')
    else:
        print('O CPF NÃO EXISTE EM NOSSA BASE DE DADOS')
def excluir():

    print('\n')
    print('-'*20)
    cpf = input('DIGITE O CPF QUE DESEJA EXCLUIR: ')
    print('-'*20)
    if existeCPF(cpf) == True:
        linhas = []
        with open('contato.txt', 'r') as arq:
            linhas = arq.readlines()
        with open('contato.txt', 'w') as arq:
            for linha in linhas:
                dados = linha.split('??????')
                if dados[1] != cpf:
                    arq.write(linha)

            print('CONTATO EXCLUÍDO')
    else:
        print('O CPF NÃO EXISTE EM NOSSA BASE DE DADOS')
def main():
    menu()

main()
#flag = existeCPF('3434')
#print(flag)

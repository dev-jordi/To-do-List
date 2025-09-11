def exibir_menu():
    # Mostra o menu principal de opções
    print("\nMenu:")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Excluir")
    print("4. Sair")

def carregar_tarefas():
    try:
        # Lê o arquivo de tarefas e retorna uma lista sem quebras de linha
        with open("tasks.txt", "r") as arquivo:
            tarefas = arquivo.readlines()
        return [tarefa.strip() for tarefa in tarefas]
    except FileNotFoundError:
        # Se o arquivo não existir, retorna lista vazia
        return []

def salvar_tarefas(tarefas):
    # Salva todas as tarefas no arquivo, uma por linha
    with open("tasks.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

def adicionar_tarefa(tarefas):
    # Recebe uma nova tarefa, adiciona e persiste no arquivo
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    # Mostra a lista de tarefas com índice
    if tarefas:
        print("\nTarefas:")
        for idx, tarefa in enumerate(tarefas, 1):
            print(f"{idx}. {tarefa}")
    else:
        print("Nenhuma encontrada.")

def excluir_tarefa(tarefas):
    # Permite remover uma tarefa pelo índice
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a ser excluída: "))
        if 1 <= indice <= len(tarefas):
            tarefas.pop(indice - 1)  # remove pelo índice ajustado
            salvar_tarefas(tarefas)
            print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    tarefas = carregar_tarefas()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            excluir_tarefa(tarefas)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
import threading
import time

# Definindo a função que a thread vai executar
def minha_tarefa(nome, duracao):
    print(f"Tarefa {nome} começou!")
    time.sleep(duracao)
    print(f"Tarefa {nome} terminou!")

# Criando threads
thread1 = threading.Thread(target=minha_tarefa, args=("A", 2))
thread2 = threading.Thread(target=minha_tarefa, args=("B", 3))

# Iniciando threads
thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print("Todas as tarefas terminaram!")

import threading
import time

class MinhaThread(threading.Thread):
    def __init__(self, nome, duracao):
        threading.Thread.__init__(self)
        self.nome = nome
        self.duracao = duracao

    def run(self):
        print(f"Tarefa {self.nome} começou!")
        time.sleep(self.duracao)
        print(f"Tarefa {self.nome} terminou!")

# Criando e iniciando threads
thread1 = MinhaThread("A", 2)
thread2 = MinhaThread("B", 3)

thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print("Todas as tarefas terminaram!")

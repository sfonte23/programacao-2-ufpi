import threading

# Variável compartilhada
contador = 0
# Lock para sincronização
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        # Adquirir o lock antes de modificar o contador
        lock.acquire()
        contador += 1
        # Liberar o lock após modificar o contador
        lock.release()

# Criando e iniciando 10 threads
threads = [threading.Thread(target=incrementar) for _ in range(10)]
for thread in threads:
    thread.start()

# Esperando as threads terminarem
for thread in threads:
    thread.join()

print(f"Valor final do contador: {contador}")

import random
import threading
import time

# lista compartilhada da fila
fila = []
# lock para garantir exclusão mútua ao acessar a lista
lock = threading.Lock()


# criando produtor
def produtor():
    while True:
        # gerar número aleatório
        numero = random.randint(1, 100)

        lock.acquire()
        # adicionar número à lista
        fila.append(numero)
        print(f"Produtor adicionou o número: {numero}")

        lock.release()

        # esperando 1 segundo antes de adicionar o próximo número
        time.sleep(1)

    # criando consumidor


def consumidor():
    while True:

        lock.acquire()
        if len(fila) > 0:
            # remover o primeiro número da lista (funcionando como uma fila)
            numero = fila.pop(0)
            print(f"Consumidor removeu o número: {numero}")

        lock.release()

        # esperando 1 segundo antes de remover o próximo número
        time.sleep(1)

    # Criar as threads para as funções produtor e consumidor


thread_produtor = threading.Thread(target=produtor)
thread_consumidor = threading.Thread(target=consumidor)

# Iniciar as threads
thread_produtor.start()
thread_consumidor.start()
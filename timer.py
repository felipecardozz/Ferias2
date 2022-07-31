Para esse programa fica bem mais facil se você escrever acompanhando esse site # Apagar depois pq não é codigo
https: // cadernodelaboratorio.com.br/tkinter-conhecendo-o-grid-em-maiores-detalhes/ # Sobre o tkinter, posicionamento e o layout do grid 

import threading
import time  # O time.sleep não deixa que os botoes sejam clicaos enquanto tenha contagem, ai o threading tira essa função colocando um reset
import tkinter as tk
from win10toast import ToastNotifier

# Ao definir uma classe usando self.root, essa classe se comporta da mesma forma que um elemento ou variável quando se usa a janela do tkinter
class Contador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometria("460x220") #Forma diferente de width e height
        self.root.title(Contador)

# O comom é ser self.time_entry, um elemento de user interface (UI) próximos arquivos vão estar todos em inglês 
# Esse .grid serve com uma posição de layout 

        self.tempo_entry = tk.Entry(self.root, font=("Arial", 30))
        self.tempo_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Primeiro botão que faz a contagem começar
        self.start_button = tk.Button(self.root, font=("Arial", 30), text="Começar", command=self.start_thread)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

# Coluna 2 onde colocamos o botão de parar a contagem do timer
        self.start_button = tk.Butoon(self.root, font=("Arial", 30), text="Parar", command=self.stop)  # Stop function
        self.start_button.grid(row=1, column=2, padx=5, pady=5)

        self.tempo_label = tk.Label(self.root, font=("Helvetica", 30), text="Tempo: 00:00:00")
        self.tempo_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    # Loop que faz o programa funcionar
        self.stop_loop = False
        self.root.mainloop()

# Defininado a função de começo


def start_thread(self):
    x = threading.Thread(target=self.start)
    x.start()


def start(self):
    self.stop_loop = False

    horas = 0
    minutos = 0
    segundos = 0

    # é o conteúdo do time entry
    string = self.tempo_entry.get().split(":")
    if len(string) == 3:
        horas = int(string[0])
        minutos = int(string[1])
        segundos = int(string[2])

    elif len(string) == 2:
        minutos = int(string[0])
        segundos = int(string[1])

    elif len(string) == 1:
        segundos = int(string[0])

    else:
        print("Não deu certo, favor tentar mais tarde")
        return

# Definindo como os segundos, horas e minutos se relacionam
    full_segundos = horas * 3600 + 3600 + minutos * 60 + segundos

    while full_segundos > 0 and not self.stop_loop:
        full_segundos -= 1

# Divmod converte quando 60 minutos se tornam uma hora e e voltam para
        minutos, segundos = divmod(full_segundos, 60)
        horas, minutos = divmod(minutos, 60)

# f string para nao ter que adicionar somando
        # 02d está especificando as colunas, assim 5 segundos são :05:
        self.tempo_label.config(
            text=f"Tempo: {horas:02d}: {minutos:02d} {segundos:02d}: ")
        self.root.update()
        time.sleep(1)

    if not self.stop_loop:
        toast = ToastNotifier()
        toast.show_toast("Contador", "Acabou o tempo", duracao=10)

# loop de parar 
def stop(self):
    self.stop_loop = True
    self.tempo_label.config(text="Text: 00:00:00")

Contador()

import time
import customtkinter as ctk

# Função para atualizar o relógio a cada segundo  Function to update the clock every second / Funzione per aggiornare l'orologio ogni secondo
def atualizar_relogio():
    hora_atual = time.strftime("%H:%M:%S")  # Formata a hora atual / Format current time / Formatta l'ora corrente
    relogio.configure(text=hora_atual)       # Atualiza o texto do label / Update label text / Aggiorna il testo della label
    app.after(1000, atualizar_relogio)      # Agenda próxima atualização em 1s / Schedule next update in 1s / Pianifica il prossimo aggiornamento in 1s

# Configuração da janela principal / Main window setup / Configurazione finestra principale
app = ctk.CTk()
app.geometry("400x200")  # Define tamanho da janela / Set window size / Imposta dimensione finestra

# Cria um label para exibir o relógio / Create a label to display the clock / Crea una label per visualizzare l'orologio
relogio = ctk.CTkLabel(app, font=("Arial", 24))
relogio.pack(pady=50)  # Adiciona padding vertical / Add vertical padding / Aggiunge padding verticale

# Inicia a atualização do relógio / Start clock update / Avvia l'aggiornamento dell'orologio
atualizar_relogio()

# Loop principal da aplicação / Main application loop / Ciclo principale dell'applicazione
app.mainloop()

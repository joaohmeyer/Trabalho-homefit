import tkinter as tk
from tkinter import font

# Função para quando o botão 'Ir para o menu inicial' for clicado
def ir_para_menu():
    print("Indo para o menu inicial...")

# Função para quando o botão 'Logar ou criar conta' for clicado
def logar_criar_conta():
    print("Logar ou criar conta...")

# Criação da janela principal
janela = tk.Tk()
janela.title("HomeFIT")
janela.geometry("300x500")  # Definindo o tamanho da janela

# Definindo uma fonte personalizada para o título
titulo_font = font.Font(family="Helvetica", size=24, weight="bold")

# Adicionando o ícone de pessoa 
icon_frame = tk.Frame(janela)
icon_frame.pack(pady=10)
icon_pessoa = tk.Label(icon_frame, text="👤", font=("Helvetica", 20))
icon_pessoa.pack()

# Título da aplicação
titulo = tk.Label(janela, text="HomeFIT", font=titulo_font)
titulo.pack(pady=10)

# Exemplo de um ícone de peso (pode ser substituído por uma imagem)
icone_peso = tk.Label(janela, text="🏋️", font=("Helvetica", 50))
icone_peso.pack(pady=20)

# Botão para ir ao menu inicial
botao_menu = tk.Button(janela, text="Ir para o menu inicial", font=("Helvetica", 14), command=ir_para_menu)
botao_menu.pack(pady=10)

# Botão para logar ou criar conta
botao_conta = tk.Button(janela, text="Logar ou criar conta", font=("Helvetica", 14), command=logar_criar_conta)
botao_conta.pack(pady=10)

# Iniciar o loop principal da interface
janela.mainloop()

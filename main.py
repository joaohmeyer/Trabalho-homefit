import tkinter as tk

# Configurações de estilo
BG_COLOR = "#F3F6FA"
BTN_COLOR = "#4A6FA5"
TEXT_COLOR = "#FFFFFF"
BTN_FONT = ("Helvetica", 12, "bold")
TITLE_FONT = ("Helvetica", 16, "bold")
LABEL_FONT = ("Helvetica", 10)

# Descrições dos exercícios
descricoes_exercicios = {
    7: "Exercício 1: Alongamento para pescoço. Realize 3x10 repetições com pausas de 30s.",
    8: "Exercício 2: Alongamento para ombros. Realize 3x10 repetições com pausas de 30s.",
    9: "Exercício 3: Alongamento para braços. Realize 3x10 repetições com pausas de 30s.",
    10: "Exercício 4: Alongamento para costas. Realize 3x10 repetições com pausas de 30s.",
    11: "Exercício 5: Alongamento para pernas. Realize 3x10 repetições com pausas de 30s.",
    12: "Exercício 6: Alongamento para quadris. Realize 3x10 repetições com pausas de 30s.",
    13: "Exercício 7: Alongamento para tornozelos. Realize 3x10 repetições com pausas de 30s.",
    14: "Exercício 8: Alongamento completo. Realize 3x10 repetições com pausas de 30s."
}

# Variável global para controlar o dia selecionado
dia_selecionado = None

# Função para exibir cada tela com o design personalizado e navegação correta
def exibir_tela(numero_tela):
    global dia_selecionado
    for widget in janela.winfo_children():
        widget.destroy()  # Limpa a tela anterior

    janela.configure(bg=BG_COLOR)

    # Funções de navegação entre telas
    def criar_botao(texto, destino):
        return tk.Button(janela, text=texto, command=lambda: exibir_tela(destino),
                         bg=BTN_COLOR, fg=TEXT_COLOR, font=BTN_FONT, relief="flat", padx=10, pady=5)

    # Tela 1: Login
    if numero_tela == 1:
        tk.Label(janela, text="HomeFIT", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        tk.Label(janela, text="Faça o Login para Acessar", font=LABEL_FONT, bg=BG_COLOR).pack()

        tk.Entry(janela, font=LABEL_FONT, width=30).pack(pady=5)
        tk.Entry(janela, font=LABEL_FONT, width=30, show="*").pack(pady=5)

        criar_botao("Login", 2).pack(pady=10)
        criar_botao("Cadastrar-se aqui", 3).pack(pady=5)

    # Tela 2: Bem-vindo
    elif numero_tela == 2:
        tk.Label(janela, text="Seja Bem-Vindo!", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        criar_botao("Voltar para Tela 1", 1).pack(pady=10)

    # Tela 3: Cadastro
    elif numero_tela == 3:
        tk.Label(janela, text="Faça seu Cadastro", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        tk.Label(janela, text="Nome:", font=LABEL_FONT, bg=BG_COLOR).pack()
        tk.Entry(janela, font=LABEL_FONT, width=30).pack(pady=5)

        tk.Label(janela, text="Email:", font=LABEL_FONT, bg=BG_COLOR).pack()
        tk.Entry(janela, font=LABEL_FONT, width=30).pack(pady=5)

        tk.Label(janela, text="Senha:", font=LABEL_FONT, bg=BG_COLOR).pack()
        tk.Entry(janela, font=LABEL_FONT, width=30, show="*").pack(pady=5)

        criar_botao("Cadastrar", 4).pack(pady=10)
        criar_botao("Voltar", 1).pack(pady=5)

    # Tela 4: Formulário Nova Rotina
    elif numero_tela == 4:
        tk.Label(janela, text="Formulário de Nova Rotina", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        tk.Label(janela, text="Deseja adicionar uma nova rotina?", font=LABEL_FONT, bg=BG_COLOR).pack()
        criar_botao("Continuar", 5).pack(pady=10)
        criar_botao("Voltar para Tela 3", 3).pack(pady=5)

    # Tela 5: Progresso
    elif numero_tela == 5:
        tk.Label(janela, text="Seu Progresso", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        tk.Label(janela, text="[Gráfico de Progresso]", font=LABEL_FONT, bg=BG_COLOR).pack(pady=10)

        criar_botao("Ir para Cronograma", 6).pack(pady=10)
        criar_botao("Voltar para Tela 4", 4).pack(pady=5)

    # Tela 6: Cronograma Semanal
    elif numero_tela == 6:
        tk.Label(janela, text="Cronograma Semanal", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        dias_semana = {
            "Segunda-feira": 16, "Terça-feira": 16, "Quarta-feira": 16,
            "Quinta-feira": 16, "Sexta-feira": 16, "Sábado": 16, "Domingo": 16
        }
        for dia, destino in dias_semana.items():
            tk.Button(janela, text=dia, bg=BTN_COLOR, fg=TEXT_COLOR, font=LABEL_FONT, relief="flat",
                      command=lambda d=dia: abrir_exercicios_do_dia(d)).pack(pady=2)

        criar_botao("Voltar para Progresso", 5).pack(pady=10)

    # Tela 16: Lista de Exercícios para o Dia Selecionado
    elif numero_tela == 16:
        tk.Label(janela, text=f"Exercícios - {dia_selecionado}", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        for i in range(1, 8):
            criar_botao(f"Exercício {i}", 6 + i).pack(pady=2)

        criar_botao("Voltar para Cronograma", 6).pack(pady=10)

    # Telas 7-14: Exercícios individuais com descrição
    elif numero_tela in range(7, 15):
        tk.Label(janela, text=f"Exercício {numero_tela - 6}", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        descricao = descricoes_exercicios.get(numero_tela, "Descrição do exercício não disponível.")
        tk.Label(janela, text=descricao, font=LABEL_FONT, bg=BG_COLOR, wraplength=300).pack(pady=10)

        # Navegação entre os exercícios e para voltar ao menu do dia
        criar_botao("Voltar para Lista de Exercícios", 16).pack(pady=5)
        if numero_tela > 7:
            criar_botao("Exercício Anterior", numero_tela - 1).pack(side="left", padx=10)
        if numero_tela < 14:
            criar_botao("Próximo Exercício", numero_tela + 1).pack(side="right", padx=10)

    # Tela 15: Parabéns
    elif numero_tela == 15:
        tk.Label(janela, text="Parabéns!", font=TITLE_FONT, bg=BG_COLOR, fg=BTN_COLOR).pack(pady=20)
        tk.Label(janela, text="Você completou os alongamentos de hoje!", font=LABEL_FONT, bg=BG_COLOR).pack(pady=10)
        criar_botao("Voltar para Progresso", 5).pack(pady=10)

# Função para abrir a lista de exercícios de um dia específico
def abrir_exercicios_do_dia(dia):
    global dia_selecionado
    dia_selecionado = dia
    exibir_tela(16)

# Configuração da janela principal
janela = tk.Tk()
janela.title("HomeFIT")
janela.geometry("400x600")

# Iniciar na tela 1
exibir_tela(1)

janela.mainloop()

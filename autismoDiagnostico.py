# Imports
import tkinter as tk
from tkinter import messagebox, ttk

# Cores do Aplicativo
cor_fundo = "#1E1E1E"
cor_fontePrincipal = "#FFFFFF"
cor_fonteSecundaria = "#837B6F"

# Configurações da Janela Principal
janela = tk.Tk()
janela.title("Diagnóstico de Autismo")
janela.geometry("850x400")
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

# Mostra o Título da janela
titulo = tk.Label(janela, text="Diagnóstico de Autismo", font=("Helvetica", 22, "bold"), bg=cor_fundo, fg=cor_fontePrincipal)
titulo.pack(pady=5, ipadx=5, ipady=5)

# Subtítulo, aviso importante.
instrucoes = tk.Label(janela, text="Esse formulário não substitui uma avaliação profissional completa.", font=("Helvetica", 13), bg=cor_fundo, fg=cor_fonteSecundaria)
instrucoes.pack(pady=7)

# Rodapé com o nome dos integrantes do grupo.
rodape = tk.Label(janela, text="Grupo Desenvolvedor: Juliene, Diego, Maria Julia, Gabriel Torres, Gabriel da Silva", font=("Helvetica", 8), bg=cor_fundo, fg=cor_fonteSecundaria)
rodape.pack(side="bottom", pady=10)

# Perguntas e opções de resposta com pontuação equivalente
perguntas = [
    
    # Tópico de Comunicação
    ## Pergunta 1
    ("O paciente tem dificuldades em manter uma conversa ou iniciar interações?", 
     ("Sim, o paciente evita iniciar conversas e responde de maneira muito limitadas.", 1), 
     ("Não, o paciente mantém conversas normais, sem dificuldades aparentes.", 0), 
     ("O paciente responde perguntas mas raramente inicia uma conversa.", 0.5)),

    ## Pergunta 2
    ("O paciente mostra falta de reciprocidade emocional?", 
     ("Sim, o paciente não responde adequadamente a demonstrações de afeto e parece indiferente.", 1), 
     ("Não, o paciente responde emocionalmente como esperado.", 0), 
     ("Às vezes, o paciente responde com gestos de afeto, mas não de forma constante", 0.5)),

    # Tópico de Comportamento
    ## Pergunta 3
    ("O paciente mantém contato visual durante as interações?", 
     ("Não, o paciente evita completamente o contato visual.", 1), 
     ("Sim, o paciente mantém contato visual normal durante a conversa.", 0), 
     ("O paciente faz contato visual, mas apenas brevemente.", 0.5)),

    ## Pergunta 4
    ("O paciente apresenta movimentos repetitivos como balançar ou agitar as mãos?", 
     ("Sim, o paciente balança o corpo frequentemente", 1), 
     ("Não, o paciente não apresenta esse tipo de comportamento", 0), 
     ("O paciente tem comportamentos repetitivos ocasionais, mas não com frequência.", 0.5)),

    ## Pergunta 5
    ("O paciente segue rotinas rígidas e reage mal a mudanças?", 
     ("Sim, o paciente fica muito ansioso com qualquer alteração na rotina.", 1), 
     ("Não, o paciente lida bem com mudanças na rotina.", 0), 
     ("O paciente prefere rotinas, mas consegue lidar com pequenas mudanças.", 0.5)),

    ## Pergunta 6
    ("O paciente tem fixação em interesses incomuns?", 
     ("Sim, o paciente passa horas focado em um único tema ou objeto", 1), 
     ("Não, o paciente tem interesses diversos e variados.", 0), 
     ("O paciente mostra interesse por tópicos específicos, mas sem uma fixação incomum.", 0.5)),

    # Tópico de Sensibilidade
    ## Pergunta 7
    ("O paciente tem hipersensibilidade a sons, luzes ou texturas?", 
     ("Sim, o paciente se incomoda muito com barulhos altos e texturas de certas roupas.", 1), 
     ("Não, o paciente não mostra sinais de sensibilidade anormal a estímulos.", 0), 
     ("O paciente é sensível a estímulos sensoriais, mas consegue se adaptar na maioria das vezes.", 0.5)),

    ## Pergunta 8
    ("O paciente evita certos tipos de alimentos devido a textura ou sabor?", 
     ("Sim, o paciente só come alimentos com texturas específicas e rejeita a maioria dos outros", 1), 
     ("Não, o paciente come alimentos sem restrições relacionadas à textura ou sabor.", 0), 
     ("O paciente tem preferências alimentares, mas ainda come uma variedade razoável de alimentos.", 0.5)),

    ## Pergunta 9
    ("O paciente cobre os ouvidos ou se afasta em ambientes barulhentos?", 
     ("Sim, o paciente cobre os ouvidos sempre que há barulho ou multidão", 1), 
     ("Não, o paciente lida bem com ambientes barulhentos.", 0), 
     ("O paciente às vezes demonstra desconforto em ambientes barulhentos, mas não com frequência.", 0.5)),

    ## Pergunta 10
    ("O paciente tem dificuldades em compreender expressões faciais ou gestos?", 
     ("Sim, o paciente geralmente não entende expressões faciais e gestos.", 1), 
     ("Não, o paciente entende bem as expressões e gestos.", 0), 
     ("O paciente tem dificuldades ocasionais, mas entende a maioria das expressões e gestos.", 0.5)),
]

respostas = []  # Lista para armazenar as respostas
indice_pergunta = 0  # Índice para rastrear a pergunta atual
pontuacao_total = 0.0 # Variável para armazenar a pontuação total do formulário

# Pontuações inicias dos tópicos
pontuacoes_topicos = {
    "Comunicação": 0,
    "Comportamento": 0,
    "Sensibilidade": 0,
}

# Função para Retornar para a pergunta anterior
def voltar_pergunta():
    global indice_pergunta, pontuacao_total

    # Verifica se não está na primeira pergunta
    if indice_pergunta > 0:
        # Volta para a pergunta anterior
        indice_pergunta -= 1

        # Obtém a pontuação da resposta anterior
        resposta_anterior = respostas.pop()

        # Reduz a pontuação total
        pontuacao_total -= resposta_anterior

        # Reduz a pontuação do tópico correspondente
        if indice_pergunta < 2:
            pontuacoes_topicos["Comunicação"] -= resposta_anterior
        elif indice_pergunta < 6:
            pontuacoes_topicos["Comportamento"] -= resposta_anterior
        else:
            pontuacoes_topicos["Sensibilidade"] -= resposta_anterior

        # Exibe as novas pontuações no terminal.
        print(f"Comunicação: {pontuacoes_topicos['Comunicação']:.2f}")
        print(f"Comportamento: {pontuacoes_topicos['Comportamento']:.2f}")
        print(f"Sensibilidade: {pontuacoes_topicos['Sensibilidade']:.2f}")
        print("-" * 30)

        # Mostra a pergunta anterior na interface
        mostrar_pergunta()

# Função para exibir a próxima pergunta
def mostrar_pergunta():
    global indice_pergunta

    # Limpa os botões anteriores e redefine a seleção
    resposta_selecionada.set("")

    # Verificação se o índice da pergunta é existente para ativação do formulário
    if indice_pergunta < len(perguntas):
        pergunta, texto_sim, texto_nao, texto_talvez = perguntas[indice_pergunta]
        label_pergunta.config(text=pergunta)

        # Atualização dos textos dos botões conforme o indíce.
        botaoSim.config(text=texto_sim[0], value=texto_sim[1])
        botaoNao.config(text=texto_nao[0], value=texto_nao[1])
        botaoTalvez.config(text=texto_talvez[0], value=texto_talvez[1])

        # Exibe os botões com textos específicos.
        botaoSim.pack(pady=5)
        botaoNao.pack(pady=5)
        botaoTalvez.pack(pady=5)
        botoesEnvio.pack(pady=20)

        # Controla a exibição do botão "Voltar"
        if indice_pergunta > 0:
            botaoVoltar.pack(pady=5) 
        else:
            botaoVoltar.pack_forget() 
    else:
        # Exibe a mensagem de conclusão quando todas as perguntas foram respondidas, excluindo todos os outros botões e oferecendo o diagnóstico.
        exibir_mensagemFinal()

# Função para salvar a resposta e passar para a próxima pergunta
def confirmar_resposta():
    global indice_pergunta, pontuacao_total

    # Verifica se alguma das opções foi selecionada.
    if not resposta_selecionada.get():
        messagebox.showwarning("Aviso", "Cada pergunta é obrigatória.") 
        return 

    # Adiciona a pontuação da resposta selecionada ao total
    pontuacao_resposta = float(resposta_selecionada.get())
    pontuacao_total += pontuacao_resposta

    # Adiciona a pontuação ao tópico correspondente
    if indice_pergunta < 2: 
        pontuacoes_topicos["Comunicação"] += pontuacao_resposta
    elif indice_pergunta < 6: 
        pontuacoes_topicos["Comportamento"] += pontuacao_resposta
    else:
        pontuacoes_topicos["Sensibilidade"] += pontuacao_resposta

    # Adiciona a resposta à lista de respostas.
    respostas.append(pontuacao_resposta)

    # Print na tela sobre as pontuações.
    print(f"Comunicação: {pontuacoes_topicos['Comunicação']:.2f}")
    print(f"Comportamento: {pontuacoes_topicos['Comportamento']:.2f}")
    print(f"Sensibilidade: {pontuacoes_topicos['Sensibilidade']:.2f}")
    print("-" * 30)

    # Se a última pergunta foi respondida, exibe a mensagem final
    if indice_pergunta == len(perguntas) - 1:
        exibir_mensagemFinal()
    else:
        indice_pergunta += 1
        mostrar_pergunta()

# Label para exibir a pergunta atual
label_pergunta = tk.Label(janela, text="", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)
label_pergunta.pack(pady=20)

# Variável para armazenar a resposta selecionada
resposta_selecionada = tk.StringVar()
resposta_selecionada.set("")

# Estilo dos radiobuttons
estilo_radiobutton = ttk.Style()
estilo_radiobutton.configure("TRadiobutton", background=cor_fundo, foreground=cor_fontePrincipal, font=("Helvetica", 12))

# Criação dos botões de resposta
botaoSim = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")
botaoNao = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")
botaoTalvez = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")

# Criando frame para alinhar os botões Confirmar e Voltar lado a lado
botoesEnvio = tk.Frame(janela, bg=cor_fundo)

# Botão de confirmar com o comando que grava a pontuação da resposta para a mensagem final
botaoConfirmar = ttk.Button(botoesEnvio, text="Confirmar", command=confirmar_resposta, width=25)

# Botão de voltar com o comando que retorna a pontuação junto da pergunta no caso do usuário se arrepender da resposta
botaoVoltar = ttk.Button(botoesEnvio, text="Voltar", command=voltar_pergunta, width=25)

# Ativando os botões
botaoConfirmar.pack(side="left", padx=10)
botaoVoltar.pack(side="left", padx=10)

# Exibir a primeira pergunta
mostrar_pergunta()

# Função para exibição da mensagem de conclusão final
def exibir_mensagemFinal():
    label_pergunta.pack_forget()
    instrucoes.pack_forget()
    botaoSim.pack_forget()
    botaoNao.pack_forget()
    botaoTalvez.pack_forget()
    botoesEnvio.pack_forget()

    # Inicializa a variável mensagem com um valor padrão
    mensagem = "Pontuação inválida: Erro encontrado."

    # Condicional de pontuação total
    if pontuacao_total < 5:
        mensagem = "Pontuação baixa: poucas indicações de autismo."
    elif pontuacao_total >= 5 and pontuacao_total <= 7:
        mensagem = "Pontuação média: há sinais que merecem atenção."
    elif pontuacao_total > 7 and pontuacao_total < 10:
        mensagem = "Pontuação alta: recomendamos uma avaliação profissional."
    elif pontuacao_total == 10:
        mensagem = "Pontuação máxima: altos indícios de autismo, consulte um profissional."

    # Exibe o texto de conclusão do formulário.
    conclusao.config(text=mensagem)
    conclusao.pack()

    # Exibe orientações baseadas nas pontuações dos tópicos
    orientacoesComunicacao = tk.Label(janela, text="", font=("Helvetica", 12), bg=cor_fundo, fg=cor_fonteSecundaria)
    orientacoesComportamento = tk.Label(janela, text="", font=("Helvetica", 12), bg=cor_fundo, fg=cor_fonteSecundaria)
    orientacoesSensibilidade = tk.Label(janela, text="", font=("Helvetica", 12), bg=cor_fundo, fg=cor_fonteSecundaria)

    # Orientações para o tópico de Comunicação
    if pontuacoes_topicos["Comunicação"] < 1.0:
        orientacoesComunicacao.config(text="As habilidades de comunicação estão dentro da normalidade.")
    elif pontuacoes_topicos["Comunicação"] >= 1.0:
        orientacoesComunicacao.config(text="Pode ser útil procurar ajuda para melhorar as habilidades de comunicação.")

    # Exibindo mensagem de orientação sobre o tópico de comunicação
    orientacoesComunicacao.pack()

    # Orientações para o tópico de Comportamento
    if pontuacoes_topicos["Comportamento"] == 4.0:
        orientacoesComportamento.config(text="Alto índice de comportamentos repetitivos. Recomenda-se uma avaliação profissional.")
    elif pontuacoes_topicos["Comportamento"] >= 2.0:
        orientacoesComportamento.config(text="Recomenda-se observar e discutir comportamentos com um profissional.")
    elif pontuacoes_topicos["Comportamento"] < 2.0:
        orientacoesComportamento.config(text="Não há sinais preocupantes de comportamentos repetitivos.")

    # Exibindo mensagem de orientação sobre o tópico de comportamento
    orientacoesComportamento.pack()

    # Orientações para o tópico de Sensibilidade
    if pontuacoes_topicos["Sensibilidade"] == 4.0:
        orientacoesSensibilidade.config(text="Alto nível de hipersensibilidade. Pode ser útil buscar estratégias para lidar com isso.")
    elif pontuacoes_topicos["Sensibilidade"] >= 2.0:
        orientacoesSensibilidade.config(text="Pode ser útil buscar estratégias para lidar com a hipersensibilidade.")
    elif pontuacoes_topicos["Sensibilidade"] < 2.0:
        orientacoesSensibilidade.config(text="A sensibilidade parece estar dentro da faixa normal.")

    # Exibindo mensagem de orientação sobre o tópico de Sensibilidade
    orientacoesSensibilidade.pack()

    # Botão Sair para fechar a aplicação
    botaoSair = ttk.Button(janela, text="Concluir", command=janela.quit)
    botaoSair.pack(pady=20)

# Mensagem de conclusão
conclusao = tk.Label(janela, text="Teste concluído! Obrigado por responder.", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)

# Executando a Janela
janela.mainloop()

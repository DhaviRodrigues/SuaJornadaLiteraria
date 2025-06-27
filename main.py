from datetime import datetime

def estimativa_5_anos(livros_por_ano, anos=5):
    """
    Calcula a estimativa de livros lidos nos próximos 5 anos,
    com base na média anual atual.
    """
    return livros_por_ano * anos

def feedback(total_livros):
    """
    Gera feedback personalizado com base no volume de leitura anual.
    """
    if total_livros >= 50:
        return "Uau! Você é um verdadeiro devorador de livros! Continue assim."
    elif total_livros >= 20:
        return "Excelente ritmo de leitura! Você está explorando bastante."
    elif total_livros >= 5:
        return "Bom começo! Que tal tentar aumentar um pouco mais?"
    else:
        return "Parece que você está lendo pouco. Que tal reservar um tempinho a mais para os livros?"

def estimativa_1000_anos(livros_por_ano):
    """
    Estima quantos anos o usuário levaria para ler 1000 livros,
    mantendo o ritmo atual.
    """
    if livros_por_ano > 0:
        return 1000 / livros_por_ano
    else:
        print("Você não leu nenhum livro no último ano.")

def calcular_equivalencia_tempo(total_horas):
    total_minutos_anuais = total_horas * 60

    km_andados = float (total_minutos_anuais / 12)
    filmes_assistidos = float(total_minutos_anuais / 120)
    disciplinas_graduacao = float(total_horas / 60)
    return km_andados, filmes_assistidos, disciplinas_graduacao

def calcular_horas_estudo_anual(horas_semanais):
    """
    Calcula o total de horas dedicadas aos estudos em um ano.
    """
    return horas_semanais * 52

def calcular_horas_lazer_anual(horas_semanais):
    """
    Calcula o total de horas dedicadas à leitura por lazer em um ano.
    """
    return horas_semanais * 52

# --- Coleta de Dados do Usuário ---

def coletar_dados():
    """
    Coleta todas as informações do usuário e retorna um dicionário.
    """
    print("Olá! Vamos coletar alguns dados sobre seus hábitos de leitura.\n")

    nome = input("Qual é o seu nome? ").strip().title()
    idade = int(input("Qual é a sua idade? "))
    livros_digitais = int(input("Quantos livros digitais você leu no último ano? "))
    livros_fisicos = int(input("Quantos livros físicos você leu no último ano? "))
    preferencia_leitura = input("Qual sua preferência de leitura (Digital, como Kindle, ou Físico)? ").strip().title()
    horas_estudo_semanais = float(input("Quantas horas você dedica aos livros de estudo por semana? "))
    horas_lazer_semanais = float(input("Quantas horas você dedica aos livros por lazer na semana? "))
    genero_favorito = input("Qual é o seu gênero literário favorito? ").strip().title()

    return {
        "nome": nome,
        "idade": idade,
        "livros_digitais": livros_digitais,
        "livros_fisicos": livros_fisicos,
        "preferencia_leitura": preferencia_leitura,
        "horas_estudo_semanais": horas_estudo_semanais,
        "horas_lazer_semanais": horas_lazer_semanais,
        "genero_favorito": genero_favorito
    }

dados_usuario = coletar_dados()

print("\n" + "="*50)
print("           RELATÓRIO DE HÁBITOS DE LEITURA")
print("="*50 + "\n")

# 1 - Mensagem Personalizada
print(f"Olá, {dados_usuario['nome']}! É um prazer ter você por aqui.")

# 2 - Estimativa de Leitura
total_livros = dados_usuario['livros_digitais'] + dados_usuario['livros_fisicos']
total_horas = dados_usuario['horas_lazer_semanais'] + dados_usuario['horas_estudo_semanais']
estimativa_5_anos = estimativa_5_anos(total_livros, 5)

print(f"Com base no seu ritmo atual de {total_livros} livros lidos no último ano, estimamos que você leria aproximadamente {estimativa_5_anos:.0f} livros nos próximos 5 anos!")
print(feedback(total_livros))
print(f"Sua preferência é por livros {dados_usuario['preferencia_leitura']}.\n")

# 3 - Cálculo de Estudo por Ano
horas_estudo_anual = calcular_horas_estudo_anual(dados_usuario['horas_estudo_semanais'])
print(f"Você dedica cerca de {horas_estudo_anual:.1f} horas aos estudos com livros por ano. Isso é um ótimo investimento em seu conhecimento!\n")

# 4 - Cálculo de Leituras por Ano (lazer)
horas_lazer_anual = calcular_horas_lazer_anual(dados_usuario['horas_lazer_semanais'])
print(f"Para lazer, você dedica aproximadamente {horas_lazer_anual:.1f} horas por ano aos livros. Isso é excelente para relaxar e se divertir!\n")

# 5 - Funções Criativas de Tendências/Estimativas

# Estimativa de tempo para ler 1000 livros
tempo_para_mil_livros = estimativa_1000_anos(total_livros)
if tempo_para_mil_livros is < 0:
    print("Se você não leu nenhum livro no último ano, o caminho para 1000 livros pode ser longo. Que tal começar com um objetivo pequeno?")
else:
    print(f"Mantendo seu ritmo atual, você levaria cerca de {tempo_para_mil_livros:.1f} anos para ler 1000 livros. Uma meta e tanto!\n")

# Estimativa de quilômetros andados
calcular_equivalencia_tempo(total_horas)



# Sugestão de leitura baseada em gênero
print(f"Como seu gênero favorito é '{dados_usuario['genero_favorito']}', que tal explorar autores novos ou clássicos dentro dessa área para expandir suas leituras?\n")

print("="*50)
print("Obrigado por participar! Continue cultivando o hábito da leitura!")
print("="*50)
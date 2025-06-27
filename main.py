from datetime import datetime
import time

# Função para estimar a leitura em um período de 5 anos
def estimativa_5_anos(livros_por_ano, anos=5):
    """
    Calcula a estimativa de livros lidos nos próximos 5 anos,
    com base na média anual atual.
    """
    return livros_por_ano * anos

# Função para fornecer feedback com base no total de livros lidos
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

# Função para estimar o tempo para ler 1000 livros
def estimativa_1000_anos(livros_por_ano):
    """
    Estima quantos anos o usuário levaria para ler 1000 livros,
    mantendo o ritmo atual.
    """
    if livros_por_ano > 0:
        return 1000 / livros_por_ano
    else:
        # Mensagem exibida se o usuário não leu nenhum livro
        print("Você não leu nenhum livro no último ano.")

# Função para calcular equivalências de tempo de leitura em outras atividades
def calcular_equivalencia_tempo(total_horas_anuais):
    total_minutos_anuais = total_horas_anuais * 60

    km_andados = float (total_minutos_anuais / 12)
    filmes_assistidos = float(total_minutos_anuais / 120)
    disciplinas_graduacao = float(total_horas_anuais / 60)

    return km_andados, filmes_assistidos, disciplinas_graduacao

# Função para calcular as horas de estudo anuais
def calcular_horas_estudo_anual(horas_semanais):
    """
    Calcula o total de horas dedicadas aos estudos em um ano.
    """
    return horas_semanais * 52

# Função para calcular as horas de lazer anuais
def calcular_horas_lazer_anual(horas_semanais):
    """
    Calcula o total de horas dedicadas à leitura por lazer em um ano.
    """
    return horas_semanais * 52

# Função para coletar todas as informações do usuário com validações
def coletar_dados():
    print("="*65)
    print("Olá! Vamos coletar alguns dados sobre seus hábitos de leitura.")
    print("="*65)

    # Coleta e valida o nome
    while True:
        nome = input("Qual é o seu nome? ").strip().title()
        if nome:
            break
        else:
            print("Nome não pode ser vazio. Por favor, digite seu nome.")

    # Coleta e valida a idade
    while True:
        try:
            idade = int(input("Qual é a sua idade? "))
            if idade > 0:
                break
            else:
                print("Idade deve ser um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    # Coleta e valida a quantidade de livros digitais
    while True:
        try:
            livros_digitais = int(input("Quantos livros digitais você leu no último ano? "))
            if livros_digitais >= 0:
                break
            else:
                print("A quantidade de livros digitais não pode ser negativa.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para livros digitais.")

    # Coleta e valida a quantidade de livros físicos
    while True:
        try:
            livros_fisicos = int(input("Quantos livros físicos você leu no último ano? "))
            if livros_fisicos >= 0:
                break
            else:
                print("A quantidade de livros físicos não pode ser negativa.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para livros físicos.")

    # Coleta e valida a preferência de leitura
    while True:
        preferencia_leitura = input("Qual sua preferência de leitura (Digital, como Kindle, ou Físico)? ").strip().title()
        if preferencia_leitura:
            break
        else:
            print("Preferência de leitura não pode ser vazia. Por favor, digite sua preferência.")

    # Coleta e valida as horas de estudo semanais
    while True:
        try:
            horas_estudo_semanais = float(input("Quantas horas você dedica aos livros de estudo por semana? "))
            if horas_estudo_semanais >= 0:
                break
            else:
                print("As horas de estudo não podem ser negativas.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para as horas de estudo.")

    # Coleta e valida as horas de lazer semanais
    while True:
        try:
            horas_lazer_semanais = float(input("Quantas horas você dedica aos livros por lazer na semana? "))
            if horas_lazer_semanais >= 0:
                break
            else:
                print("As horas de lazer não podem ser negativas.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para as horas de lazer.")

    # Coleta e valida o gênero favorito
    while True:
        genero_favorito = input("Qual é o seu gênero literário favorito? ").strip().title()
        if genero_favorito:
            break
        else:
            print("Gênero favorito não pode ser vazio. Por favor, digite seu gênero.")

    # Retorna todos os dados coletados em um dicionário
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

# Chama a função para coletar os dados do usuário e armazena o resultado
dados_usuario = coletar_dados()

# Imprime um cabeçalho para o relatório
print("\n" + "="*50)
print("           RELATÓRIO DE HÁBITOS DE LEITURA")
print("="*50 + "\n")

# Mensagem de boas-vindas personalizada
print(f"Olá, {dados_usuario['nome']}! É um prazer ter você por aqui.")
# Informação sobre o potencial de leitura baseado na idade

# Calcula o total de livros lidos no último ano
total_livros = dados_usuario['livros_digitais'] + dados_usuario['livros_fisicos']
# Variável total_horas_anuais é declarada aqui mas recalculada mais abaixo, o que pode ser um ponto de otimização
total_horas_anuais = dados_usuario['horas_lazer_semanais'] + dados_usuario['horas_estudo_semanais']
# Calcula a estimativa de leitura para os próximos 5 anos
estimativa_5_anos = estimativa_5_anos(total_livros, 5)

# Exibe a estimativa de leitura e o feedback
print(f"Com base no seu ritmo atual de {total_livros} livros lidos no último ano, estimamos que você leria aproximadamente {estimativa_5_anos:.0f} livros nos próximos 5 anos!")
print(feedback(total_livros))
time.sleep(2)

print(f"Sua preferência é por livros {dados_usuario['preferencia_leitura']}.\n")
time.sleep(2)

# Calcula e exibe as horas anuais dedicadas a estudo
horas_estudo_anual = calcular_horas_estudo_anual(dados_usuario['horas_estudo_semanais'])
print(f"Você dedica cerca de {horas_estudo_anual:.1f} horas aos estudos com livros por ano. Isso é um ótimo investimento em seu conhecimento!\n")
time.sleep(2)

# Calcula e exibe as horas anuais dedicadas a lazer
horas_lazer_anual = calcular_horas_lazer_anual(dados_usuario['horas_lazer_semanais'])
print(f"Para lazer, você dedica aproximadamente {horas_lazer_anual:.1f} horas por ano aos livros. Isso é excelente para relaxar e se divertir!\n")
time.sleep(2)

# Estima e exibe o tempo para ler 1000 livros
tempo_para_mil_livros = estimativa_1000_anos(total_livros)

# A condição 'tempo_para_mil_livros < 0' nunca será verdadeira com a implementação atual da função estimativa_1000_anos
if tempo_para_mil_livros < 0:
    print("Se você não leu nenhum livro no último ano, o caminho para 1000 livros pode ser longo. Que tal começar com um objetivo pequeno?")
else:
    print(f"Mantendo seu ritmo atual, você levaria cerca de {tempo_para_mil_livros:.1f} anos para ler 1000 livros. Uma meta e tanto!\n")
time.sleep(2)

# Recalcula o total de horas anuais dedicadas à leitura (estudo + lazer)
total_horas_anuais = horas_estudo_anual + horas_lazer_anual
# Calcula as equivalências de tempo para outras atividades
km_andados, filmes_assistidos, disciplinas_graduacao = calcular_equivalencia_tempo(total_horas_anuais)

# Exibe as equivalências calculadas
# A condição 'total_horas_anuais < 0' nunca será verdadeira devido às validações de entrada e o cálculo
if total_horas_anuais < 0:
    print("Se você não leu nenhum livro no último ano, o que seria equivalente, em horas, a 0 km andados")
else:
    print(f"""Em um ano com {total_horas_anuais:.1f} horas de leitura, você teria, aproximadamente:
           Andado {km_andados:.1f} km
           Visto {filmes_assistidos:.1f} filmes
           Ou cursado {disciplinas_graduacao:.1f} disciplinas de graduação.\n""")
time.sleep(3)

# Sugestão de leitura baseada no gênero favorito
print(f"Como seu gênero favorito é '{dados_usuario['genero_favorito']}', que tal explorar autores novos ou clássicos dentro dessa área para expandir suas leituras?\n")
time.sleep(2)

# Imprime o rodapé final do relatório
print("="*70)
print("Obrigado por participar! Continue cultivando o hábito da leitura!")
print("="*70)
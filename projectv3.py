import requests
from bs4 import BeautifulSoup
import random

# Função para coletar os trending topics do Twitter
def coletar_trending_topics():
    url = "https://trends24.in/brazil/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscar todas as tags <span> com a classe "trend-name"
            trends = soup.find_all('span', class_='trend-name')
            
            # Extrair apenas o texto dentro da tag <a> (ignorando a contagem de tweets)
            trend_names = [trend.find('a').text.strip() for trend in trends][:10]
            
            return trend_names
        else:
            print(f"Erro {response.status_code}: Não foi possível acessar a página")
            return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []

# Função para buscar um versículo aleatório da Bíblia
def buscar_versiculo_aleatorio():
    # Lista de livros da Bíblia em inglês com o número máximo de capítulos
    livros = {
        "Genesis": 50, "Exodus": 40, "Leviticus": 27, "Numbers": 36, "Deuteronomy": 34,
        "Joshua": 24, "Judges": 21, "Ruth": 4, "1 Samuel": 31, "2 Samuel": 24,
        "1 Kings": 22, "2 Kings": 25, "1 Chronicles": 29, "2 Chronicles": 36, "Ezra": 10,
        "Nehemiah": 13, "Esther": 10, "Job": 42, "Psalms": 150, "Proverbs": 31,
        "Ecclesiastes": 12, "Song of Solomon": 8, "Isaiah": 66, "Jeremiah": 52, "Lamentations": 5,
        "Ezekiel": 48, "Daniel": 12, "Hosea": 14, "Joel": 3, "Amos": 9,
        "Obadiah": 1, "Jonah": 4, "Micah": 7, "Nahum": 3, "Habakkuk": 3,
        "Zephaniah": 3, "Haggai": 2, "Zechariah": 14, "Malachi": 4, "Matthew": 28,
        "Mark": 16, "Luke": 24, "John": 21, "Acts": 28, "Romans": 16,
        "1 Corinthians": 16, "2 Corinthians": 13, "Galatians": 6, "Ephesians": 6, "Philippians": 4,
        "Colossians": 4, "1 Thessalonians": 5, "2 Thessalonians": 3, "1 Timothy": 6, "2 Timothy": 4,
        "Titus": 3, "Philemon": 1, "Hebrews": 13, "James": 5, "1 Peter": 5,
        "2 Peter": 3, "1 John": 5, "2 John": 1, "3 John": 1, "Jude": 1,
        "Revelation": 22
    }

    # Escolhe um livro aleatório
    livro = random.choice(list(livros.keys()))
    max_capitulos = livros[livro]

    # Escolhe um capítulo aleatório dentro do limite do livro
    capitulo = random.randint(1, max_capitulos)

    # Monta a URL da API para buscar o capítulo inteiro em português (Almeida)
    versao = "almeida"  # Almeida Revista e Corrigida
    url = f"https://bible-api.com/{livro}+{capitulo}?translation={versao}"

    try:
        # Faz a requisição à API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Converte a resposta para JSON
        dados = response.json()

        # Verifica se há versículos no capítulo
        if "verses" not in dados:
            return "Nenhum versículo encontrado."

        # Escolhe um versículo aleatório dentro do capítulo
        versiculo = random.choice(dados["verses"])
        texto = versiculo["text"]
        referencia = dados["reference"]  # A referência está no nível superior da resposta

        return f"Versículo aleatório:\n{texto}\nReferência: {referencia}"
    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar o versículo: {e}"
    except KeyError as e:
        return f"Erro ao processar a resposta da API: {e}"

# Função principal
def main():
    # Buscar versículo aleatório
    versiculo = buscar_versiculo_aleatorio()
    print(versiculo)  # Exibe o versículo no terminal

    # Coletar trending topics
    print("\nTrending Topics do Twitter:")
    trend_names = coletar_trending_topics()
    for trend in trend_names:
        print(trend)  # Exibe cada trending topic sem numeração

if __name__ == "__main__":
    main()

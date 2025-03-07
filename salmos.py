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

# Função para buscar um versículo aleatório do livro de Salmos
def buscar_versiculo_salmos():
    # Número máximo de capítulos no livro de Salmos
    max_capitulos = 150

    # Escolhe um capítulo aleatório dentro do limite do livro de Salmos
    capitulo = random.randint(1, max_capitulos)

    # Monta a URL da API para buscar o capítulo inteiro em português (Almeida)
    versao = "almeida"  # Almeida Revista e Corrigida
    url = f"https://bible-api.com/Psa+{capitulo}?translation={versao}"

    try:
        # Faz a requisição à API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Converte a resposta para JSON
        dados = response.json()

        # Verifica se há versículos no capítulo
        if "verses" not in dados:
            return "Nenhum versículo encontrado no livro de Salmos."

        # Escolhe um versículo aleatório dentro do capítulo
        versiculo = random.choice(dados["verses"])
        texto = versiculo["text"]
        referencia = dados["reference"]  # A referência está no nível superior da resposta

        return f"Versículo aleatório de Salmos:\n{texto}\nReferência: {referencia}"
    except requests.exceptions.RequestException as e:
        return f"Erro ao buscar o versículo: {e}"
    except KeyError as e:
        return f"Erro ao processar a resposta da API: {e}"

# Função principal
def main():
    # Buscar versículo aleatório de Salmos
    versiculo = buscar_versiculo_salmos()
    print(versiculo)  # Exibe o versículo no terminal

    # Coletar trending topics
    print("\n#paz")
    trend_names = coletar_trending_topics()
    for trend in trend_names:
        print(trend)  # Exibe cada trending topic sem numeração

if __name__ == "__main__":
    main()

import streamlit as st
import requests
from bs4 import BeautifulSoup
import random

# Função para coletar os trending topics do Twitter em português
def coletar_trending_topics_pt():
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
            return [f"Erro {response.status_code}: Não foi possível acessar a página"]
    except Exception as e:
        return [f"Erro inesperado: {e}"]

# Função para coletar os trending topics do Twitter em inglês
def coletar_trending_topics_en():
    url = "https://trends24.in/united-states/"
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
            return [f"Erro {response.status_code}: Não foi possível acessar a página"]
    except Exception as e:
        return [f"Erro inesperado: {e}"]

# Função para buscar um versículo aleatório do livro de Salmos em português
def buscar_versiculo_salmos_pt():
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

# Função para buscar um versículo aleatório do livro de Salmos em inglês
def buscar_versiculo_salmos_en():
    # Número máximo de capítulos no livro de Salmos
    max_capitulos = 150

    # Escolhe um capítulo aleatório dentro do limite do livro de Salmos
    capitulo = random.randint(1, max_capitulos)

    # Monta a URL da API para buscar o capítulo inteiro em inglês (WEB)
    versao = "web"  # World English Bible
    url = f"https://bible-api.com/Psalms+{capitulo}?translation={versao}"

    try:
        # Faz a requisição à API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Converte a resposta para JSON
        dados = response.json()

        # Verifica se há versículos no capítulo
        if "verses" not in dados:
            return "No verse found in Psalms."

        # Escolhe um versículo aleatório dentro do capítulo
        versiculo = random.choice(dados["verses"])
        texto = versiculo["text"]
        referencia = dados["reference"]  # A referência está no nível superior da resposta

        return f"Random Psalms Verse:\n{texto}\nReference: {referencia}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching verse: {e}"
    except KeyError as e:
        return f"Error processing API response: {e}"

# Interface do aplicativo no Streamlit
def main():
    st.title("Aplicativo de Versículos e Trending Topics")

    # Botões para português
    if st.button("Buscar Versículo de Salmos (PT)"):
        versiculo = buscar_versiculo_salmos_pt()
        st.text_area("Resultado em Português", versiculo, height=150)

    if st.button("Buscar Trending Topics (PT)"):
        trending = coletar_trending_topics_pt()
        st.text_area("Resultado em Português", "\n".join(trending), height=150)

    # Botões para inglês
    if st.button("Search Psalms Verse (EN)"):
        versiculo = buscar_versiculo_salmos_en()
        st.text_area("Resultado em Inglês", versiculo, height=150)

    if st.button("Search Trending Topics (EN)"):
        trending = coletar_trending_topics_en()
        st.text_area("Resultado em Inglês", "\n".join(trending), height=150)

if __name__ == '__main__':
    main()

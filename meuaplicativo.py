from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
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

# Interface do aplicativo
class MyApp(App):
    def build(self):
        # Layout principal (FloatLayout para posicionamento livre)
        layout = FloatLayout()

        # Botões para português
        btn_versiculo_pt = Button(
            text='Buscar Versículo de Salmos',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.85},
            background_color=(0, 0.7, 0, 1)  # Cor verde
        )
        btn_versiculo_pt.bind(on_press=self.mostrar_versiculo_pt)

        btn_trending_pt = Button(
            text='Buscar Trending Topics',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.75},
            background_color=(0, 0.7, 0, 1)  # Cor verde
        )
        btn_trending_pt.bind(on_press=self.mostrar_trending_pt)

        # Botões para inglês
        btn_versiculo_en = Button(
            text='Search Psalms Verse',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.65},
            background_color=(0, 0.7, 0, 1)  # Cor verde
        )
        btn_versiculo_en.bind(on_press=self.mostrar_versiculo_en)

        btn_trending_en = Button(
            text='Search Trending Topics',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.55},
            background_color=(0, 0.7, 0, 1)  # Cor verde
        )
        btn_trending_en.bind(on_press=self.mostrar_trending_en)

        # Texto explicativo para a caixa de saída em português
        label_pt = Label(
            text="Resultados em Português:",
            size_hint=(0.6, 0.05),
            pos_hint={'x': 0.35, 'y': 0.90},
            color=(1, 1, 1, 1)  # Cor branca
        )

        # Caixa de saída para português
        self.resultado_pt = TextInput(
            size_hint=(0.6, 0.3),
            pos_hint={'x': 0.35, 'y': 0.6},
            readonly=True,
            multiline=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )

        # Texto explicativo para a caixa de saída em inglês
        label_en = Label(
            text="Resultados em Inglês:",
            size_hint=(0.6, 0.05),
            pos_hint={'x': 0.35, 'y': 0.5},
            color=(1, 1, 1, 1)  # Cor preta
        )

        # Caixa de saída para inglês
        self.resultado_en = TextInput(
            size_hint=(0.6, 0.3),
            pos_hint={'x': 0.35, 'y': 0.2},
            readonly=True,
            multiline=True,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )

        # Botões para copiar texto
        btn_copiar_pt = Button(
            text='Copiar Texto (PT)',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.45},
            background_color=(0, 0.7, 0, 1)
        )
        btn_copiar_pt.bind(on_press=lambda instance: self.copiar_texto(self.resultado_pt.text))

        btn_copiar_en = Button(
            text='Copy Text (EN)',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.05, 'y': 0.35},
            background_color=(0, 0.7, 0, 1)
        )
        btn_copiar_en.bind(on_press=lambda instance: self.copiar_texto(self.resultado_en.text))

        # Adiciona os widgets ao layout
        layout.add_widget(btn_versiculo_pt)
        layout.add_widget(btn_trending_pt)
        layout.add_widget(btn_versiculo_en)
        layout.add_widget(btn_trending_en)
        layout.add_widget(label_pt)
        layout.add_widget(self.resultado_pt)
        layout.add_widget(label_en)
        layout.add_widget(self.resultado_en)
        layout.add_widget(btn_copiar_pt)
        layout.add_widget(btn_copiar_en)

        return layout

    # Funções para exibir resultados em português
    def mostrar_versiculo_pt(self, instance):
        versiculo = buscar_versiculo_salmos_pt()
        self.resultado_pt.text = versiculo

    def mostrar_trending_pt(self, instance):
        trending = coletar_trending_topics_pt()
        self.resultado_pt.text = '\n'.join(trending)

    # Funções para exibir resultados em inglês
    def mostrar_versiculo_en(self, instance):
        versiculo = buscar_versiculo_salmos_en()
        self.resultado_en.text = versiculo

    def mostrar_trending_en(self, instance):
        trending = coletar_trending_topics_en()
        self.resultado_en.text = '\n'.join(trending)

    # Função para copiar o texto
    def copiar_texto(self, texto):
        if texto.strip():
            from kivy.core.clipboard import Clipboard
            Clipboard.copy(texto)
            self.mostrar_popup("Texto copiado para a área de transferência!")
        else:
            self.mostrar_popup("Nada para copiar.")

    # Função para exibir um popup de mensagem
    def mostrar_popup(self, mensagem):
        popup = Popup(
            title='Aviso',
            content=Label(text=mensagem),
            size_hint=(0.6, 0.3)
        )
        popup.open()

# Executa o aplicativo
if __name__ == '__main__':
    MyApp().run()

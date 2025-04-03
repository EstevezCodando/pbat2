import asyncio
import aiohttp
import certifi
import ssl
import time
import matplotlib.pyplot as plt
import csv

# Criar contexto SSL a partir dos certificados da biblioteca certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Lista de 32 URLs relacionadas à globalização
urls = [
    "https://www.bbc.com/news/world-47080580",  # Notícias sobre globalização
    "https://www.weforum.org/agenda/2020/01/the-globalization-of-business/",  # Fórum Econômico Mundial sobre globalização de negócios
    "https://www.cnbc.com/2020/01/21/how-globalization-has-shape-the-world-economy-in-the-past-50-years.html",  # Artigo sobre como a globalização moldou a economia
    "https://www.imf.org/en/Topics/Globalization",  # FMI sobre globalização
    "https://www.theguardian.com/global-development/2020/feb/28/what-is-globalisation",  # Guardian explicando o conceito de globalização
    "https://www.brookings.edu/research/the-impacts-of-globalization-on-the-global-economy/",  # Brookings sobre impactos da globalização
    "https://www.reuters.com/article/us-globalization-idUSKCN1VV0W9",  # Reuters sobre globalização
    "https://www.worldbank.org/en/topic/globalization",  # Banco Mundial sobre globalização
    "https://www.forbes.com/sites/forbestechcouncil/2020/02/05/how-globalization-is-driving-the-future-of-business/",  # Forbes sobre o futuro dos negócios e a globalização
    "https://www.un.org/en/global-issues/globalization",  # ONU sobre a globalização
    "https://www.theguardian.com/world/2021/feb/01/how-globalisation-is-affecting-our-lives",  # Como a globalização afeta nossas vidas
    "https://www.nytimes.com/2020/03/24/opinion/globalization-economy-coronavirus.html",  # Efeitos do coronavírus na globalização
    "https://www.bbc.com/news/uk-48857808",  # Como o Brexit impacta a globalização
    "https://www.weforum.org/agenda/2020/12/a-new-era-of-globalisation-why-things-will-be-different-after-covid-19/",  # A nova era da globalização pós-COVID-19
    "https://www.npr.org/2020/07/01/884201037/how-globalization-is-being-reshaped-by-the-pandemic",  # Como a pandemia está remodelando a globalização
    "https://www.pwc.com/gx/en/issues/globalization.html",  # PwC sobre globalização
    "https://www.economist.com/special-report/2020/01/18/the-death-of-globalisation",  # Economist sobre a morte da globalização
    "https://www.foreignaffairs.com/articles/2020-05-12/future-globalization",  # The future of globalization
    "https://www.oxfam.org/en/what-we-do/issues/globalization",  # Oxfam sobre a globalização
    "https://www.ft.com/content/f1a76c5a-3837-11ea-a6d3-9a26f8c3f3e7",  # Financial Times sobre a globalização
    "https://www.brookings.edu/education/the-globalization-of-education/",  # Brookings sobre a globalização da educação
    "https://www.un.org/development/desa/dpad/publication/world-economic-situation-and-prospects-2020/",  # Desafios econômicos da globalização
    "https://www.oecd.org/globalization/",  # OECD sobre globalização
    "https://www.npr.org/2020/04/28/849436634/what-will-the-future-of-globalization-look-like",  # NPR sobre o futuro da globalização
    "https://www.hbr.org/2020/06/how-globalization-is-shaping-innovation",  # Harvard Business Review sobre inovação e globalização
    "https://www.bbc.com/news/uk-politics-48046851",  # Como a globalização afeta a política
    "https://www.huffpost.com/entry/the-real-reason-why-globalization-is-becoming-unpopular_b_5ecfdadac5b6a21112fc0e04",  # Huffington Post sobre a popularidade da globalização
    "https://www.wsj.com/articles/what-is-globalization-11582611496",  # Wall Street Journal sobre o que é globalização
    "https://www.imf.org/en/Blogs/Articles/2020/09/23/where-are-we-in-the-globalization-debate",  # IMF sobre o debate da globalização
    "https://www.cnbc.com/2021/07/12/why-globalization-has-fueled-inequality-and-what-to-do-about-it.html",  # CNBC sobre a globalização e desigualdade
]

# Função assíncrona para baixar o conteúdo de uma URL
async def download_url(session, url):
    async with session.get(url, ssl=ssl_context) as response:
        return await response.read()

# Função principal que faz o download de múltiplas URLs de forma assíncrona
async def download_urls_concurrently(urls, num_threads):
    connector = aiohttp.TCPConnector(limit_per_host=10)  # Limitar as conexões por host
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(num_threads):
            url = urls[i % len(urls)]  # Seleciona a URL
            task = asyncio.ensure_future(download_url(session, url))
            tasks.append(task)
        return await asyncio.gather(*tasks)

# Função para medir o tempo de download e gerar o gráfico
def measure_downloads_and_plot():
    times = []
    num_threads_range = [1, 2, 4, 8, 16, 32]  # Testando diferentes números de threads

    # Gravar os resultados em um arquivo CSV
    with open("resultados_download.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Número de Threads", "Tempo (segundos)"])  # Cabeçalho do CSV

        for num_threads in num_threads_range:
            start_time = time.time()
            asyncio.run(download_urls_concurrently(urls, num_threads))
            elapsed_time = time.time() - start_time
            times.append(elapsed_time)
            writer.writerow([num_threads, elapsed_time])  # Gravar os dados no CSV

    # Plotando o gráfico
    plt.plot(num_threads_range, times, marker='o')
    plt.title("Tempo de Download x Número de Threads")
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo (segundos)")
    plt.grid(True)
    plt.show()

# Executando a função para medir e gerar o gráfico
measure_downloads_and_plot()

import os
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

# Caminhos de entrada e saída
input_folder = "/home/afect/Faculdade/PB/pbtp2/Ex3"
output_folder = "/home/afect/Faculdade/PB/pbtp2/Ex3_output"

# Certifique-se de que a pasta de saída existe
os.makedirs(output_folder, exist_ok=True)

# Lista de imagens (assumindo que os arquivos são img1, img2, img3, img4 etc.)
image_files = [f for f in os.listdir(input_folder) if f.startswith("img")]

def apply_filter_and_save(input_path, output_path):
    """
    Lê a imagem, aplica um filtro e salva no caminho de saída.
    """
    with Image.open(input_path) as img:
        # Exemplo: aplica um Filtro de Borda
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
        # Salva a imagem resultante
        filtered_img.save(output_path)

async def process_image_async(executor, img_name):
    """
    Função assíncrona que delega o processamento de imagem
    para uma thread usando asyncio.to_thread.
    """
    input_path = os.path.join(input_folder, img_name)
    output_path = os.path.join(output_folder, f"filtered_{img_name}")
    # Executa a função apply_filter_and_save em thread paralela
    await asyncio.to_thread(apply_filter_and_save, input_path, output_path)

async def process_all_images(n_threads):
    """
    Cria um ThreadPoolExecutor com n_threads e processa todas
    as imagens assincronamente.
    """
    # Cria um conjunto de futures para processar cada imagem
    # simultaneamente, limitado a n_threads
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=n_threads) as executor:
        tasks = []
        for img_name in image_files:
            task = asyncio.create_task(process_image_async(executor, img_name))
            tasks.append(task)
        # Aguarda todas as tasks finalizarem
        await asyncio.gather(*tasks)

def measure_time_for_threads(thread_values):
    """
    Para cada valor de thread em thread_values, mede o tempo de processamento
    de todas as imagens e retorna uma lista de tempos.
    """
    results = []
    for n in thread_values:
        start = time.time()
        asyncio.run(process_all_images(n))
        end = time.time()
        elapsed = end - start
        print(f"Threads = {n}, Tempo = {elapsed:.4f} s")
        results.append(elapsed)
    return results

def main():
    # Defina aqui os valores de threads que deseja testar
    thread_values = [1, 2, 4, 8]
    
    # Mede o tempo de execução para cada quantidade de threads
    times = measure_time_for_threads(thread_values)
    
    # Plotar o gráfico Threads x Tempo
    plt.figure()
    plt.plot(thread_values, times, marker='o')
    plt.title("Processamento de Imagens Assíncrono (Threads x Tempo)")
    plt.xlabel("Número de Threads")
    plt.ylabel("Tempo (s)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

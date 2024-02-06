import requests
from multiprocessing import Pool


def fetch_page(page_number):
    url = f"https://pokeapi.co/api/v2/pokemon/?offset={(page_number - 1) * 20}&limit=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for result in data['results:']:
            print(result['name'], result['url'])
    else:
        print(f"Erro na pagina {page_number}: {response.status_code}")


num_pages = 10


with Pool() as pool:
    pool.map(fetch_page, range(1, num_pages + 1))

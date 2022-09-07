from bs4 import BeautifulSoup
import requests
from datetime import datetime
import json

URL = "https://www.anbima.com.br/informacoes/ima/arqs/ima_completo.xml"


def find_attributes(url):
    data = requests.get(url).content
    soup = BeautifulSoup(data, 'xml')

    all_items = soup.find('FAMILIA', INDICE="IMA-B 5")

    date = str(all_items.find('TOTAIS').get('DT_REF'))
    date_formatted = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
    quote = float(all_items.find('TOTAL').get('T_Num_Indice').replace(',', '.'))

    result = {
        "quote": quote,
        "date": date_formatted
    }

    return json.dumps(result, indent=2)


json_object = find_attributes(URL)
print(json_object)

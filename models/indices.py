import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import jsonify

# base URL for the web-scrapping
URL = "https://www.anbima.com.br/informacoes/ima/arqs/ima_completo.xml"


# Creating helper function to perform the web-scrapping
def find_attributes(url):

    # reading url
    data = requests.get(url).content

    # Initializing soup variable for parsing through the target tags
    soup = BeautifulSoup(data, 'xml')

    all_items = soup.find('FAMILIA', INDICE="IMA-B 5")

    # getting the value of the IMA-B 5 date and converting it to the desired format
    date_raw = str(all_items.find('TOTAIS').get('DT_REF'))
    date = datetime.strptime(date_raw, "%d/%m/%Y").strftime("%Y-%m-%d")

    # getting the value of the IMA-B 5 index and converting it to the desired format
    quote = float(all_items.find('TOTAL').get('T_Num_Indice').replace(',', '.'))

    # adding extracted values to the dictionary list
    result = [
        {
            "quote": quote,
            "date": date
        }
    ]
    return jsonify(result)


# function to communicate with the API
def get_index():
    json_object = find_attributes(URL)
    return json_object


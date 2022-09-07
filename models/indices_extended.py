import requests
from datetime import datetime
from bs4 import BeautifulSoup
from flask import jsonify

# base URL for the web-scrapping
URL = "https://www.anbima.com.br/informacoes/ima/arqs/ima_completo.xml"

# list of the desired indices
index_list = ['IRF-M 1', 'IRF-M 1+', 'IRF-M', 'IMA-B 5', 'IMA-B 5+', 'IMA-B', 'IMA-S', 'IMA-GERAL-EX-C',
              'IMA-GERAL']


# Creating helper function to perform the web-scrapping
def find_attributes(url):
    # reading url
    data = requests.get(url).content

    # Initializing soup variable for parsing through the target tags
    soup = BeautifulSoup(data, 'xml')

    daily_indices = []
    for index in index_list:

        # finding the correct tag associated with the target index
        all_items = soup.find('FAMILIA', INDICE=index)

        # getting the value of the IMA-B 5 date and converting it to the desired format
        date_raw = str(all_items.find('TOTAIS').get('DT_REF'))
        date = datetime.strptime(date_raw, "%d/%m/%Y").strftime("%Y-%m-%d")

        # getting the value of the IMA-B 5 index and converting it to the desired format
        quote = float(all_items.find('TOTAL').get('T_Num_Indice').replace(',', '.'))

        # adding variables to a dictionary
        result = {
            index: {
                "quote": quote,
                "date": date
            }
        }

        # adding dictionaries to the final list of dictionaries
        daily_indices.append(result)

    return daily_indices


# function to communicate with the API
def get_index(index_name=None):
    json_object = find_attributes(URL)
    # if index name is matches one of our indices, return only the "quote" and "date" for that specific index name.
    if index_name is not None:
        for row in json_object:
            if list(row.keys())[0] == index_name:
                return jsonify(row[index_name])

        return jsonify({'message': f'Index not found, try one of the following: {index_list}'})

    # if index name is not provided, return general json file with all indices provided by the ANBIMA website.
    return json_object

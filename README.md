## Challenge IMA-B 5

### 1. The challenge

This challenge is part of a data engineering hiring process. The goal was to create an API and a web-scrapper for the ANBIMA 
website, where we should come up with a way to provide both the IMA-B 5 index and its corresponding date through the following 
endpoint and format:

``Endpoint: /api/vi/cota (GET)``
```
[
  {
    "quote": 4955.994716,
    "date": "2022-08-19"
  }
]
```

### 2. Main technologies

- Programming Language: `Python 3.10`
- IDE: `PyCharm 2022.2`
- API Framework: `Flask 2.2.2`
- Web-scrapping: `Requests & bs4`
- API Testing: `Postman`

### 3. How to run this project?

The first and one of the easiest ways to get the results of this project running is to have Python and an IDE, like PyCharm, 
installed on our computer. Secondly, we also need an API platform, like Postman, to test our API outcome. Once those requirements 
are met, we can proceed with the following steps:

#### 1. Create a virtual environment

Open the terminal, making sure to be in the correct path for the intended project and, in turn, type:
```
1. pip install virtualenv
2. virtualenv env
3. source env/bin/activate
```
#### 2. Add all files from this repository to your project folder.

Install the necessary packages from the `requirements.txt` file. This can be performed through the command 
below:

```
1. pip install -r /path/to/requirements.txt
```

#### 3. Run the `run.py` file

The `run.py` file is the main script to initialize our flask API. There the HTTP method `GET` was created through the decorator
`@app.route()`, where both the endpoint and method were specified. Through the `app.run()` the script starts running the
local server which, by default, is usually at `port=5000`. Pay attention to the HTTP address that will appear on the console
after running the `run.py` script, this address will be added along with the endpoint for testing in the next step. In brief, 
we should see a message like this:

```
 * Serving Flask app 'run'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

`run.py` inherits from `indices.py` the function `get_index()`. This function makes use of a helper function to perform
web-scrapping in the ANBIMA website. The comments on the script already explain in detail the steps of this process but,
in general, the script takes advantage of the daily updates to the XML file address in the website to retrieve the IMA-B 5 
index. After parsing the url address through the `requests` library, `BeautifulSoup` was used to traverse the XML tree and 
attain the necessary data. Everything was added to a dictionary list which, in turn, was converted to a `.JSON` format.

#### 4. Open postman and send a `GET` request through the `/api/v1/cota` endpoint

After downloading and loging into Postman, we can send the `GET` request through the steps below:

1) Select `Collections` and create a new collection through the `+` sign
2) Add a `request` and select `GET` from the dropdown 
3) Select `Environments` and create a new environment through the `+` sign
4) Type the entry point of the API instance and name it to a variable such as:
   - `VARIABLE = Server`
   - `TYPE = default`
   - `INITIAL VALUE = localhost:5000`
   - `CURRENT VALUE = localhost:5000`
5) Under the `GET` request, once the environment is created, type: `http://{{server}}/api/v1/cota`
6) Hit `Send`
7) Check the status code returned by the API (we should see 200 OK) along with the output in a `.JSON` format.

Here is the output obtained through this process:

<img width="1439" alt="Screen Shot 2022-09-07 at 10 55 16 PM" src="https://user-images.githubusercontent.com/101138915/189016435-e5154939-61cd-474b-8a4b-b088f1dc6a92.png">

### 4. Challenge Extension

For the purpose of extending the approach aforementioned, two other scripts were created:
`run_extended.py` and `indices_extended.py`. Those two files follow the same logic we already discussed for `run.py` and
`indices.py`, with the addition of a few features. 

#### 1. run_extended.py

For this script two routes were added with the HTTP method of the type `GET`. The first one follows the same endpoint we are already familiarized with: `/api/v1/cota`.
However, through the changes in `indices_extended.py`, if we run our API through this endpoint, we will obtain not only the
IMA-B 5 index from the ANBIMA website, but also all the other ones, namely:

```
index_list = ['IRF-M 1', 'IRF-M 1+', 'IRF-M', 'IMA-B 5', 'IMA-B 5+', 'IMA-B', 'IMA-S', 'IMA-GERAL-EX-C',
              'IMA-GERAL']
```

The second route, on that matter, allows us to specify the index we want to retrieve. For instance, after running the 
`run_extended.py` script and sending a `GET` request through the API instance: `http://{{server}}/api/v1/cota/IMA-B 5`,
we are able to attain the same results we achieved in the last session. Yet, the process can be repeated for any index from the
ANBIMA website. If we type an index/endpoint that is not contained in my index_list, we will get an error message suggesting
us the available options.

#### 2. indices_extended.py

This script takes an index list for the available indices from the ANBIMA website. Following the same approach presented
for the `indices.py` file, the web-scrapper helper function loops through every index, adds the data to a list of dictionaries,
and returns us a `.JSON` file with the results. The function `get_index()`, now verifies if an index name was specified,
if true and this name matches one of the indices in the list, the function returns only the "quote" and "date" for that 
specific index name. If the index name is not provided, a general .JSON file with all indices provided by the ANBIMA website
is returned, just as already explained.

Here is the outcome for the first route:

<img width="1440" alt="Screen Shot 2022-09-07 at 11 35 27 PM" src="https://user-images.githubusercontent.com/101138915/189021376-2b394112-b7fc-4cbc-9337-4df7fdf8f755.png">

Here are examples of the outputs for the second route:

1) IMA-B 5:

<img width="1431" alt="Screen Shot 2022-09-07 at 11 36 47 PM" src="https://user-images.githubusercontent.com/101138915/189021630-f5be1b57-bde2-4418-8cba-fd59ef432e61.png">

2) IMA-GERAL:

<img width="1435" alt="Screen Shot 2022-09-07 at 11 37 17 PM" src="https://user-images.githubusercontent.com/101138915/189021740-8743c347-924c-4e63-81f6-9250c9bfc06e.png">

3) IMA-GERA (TYPO):

<img width="1437" alt="Screen Shot 2022-09-07 at 11 38 12 PM" src="https://user-images.githubusercontent.com/101138915/189021818-9b6a48b8-8cf6-461a-9c6f-e5159bb1f789.png">


### 5. Greetings

Thank you for your time to review this entire project!
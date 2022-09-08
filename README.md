## Challenge IMA-B 5

### 1. The challenge

This challenge is part of a data engineering hiring process. The goal was to create an API and a web-scrapper for the 
ANBIMA website, where we should come up with a way to provide both the index and its corresponding date through the
following endpoint and format:

``endpoint: api/vi/cota (GET)``
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
- Web-scrapping: `bs4 & requests`
- API Testing: `Postman`

### 3. How to run this project?

The first and one of the easiest ways to get the results of this project running is to have Python and an IDE, like 
PyCharm, installed on our computer. Secondly, we also need an API platform, like Postman, to test our API outcome. Once 
those requirements are met, we can proceed with the following steps:

#### 1. Create a virtual environment
Open the terminal, making sure to be in the correct path for the intended project and,
in turn, type:
```
1. pip install virtualenv
2. virtualenv env
3. source env/bin/activate
```
#### 2. Add all files from this repository to your project folder.

Once step 2 is done, install the necessary packages from the `requirements.txt` file. This can be performed through the 
command below:

```
pip install -r /path/to/requirements.txt
```

#### 3. Run the `run.py` file

#### 4. Open postman and send a `GET` request through the `api/v1/cota` endpoint

### 5. Challenge Extension





from flask import Flask
from models import indices_extended

app = Flask(__name__)


# route decorator to get all indices values provided by the ANBIMA website
@app.route('/api/v1/cota', methods=['GET'])
def get_all_indices():
    result = indices_extended.get_index()
    return result


# route decorator to get a specified index value from a specific index name from the ANBIMA website
@app.route('/api/v1/cota/<string:index_name>', methods=['GET'])
def get_by_index(index_name):
    result = indices_extended.get_index(index_name)
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)

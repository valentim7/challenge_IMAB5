from flask import Flask
from markupsafe import escape
from models import indices
app = Flask(__name__)


@app.route('/api/v1/cota/<index>', methods=['GET'])
def index_do_dia(index):
    result = indices.get_index(index)
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)

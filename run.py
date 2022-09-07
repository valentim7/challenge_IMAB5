from flask import Flask
from models import indices

app = Flask(__name__)


@app.route('/api/v1/cota', methods=['GET'])
def get_daily_ima_b5():
    result = indices.get_index()
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5000)

import csv 
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")

sectors = []
with open('interactions.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        sector = {
            'sector_name': line[1],
            'items': []
        }
        if sector not in sectors:
            sectors.append(sector)

with open('interactions.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        for sector in sectors:
            if line[1] == sector['sector_name']:
                sector_item = {
                    'sector_id': line[0],
                    'sector_name': line[1],
                    'sector_date': line[2]
                }
                sector['items'].append(sector_item)
    

@app.route('/interactions/api', methods=['GET'])
def output_interactions():
    return jsonify(sectors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=os.getenv("DEBUG"))


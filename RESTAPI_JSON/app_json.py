from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)
app.config["DEBUG"] = True

# buka file JSON
file_json = open("mahasiswa.json")

# prsing data JSON
data = json.loads(file_json.read())


# cetak isi data JSON
@app.route('/', methods=['GET'])
def index():
    for dtmhs in data['mahasiswa']:
        print(f"Nama: {dtmhs['nama']}")
        print("Social Media:")
        print(f"- Facebook: {dtmhs['social_media']['faceboook']}")
        print(f"- Twitter: {dtmhs['social_media']['twitter']}")
        print(f"- Instagram: {dtmhs['social_media']['instagram']}")

        return make_response(json({'Biodata' : data}), 200)
    
app.run()
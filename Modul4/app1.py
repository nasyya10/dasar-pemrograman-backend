from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"]=True
@app.route("/", methods=["GET", "POST","PUT","DELETE"])
def karyawan():
    try:
        if request.method == "GET":
            data =[{
                "nama" :'pasya',
                "pekerjaan" : 'web engieer',
                'usia' : "19",
            }]
        elif request.method == "POST":
            data =[{
                "nama" :'pasya',
                "pekerjaan" : 'web engieer',
                'usia' : "19",
            }]
        elif request.method == "PUT":
            data =[{
                "nama" :'pasya',
                "pekerjaan" : 'web engieer',
                'usia' : "19",
            }]
        else:
            data =[{
                "nama" :'pasya',
                "pekerjaan" : 'web engieer',
                'usia' : "19",
            }]
    except Exception as e:
        return make_response(jsonify({"error":str(e)}),400)
    return make_response(jsonify({'data':data}),200)
app.run()
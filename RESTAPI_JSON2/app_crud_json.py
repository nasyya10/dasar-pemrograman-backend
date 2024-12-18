from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
app.config["DEBUG"] = True

# Route untuk menampilkan semua klien
@app.route("/")
def clients():
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    return render_template("clients.html", clients=all_clients)

# Route untuk menambahkan klien baru
@app.route("/clients/add", methods=['GET', 'POST'])
def create():
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    # Cari ID berikutnya
    next_id = 1
    if len(all_clients) > 0:
        next_id = all_clients[-1]["id"] + 1

    if request.method == 'POST':
        client_name = request.form["client_name"]

        if client_name == "":
            return "Name is required"

        # Tambahkan data klien
        all_clients.append(
            {
                "id": next_id,
                "name": client_name  # Perbaikan typo dari 'cient_name' ke 'client_name'
            }
        )

        # Simpan kembali ke file JSON
        with open("data/clients.json", "w") as f:
            json.dump(all_clients, f)

        return redirect("/")

    return render_template("add.html")

# Route untuk melihat detail klien berdasarkan ID
@app.route("/clients/<id>")
def client(id):
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    # Cari klien berdasarkan ID
    client_by_id = list(filter(lambda x: (x["id"] == int(id)), all_clients))
    if client_by_id:
        client_by_id = client_by_id[0]
    else:
        return "Client not found", 404

    return render_template("client.html", client=client_by_id)  # Perbaikan typo di nama file template

# Route untuk mengedit klien
@app.route("/clients/edit/<id>", methods=['GET', 'POST'])
def client_edit(id):
    with open("data/clients.json", "r") as f:
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    # Cari klien berdasarkan ID
    client_by_id = list(filter(lambda x: (x["id"] == int(id)), all_clients))
    if not client_by_id:
        return "Client not found", 404

    client_by_id = client_by_id[0]
    client_index = all_clients.index(client_by_id)

    if request.method == 'POST':
        client_name = request.form["client_name"]
        all_clients[client_index] = {"id": client_by_id["id"], "name": client_name}

        # Simpan perubahan ke file JSON
        with open("data/clients.json", "w") as f:
            json.dump(all_clients, f)

        return redirect('/')

    return render_template("edit.html", client_id=id, client=client_by_id)

# Route untuk menghapus klien
@app.route("/clients/delete")
def client_delete():
    with open("data/clients.json", "r") as f:  # Perbaikan path file
        clients_str = f.read()
    all_clients = json.loads(clients_str)

    # Ambil ID klien dari query string
    client_id = request.args.get("id")
    client_by_id = list(filter(lambda x: (x["id"] == int(client_id)), all_clients))
    if not client_by_id:
        return "Client not found", 404

    # Hapus klien dari list
    client_by_id = client_by_id[0]
    client_index = all_clients.index(client_by_id)
    del all_clients[client_index]

    # Simpan perubahan ke file JSON
    with open("data/clients.json", "w") as f:
        json.dump(all_clients, f)

    return redirect("/")

# Jalankan aplikasi
if __name__ == "__main__":
    app.run()

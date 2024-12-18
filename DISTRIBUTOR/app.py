from flask import Flask, render_template, request, redirect, url_for
import pymysql

application = Flask(__name__)

conn = cursor = None

def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", password="pasya", database="stok")
    cursor = conn.cursor()

def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@application.route('/')
def index():
    openDb()
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()
    data = []
    for container in results:
        data.append(container)
    closeDb()
    return render_template('index.html', container=data)

@application.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']
        openDb()
        sql = "INSERT INTO barang (kode_barang, nama_barang, harga, jumlah) VALUES (%s, %s, %s, %s)"
        val = (kode, nama, harga, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

@application.route('/edit/<id_barang>', methods=['GET', 'POST'])
def edit(id_barang):
    openDb()
    cursor.execute("SELECT * FROM barang WHERE id_barang=%s", (id_barang,))
    data = cursor.fetchone()
    if data:  # Pastikan data ditemukan
        if request.method == 'POST':
            kode = request.form['kode']
            nama = request.form['nama']
            harga = request.form['harga']
            jumlah = request.form['jumlah']
            sql = "UPDATE barang SET kode_barang=%s, nama_barang=%s, harga=%s, jumlah=%s WHERE id_barang=%s"
            val = (kode, nama, harga, jumlah, id_barang)
            cursor.execute(sql, val)
            conn.commit()
            closeDb()
            return redirect(url_for('index'))
        else:
            closeDb()
            return render_template('edit.html', row=data)  # Kirim 'row' ke template
    else:
        closeDb()
        return "Data tidak ditemukan", 404


@application.route('/hapus/<id_barang>', methods=['GET', 'POST'])
def hapus(id_barang):
    openDb()
    cursor.execute("DELETE FROM barang WHERE id_barang=%s", (id_barang,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)
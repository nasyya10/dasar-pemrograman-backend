from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi aplikasi
app.secret_key = 'flash_message'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'icha'
app.config['MYSQL_DB'] = 'crud_dbmysql'

# Inisialisasi MySQL
mysql = MySQL(app)


# Route Index (Menampilkan Data)
@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM siswa")
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', students=data)
    except Exception as e:
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return render_template('index.html', students=[])


# Route untuk Menambahkan Data
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        try:
            nama = request.form['nama']
            alamat = request.form['alamat']
            jurusan = request.form['jurusan']
            nohp = request.form['nohp']

            # Get maximum id from table
            cur = mysql.connection.cursor()
            cur.execute("SELECT MAX(id) FROM siswa")
            max_id = cur.fetchone()[0]

            # Generate new id by incrementing the max id
            if max_id is None:
                new_id = 1
            else:
                new_id = max_id + 1

            cur.execute(
                "INSERT INTO siswa (id, nama, alamat, jurusan, nohp) VALUES (%s, %s, %s, %s, %s)",
                (new_id, nama, alamat, jurusan, nohp),
            )
            mysql.connection.commit()
            cur.close()
            flash('Data Berhasil Ditambahkan', 'success')
        except Exception as e:
            flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return redirect(url_for('index'))


# Route untuk Memperbarui Data
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            id_data = request.form['id']
            nama = request.form['nama']
            alamat = request.form['alamat']
            jurusan = request.form['jurusan']
            nohp = request.form['nohp']

            cur = mysql.connection.cursor()
            cur.execute(
                """
                UPDATE siswa
                SET nama=%s, alamat=%s, jurusan=%s, nohp=%s
                WHERE id=%s
                """,
                (nama, alamat, jurusan, nohp, id_data),
            )
            mysql.connection.commit()
            cur.close()
            flash('Data Berhasil Diupdate', 'success')
        except Exception as e:
            flash(f"Terjadi kesalahan: {str(e)}", 'danger')
        return redirect(url_for('index'))


# Route untuk Menghapus Data
@app.route('/delete/<id_data>', methods=['GET'])
def delete(id_data):
    try:
        # Periksa apakah id_data kosong
        if not id_data:
            flash('ID tidak valid atau kosong!', 'danger')
            return redirect(url_for('index'))

        # Coba konversi id_data ke integer
        id_data = int(id_data)

        # Eksekusi query untuk menghapus data
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM siswa WHERE id=%s", (id_data,))
        mysql.connection.commit()
        cur.close()
        flash('Data Berhasil Dihapus', 'success')
    except ValueError:
        flash('ID harus berupa angka!', 'danger')
    except Exception as e:
        flash(f"Terjadi kesalahan: {str(e)}", 'danger')
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
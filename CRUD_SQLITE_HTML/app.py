from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'stikom123'

# Tambahkan fungsi untuk mengecek koneksi database
def check_db():
    try:
        conn = sqlite3.connect('database_siswa.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_siswa")
        conn.close()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

@app.route("/")
@app.route("/index")
def index():
    if not check_db():
        return "Database error! Pastikan database sudah dibuat."
        
    try:
        conn = sqlite3.connect('database_siswa.db')
        cursor = conn.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute("SELECT * FROM data_siswa")
        data = cursor.fetchall()
        return render_template("index.html", datas=data)
    except Exception as e:
        print(f"Error: {e}")
        return f"Terjadi kesalahan: {e}"
    finally:
        conn.close()

@app.route("/tambah_data", methods=['POST', 'GET'])
def tambah_data():
    if request.method == "POST":
        try:
            nama = request.form['nama']
            email = request.form['email']
            
            conn = sqlite3.connect('database_siswa.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO data_siswa(nama, email) VALUES (?, ?)", 
                         (nama, email))
            conn.commit()
            flash("Data berhasil ditambahkan!", "success")
            
        except sqlite3.IntegrityError:
            flash("Email sudah terdaftar!", "danger")
        except Exception as e:
            flash(f"Terjadi kesalahan: {str(e)}", "danger")
        finally:
            conn.close()
            
        return redirect(url_for("index"))
        
    return render_template("tambah_data.html")

@app.route("/edit_data/<string:id>", methods=['POST', 'GET'])
def edit_data(id):
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        sqliteConnection = sqlite3.connect('database_siswa.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("UPDATE data_siswa SET nama=?, email=? WHERE id=?", (nama, email, id))
        sqliteConnection.commit()
        flash('Data Sudah Di Update', 'success')
        return redirect(url_for("index"))
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM data_siswa WHERE id=?", (id,))
    data = cursor.fetchone()
    return render_template("edit_data.html", datas=data)

@app.route("/hapus_data/<string:id>", methods=["GET"])
def hapus_data(id):
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE FROM data_siswa WHERE id=?", (id,))
    sqliteConnection.commit()
    flash('Data Sudah Terhapus', 'warning')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = 'stikom123'
    app.run(debug=True)
from flask import Flask, request
from model.database import db, db_session
from model.models import ModelMahasiswa, ModelDosen, ModelKelasAmpu, ModelMataKuliah, ModelKelas
from auth.authentication import basic_auth_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/sistem_akademik"
db.init_app(app)


@app.route('/mahasiswa', methods=['POST', 'GET'])
@basic_auth_required
def handle_mahasiswa():  # put application's code here
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            add_mhs = ModelMahasiswa(
                nim=data['nim'],
                nama_mhs=data['nama_mhs'],
                jk_mhs=data['jk_mhs'],
                telp_mhs=data['telp_mhs'],
                email_mhs=data['email_mhs']
            )
            db_session.add(add_mhs)
            db_session.commit()
            return {"Message": f"data {add_mhs.nama_mhs} berhasil ditambahkan"}
        else:
            return {"Error": "Gagal menambahkan"}
    elif request.method == 'GET':
        data = ModelMahasiswa.query.all()
        results = [{
            "NIM": mhs.nim,
            "Nama Mahasiswa": mhs.nama_mhs,
            "Jenis Kelamin": mhs.jk_mhs,
            "Nomer Telpon": mhs.telp_mhs,
            "Email": mhs.email_mhs
        } for mhs in data]

        return {"Count": len(results), "Data": results}


@app.route('/mahasiswa/<nim>', methods=['GET'])
@basic_auth_required
def handle_get_mahasiswa(nim):
    mhs = ModelMahasiswa.query.get_or_404(nim)

    response = {
        "NIM": mhs.nim,
        "Nama Mahasiswa": mhs.nama_mhs,
        "Jenis Kelamin": mhs.jk_mhs,
        "Nomer Telpon": mhs.telp_mhs,
        "Email": mhs.email_mhs
    }
    return {"Message": "Success", "Data": response}


@app.route('/mahasiswa/<nim>', methods=['PUT'])
@basic_auth_required
def handle_edit_mahasiswa(nim):
    mhs = ModelMahasiswa.query.get_or_404(nim)
    data = request.get_json()
    mhs.nama_mhs = data['nama_mhs'],
    mhs.jk_mhs = data['jk_mhs'],
    mhs.telp_mhs = data['telp_mhs'],
    mhs.email_mhs = data['email_mhs']
    db_session.add(mhs)
    db_session.commit()
    return {"Message": f"Data {mhs.nim} berhasil diperbaharui"}


@app.route('/mahasiswa/<nim>', methods=['DELETE'])
@basic_auth_required
def handle_delete_mahasiswa(nim):
    mhs = ModelMahasiswa.query.get_or_404(nim)
    db_session.delete(mhs)
    db_session.commit()
    return {"Message": f"Data {mhs.nim} berhasil dihapus"}


# Matkul
@app.route('/matkul', methods=['GET'])
@basic_auth_required
def handle_getall_matkul():
    getmatkul = ModelMataKuliah.query.all()
    results = [{
        "Kode Mata Kuliah": matkul.kode_mk,
        "Nama Mata Kuliah": matkul.nama_mk,
        "SKS": matkul.sks
    } for matkul in getmatkul]

    return {"Count": len(results), "Data": results}


@app.route('/matkul', methods=['POST'])
@basic_auth_required
def handle_add_matkul():
    if request.is_json:
        data = request.get_json()
        add_matkul = ModelMataKuliah(
            kode_mk=data['kode_mk'],
            nama_mk=data['nama_mk'],
            sks=data['sks']
        )
        db_session.add(add_matkul)
        db_session.commit()
        return {"Message": f"Data mata kuliah {add_matkul.nama_mk} berhasil ditambahkan"}
    else:
        return {"Error": "Gagal menambahkan karena data bukan JSON"}


@app.route('/matkul/<kode_mk>', methods=['PUT'])
@basic_auth_required
def handle_edit_matkul(kode_mk):
    matkul = ModelMataKuliah.query.get_or_404(kode_mk)
    input_matkul = request.get_json()
    matkul.nama_mk = input_matkul['nama_mk'],
    matkul.sks = input_matkul['sks']
    db_session.add(matkul)
    db_session.commit()
    return {"Message": f"Data mata kuliah {matkul.nama_mk} berhasil diperbaharui"}


@app.route('/matkul/<kode_mk>', methods=['DELETE'])
@basic_auth_required
def handle_delete_matkul(kode_mk):
    matkul = ModelMataKuliah.query.get_or_404(kode_mk)
    db_session.delete(matkul)
    db_session.commit()
    return {"Message": f"Data {matkul.nama_mk} berhasil dihapus"}


# @app.route('/test/<nim>', methods=['GET', 'PUT', 'DELETE'])
# @basic_auth_required
# def test_handle(nim):
#     auth = request.authorization
#     if auth.username == 'ANGGA':
#         mhs = ModelMahasiswa.query.get_or_404(nim)
#         response = {
#             "NIM": mhs.nim,
#             "Nama Mahasiswa": mhs.nama_mhs,
#             "Jenis Kelamin": mhs.jk_mhs,
#             "Nomer Telpon": mhs.telp_mhs,
#             "Email": mhs.email_mhs
#         }
#         return {"Message": "Success", "Data": response}
#
#     data = ModelMahasiswa.query.all()
#     results = [{
#         "NIM": mhs.nim,
#         "Nama Mahasiswa": mhs.nama_mhs,
#         "Jenis Kelamin": mhs.jk_mhs,
#         "Nomer Telpon": mhs.telp_mhs,
#         "Email": mhs.email_mhs
#     } for mhs in data]
#     return {"Count": len(results), "Data": results}

if __name__ == '__main__':
    app.run()

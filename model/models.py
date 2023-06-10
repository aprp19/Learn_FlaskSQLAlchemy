from model.database import db


class ModelMahasiswa(db.Model):
    __tablename__ = 'mahasiswa'

    nim = db.Column(db.Text, primary_key=True)
    nama_mhs = db.Column(db.Text)
    jk_mhs = db.Column(db.Text)
    telp_mhs = db.Column(db.Text)
    email_mhs = db.Column(db.Text)


class Auth(db.Model):
    __tablename__ = 'auth'

    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)


class ModelMataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    kode_mk = db.Column(db.Text, primary_key=True)
    nama_mk = db.Column(db.Text)
    sks = db.Column(db.Integer)
    list_kelas = db.relationship('ModelKelas', backref='mata_kuliah', lazy='dynamic')


class ModelKelas(db.Model):
    __tablename__ = 'kelas'

    kode_kelas = db.Column(db.Text, primary_key=True)
    nama_kelas = db.Column(db.Text)
    nip = db.Column(db.Text, db.ForeignKey('dosen.nip'))
    kode_mk = db.Column(db.Text, db.ForeignKey('mata_kuliah.kode_mk'))
    jam = db.Column(db.Text)
    hari = db.Column(db.Text)


class ModelDosen(db.Model):
    __tablename__ = 'dosen'

    nip = db.Column(db.Text, primary_key=True)
    nama_dosen = db.Column(db.Text)
    jk_dosen = db.Column(db.Text)
    telpdosen = db.Column(db.Text)
    emaildosen = db.Column(db.Text)
    list_kelas = db.relationship('ModelKelas', backref='dosen', lazy='dynamic')


class ModelKelasAmpu(db.Model):
    __tablename__ = 'kelas_ampu'

    nim = db.Column(db.Text, db.ForeignKey('mahasiswa.nim'), primary_key=True)
    kode_kelas = db.Column(db.Text, db.ForeignKey('kelas.kode_kelas'), primary_key=True)

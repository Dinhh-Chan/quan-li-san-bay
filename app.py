from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:29092005@localhost/test2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define models
class SanBay(db.Model):
    __tablename__ = 'san_bay'
    MaSanBay = db.Column(db.String(10), primary_key=True)
    TenSanBay = db.Column(db.String(100), nullable=False)
    DiaChiSanBay = db.Column(db.String(255), nullable=False)

class HangHangKhong(db.Model):
    __tablename__ = 'hang_hang_khong'
    MaHangHangKhong = db.Column(db.String(10), primary_key=True)
    TenHangHangKhong = db.Column(db.String(100), nullable=False)
    XuatXu = db.Column(db.String(100), nullable=False)
    ChuSoHuu = db.Column(db.String(100), nullable=False)

class NhanVien(db.Model):
    __tablename__ = 'nhan_vien'
    MaNhanVien = db.Column(db.String(10), primary_key=True)
    ChucVu = db.Column(db.String(100), nullable=False)
    Ten = db.Column(db.String(100), nullable=False)
    SoDienThoai = db.Column(db.String(15), nullable=False)
    MaHangHangKhong = db.Column(db.String(10), db.ForeignKey('hang_hang_khong.MaHangHangKhong'))
    MaSanBay = db.Column(db.String(10), db.ForeignKey('san_bay.MaSanBay'))

class HanhKhach(db.Model):
    __tablename__ = 'hanh_khach'
    MaHanhKhach = db.Column(db.String(10), primary_key=True)
    Ten = db.Column(db.String(100), nullable=False)
    SoDienThoai = db.Column(db.String(15), nullable=False)
    DiaChi = db.Column(db.String(255), nullable=False)

class ChuyenBay(db.Model):
    __tablename__ = 'chuyen_bay'
    MaChuyenBay = db.Column(db.String(10), primary_key=True)
    TenChuyenBay = db.Column(db.String(100), nullable=False)
    MaHangHangKhong = db.Column(db.String(10), db.ForeignKey('hang_hang_khong.MaHangHangKhong'))
    MaHieu = db.Column(db.String(20), nullable=False)
    DiemDen = db.Column(db.String(100), nullable=False)
    LichTrinh = db.Column(db.Text, nullable=False)

class VeMayBay(db.Model):
    __tablename__ = 've_may_bay'
    MaVe = db.Column(db.String(10), primary_key=True)
    MaHanhKhach = db.Column(db.String(10), db.ForeignKey('hanh_khach.MaHanhKhach'))
    MaChuyenBay = db.Column(db.String(10), db.ForeignKey('chuyen_bay.MaChuyenBay'))
    LoaiVe = db.Column(db.String(50), nullable=False)
    GiaVe = db.Column(db.Numeric(10, 2), nullable=False)
    ChoNgoi = db.Column(db.String(10), nullable=False)

class DuongBay(db.Model):
    __tablename__ = 'duong_bay'
    SoHieu = db.Column(db.String(10), primary_key=True)
    ThongTin = db.Column(db.String(255))
    MaSanBay = db.Column(db.String(10))
    MaChuyenBay= db.Column(db.String(10))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template(
        'home.html'
    )
@app.route('/sanbay')
def sanbay():
    sanbay_data = SanBay.query.all()
    return render_template('sanbay.html', sanbay_data=sanbay_data)

@app.route('/hanghangkhong')
def hanghangkhong():
    hanghangkhong_data = HangHangKhong.query.all()
    return render_template('hanghangkhong.html', hanghangkhong_data=hanghangkhong_data)

@app.route('/nhanvien')
def nhanvien():
    nhanvien_data = NhanVien.query.all()
    return render_template('nhanvien.html', nhanvien_data=nhanvien_data)

@app.route('/hanhkhach')
def hanhkhach():
    hanhkhach_data = HanhKhach.query.all()
    return render_template('hanhkhach.html', hanhkhach_data=hanhkhach_data)

@app.route('/chuyenbay')
def chuyenbay():
    chuyenbay_data = ChuyenBay.query.all()
    return render_template('chuyenbay.html', chuyenbay_data=chuyenbay_data)

@app.route('/vemaybay')
def vemaybay():
    vemaybay_data = VeMayBay.query.all()
    return render_template('vemaybay.html', vemaybay_data=vemaybay_data)

@app.route('/duongbay')
def duongbay():
    duongbay_data = DuongBay.query.all()
    return render_template('duongbay.html', duongbay_data=duongbay_data)

# Routes for SanBay
@app.route('/add_sanbay', methods=['POST'])
def add_sanbay():
    data = request.get_json()
    ma_sanbay = data['MaSanBay']
    ten_sanbay = data['TenSanBay']
    diachi_sanbay = data['DiaChiSanBay']
    new_sanbay = SanBay(MaSanBay=ma_sanbay, TenSanBay=ten_sanbay, DiaChiSanBay=diachi_sanbay)
    db.session.add(new_sanbay)
    db.session.commit()
    return jsonify({"status": "success", "data": data})

@app.route('/update_sanbay/<id>', methods=['POST'])
def update_sanbay(id):
    sanbay = SanBay.query.get(id)
    data = request.get_json()
    sanbay.TenSanBay = data['TenSanBay']
    sanbay.DiaChiSanBay = data['DiaChiSanBay']
    db.session.commit()
    return jsonify({"status": "success", "data": data})

@app.route('/delete_sanbay/<id>', methods=['DELETE'])
def delete_sanbay(id):
    sanbay = SanBay.query.get(id)
    db.session.delete(sanbay)
    db.session.commit()
    return jsonify({"status": "success", "id": id})

# Similarly add routes for other models (HangHangKhong, NhanVien, HanhKhach, ChuyenBay, VeMayBay, DuongBay)
@app.route('/add_hanghangkhong', methods = ['POST'])
def add_hanghangkhong():
    data =request.get_json()
    mahanghangkhong =data['MaHangHangKhong']
    tenhang= data['TenHangHangKhong']
    xuatxu = data['XuatXu']
    chusohuu=data['ChuSoHuu']
    new_hanghangkhong = HangHangKhong(MaHangHangKhong = mahanghangkhong, TenHangHangKhong = tenhang, XuatXu = xuatxu, ChuSoHuu =chusohuu)
    db.session.add(new_hanghangkhong)
    db.session.commit()
    return jsonify({"status": "success", "data":data})
@app.route('/update_hanghangkhong/<id>', methods = ['POST'])
def update_hanghangkhong(id):
    hanghangkhong = HangHangKhong.query.get(id)
    data = request.get_json()
    hanghangkhong.TenHangHangKhong = data['TenHangHangKhong']
    hanghangkhong.XuatXu = data['XuatXu']
    hanghangkhong.ChuSoHuu = data['ChuSoHuu']
    db.session.commit()
    return jsonify({"status": "success", "data": data})
@app.route('/delete_hanghangkhong/<id>', methods = ['DELETE'])
def delete_hanghangkhong(id):
    hanghangkhong = HangHangKhong.query.get(id)
    db.session.delete(hanghangkhong)
    db.session.commit()
    return jsonify({"status": "success", "id": id})


if __name__ == '__main__':
    app.run(debug=True)

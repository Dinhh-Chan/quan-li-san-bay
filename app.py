from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
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
class SanBayFrom(FlaskForm):
    MaSanBay = StringField('MaSanBay', validators=[DataRequired()])
    TenSanBay = StringField('TenSanBay', validators=[DataRequired()])
    DiaChiSanBay = StringField('DiaChiSanBay', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HangHangKhong(db.Model):
    __tablename__ = 'hang_hang_khong'
    MaHangHangKhong = db.Column(db.String(10), primary_key=True)
    TenHangHangKhong = db.Column(db.String(100), nullable=False)
    XuatXu = db.Column(db.String(100), nullable=False)
    ChuSoHuu = db.Column(db.String(100), nullable=False)
    
class HangHangKhongForm(FlaskForm):
    MaHangHangKhong = StringField('MaHangHangKhong', validators=[DataRequired()])
    TenHangHangKhong = StringField('TenHangHangKhong', validators=[DataRequired()])
    XuatXu = StringField('XuatXu', validators=[DataRequired()])
    ChuSoHuu = StringField('ChuSoHuu', validators=[DataRequired()])
    submit= SubmitField('Submit')

class NhanVien(db.Model):
    __tablename__ = 'nhan_vien'
    MaNhanVien = db.Column(db.String(10), primary_key=True)
    ChucVu = db.Column(db.String(100), nullable=False)
    Ten = db.Column(db.String(100), nullable=False)
    SoDienThoai = db.Column(db.String(15), nullable=False)
    MaHangHangKhong = db.Column(db.String(10), db.ForeignKey('hang_hang_khong.MaHangHangKhong'))
    MaSanBay = db.Column(db.String(10), db.ForeignKey('san_bay.MaSanBay'))
class NhanVienForm(FlaskForm):
    MaNhanVien = StringField('MaNhanVien', validators=[DataRequired()])
    ChucVu = StringField('ChucVu', validators=[DataRequired()])
    Ten = StringField('Ten', validators=[DataRequired()])
    SoDienThoai = StringField('SoDienThoai', validators=[DataRequired()])
    MaHangHangKhong = StringField('MaHangHangKhong', validators=[DataRequired()])
    MaSanBay = StringField('MaSanBay', validators=[DataRequired()])
    submit = SubmitField('Submit')

class HanhKhach(db.Model):
    __tablename__ = 'hanh_khach'
    MaHanhKhach = db.Column(db.String(10), primary_key=True)
    Ten = db.Column(db.String(100), nullable=False)
    SoDienThoai = db.Column(db.String(15), nullable=False)
    DiaChi = db.Column(db.String(255), nullable=False)
class HanhKhachForm(FlaskForm):
    MaHanhKhach = StringField('MaHanhKhach', validators=[DataRequired()])
    Ten = StringField('Ten', validators=[DataRequired()])
    SoDienThoai = StringField('SoDienThoai', validators=[DataRequired()])
    DiaChi = StringField('DiaChi', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ChuyenBay(db.Model):
    __tablename__ = 'chuyen_bay'
    MaChuyenBay = db.Column(db.String(10), primary_key=True)
    TenChuyenBay = db.Column(db.String(100), nullable=False)
    MaHangHangKhong = db.Column(db.String(10), db.ForeignKey('hang_hang_khong.MaHangHangKhong'))
    MaHieu = db.Column(db.String(20), nullable=False)
    DiemDen = db.Column(db.String(100), nullable=False)
    LichTrinh = db.Column(db.Text, nullable=False)
class ChuyenBayForm(FlaskForm):
    MaChuyenBay = StringField('MaChuyenBay', validators=[DataRequired()])
    TenChuyenBay = StringField('TenChuyenBay', validators=[DataRequired()])
    MaHangHangKhong = StringField('MaHangHangKhong', validators=[DataRequired()])
    MaHieu = StringField('MaHieu', validators=[DataRequired()])
    DiemDen = StringField('DiemDen', validators=[DataRequired()])
    LichTrinh = StringField('LichTrinh', validators=[DataRequired()])
    submit = SubmitField('Submit')

class VeMayBay(db.Model):
    __tablename__ = 've_may_bay'
    MaVe = db.Column(db.String(10), primary_key=True)
    MaHanhKhach = db.Column(db.String(10), db.ForeignKey('hanh_khach.MaHanhKhach'))
    MaChuyenBay = db.Column(db.String(10), db.ForeignKey('chuyen_bay.MaChuyenBay'))
    LoaiVe = db.Column(db.String(50), nullable=False)
    GiaVe = db.Column(db.Numeric(10, 2), nullable=False)
    ChoNgoi = db.Column(db.String(10), nullable=False)
class VeMayBayForm(FlaskForm):
    MaVe = StringField('MaVe', validators=[DataRequired()])
    MaHanhKhach = StringField('MaHanhKhach', validators=[DataRequired()])
    MaChuyenBay = StringField('MaChuyenBay', validators=[DataRequired()])
    LoaiVe = StringField('LoaiVe', validators=[DataRequired()])
    GiaVe = StringField('GiaVe', validators=[DataRequired()])
    ChoNgoi = StringField('ChoNgoi', validators=[DataRequired()])
    submit = SubmitField('Submit')
class DuongBay(db.Model):
    __tablename__ = 'duong_bay'
    SoHieu = db.Column(db.String(10), primary_key=True)
    ThongTin = db.Column(db.String(255))
    MaSanBay = db.Column(db.String(10))
    MaChuyenBay= db.Column(db.String(10))
class DuongBayForm(FlaskForm):
    SoHieu = StringField('Số Hiệu', validators=[DataRequired()])
    ThongTin = StringField('Thông Tin', validators=[DataRequired()])
    MaSanBay = StringField('Mã Sân Bay', validators=[DataRequired()])
    MaChuyenBay = StringField('Mã Chuyến Bay', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template(
        'home.html'
    )
@app.route('/sanbay')
def sanbay():
    return render_template('sanbay.html')

@app.route('/hanghangkhong')
def hanghangkhong():
    return render_template('hanghangkhong.html')

@app.route('/nhanvien')
def nhanvien():
    return render_template('nhanvien.html')


@app.route('/hanhkhach')
def hanhkhach():
    return render_template('hanhkhach.html')

@app.route('/chuyenbay')
def chuyenbay():
    return render_template('chuyenbay.html')

@app.route('/vemaybay')
def vemaybay():
    return render_template('vemaybay.html')

@app.route('/duongbay')
def duongbay():
    return render_template('duongbay.html')

# Routes for SanBay
@app.route('/get_sanbays', methods=['GET'])
def get_sanbays():
    sanbays = SanBay.query.all()
    sanbays_list = [{'MaSanBay': sb.MaSanBay, 'TenSanBay': sb.TenSanBay, 'DiaChiSanBay': sb.DiaChiSanBay} for sb in sanbays]
    return jsonify(sanbays_list)
@app.route('/add_sanbay', methods=['POST'])
def add_sanbay():
    data = request.json
    new_sanbay = SanBay(MaSanBay=data['MaSanBay'], TenSanBay=data['TenSanBay'], DiaChiSanBay=data['DiaChiSanBay'])
    db.session.add(new_sanbay)
    db.session.commit()
    return jsonify({'message': 'San bay added successfully!'})

@app.route('/edit_sanbay/<string:MaSanBay>', methods=['POST'])
def edit_sanbay(MaSanBay):
    data = request.json
    sanbay = SanBay.query.get_or_404(MaSanBay)
    sanbay.TenSanBay = data['TenSanBay']
    sanbay.DiaChiSanBay = data['DiaChiSanBay']
    db.session.commit()
    return jsonify({'message': 'San bay updated successfully!'})
@app.route('/delete_sanbay/<string:MaSanBay>', methods=['POST'])
def delete_sanbay(MaSanBay):
    sanbay = SanBay.query.get_or_404(MaSanBay)
    db.session.delete(sanbay)
    db.session.commit()
    return jsonify({'message': 'San bay deleted successfully!'})

# Similarly add routes for other models (HangHangKhong, NhanVien, HanhKhach, ChuyenBay, VeMayBay, DuongBay)
@app.route('/get_hanghangkhongs', methods=['GET'])
def get_hanghangkhongs():
    hanghangkhongs = HangHangKhong.query.all()
    hanghangkhongs_list = [{'MaHangHangKhong': hhk.MaHangHangKhong, 'TenHangHangKhong': hhk.TenHangHangKhong, 'XuatXu': hhk.XuatXu, 'ChuSoHuu': hhk.ChuSoHuu} for hhk in hanghangkhongs]
    return jsonify(hanghangkhongs_list)
@app.route('/add_hanghangkhong', methods=['POST'])
def add_hanghangkhong():
    data = request.json
    new_hanghangkhong = HangHangKhong(MaHangHangKhong=data['MaHangHangKhong'], TenHangHangKhong=data['TenHangHangKhong'], XuatXu=data['XuatXu'], ChuSoHuu=data['ChuSoHuu'])
    db.session.add(new_hanghangkhong)
    db.session.commit()
    return jsonify({'message': 'Hãng hàng không added successfully!'})
@app.route('/edit_hanghangkhong/<string:MaHangHangKhong>', methods=['POST'])
def edit_hanghangkhong(MaHangHangKhong):
    data = request.json
    hanghangkhong = HangHangKhong.query.get_or_404(MaHangHangKhong)
    hanghangkhong.TenHangHangKhong = data['TenHangHangKhong']
    hanghangkhong.XuatXu = data['XuatXu']
    hanghangkhong.ChuSoHuu = data['ChuSoHuu']
    db.session.commit()
    return jsonify({'message': 'Hãng hàng không updated successfully!'})
@app.route('/delete_hanghangkhong/<string:MaHangHangKhong>', methods=['POST'])
def delete_hanghangkhong(MaHangHangKhong):
    hanghangkhong = HangHangKhong.query.get_or_404(MaHangHangKhong)
    db.session.delete(hanghangkhong)
    db.session.commit()
    return jsonify({'message': 'Hãng hàng không deleted successfully!'})
#Duong bay

@app.route('/get_duongbays', methods=['GET'])
def get_duongbays():
    duongbays = DuongBay.query.all()
    duongbays_list = [
        {
            'SoHieu': db.SoHieu,
            'ThongTin': db.ThongTin,
            'MaSanBay': db.MaSanBay,
            'MaChuyenBay': db.MaChuyenBay
        } for db in duongbays
    ]
    return jsonify(duongbays_list)

@app.route('/add_duongbay', methods=['POST'])
def add_duongbay():
    data = request.json
    new_duongbay = DuongBay(
        SoHieu=data['SoHieu'],
        ThongTin=data['ThongTin'],
        MaSanBay=data['MaSanBay'],
        MaChuyenBay=data['MaChuyenBay']
    )
    db.session.add(new_duongbay)
    db.session.commit()
    return jsonify({'message': 'Đường bay added successfully!'})

@app.route('/edit_duong_bay/<string:so_hieu>', methods=['POST'])
def edit_duong_bay(so_hieu):
    data = request.get_json()
    duong_bay = DuongBay.query.get_or_404(so_hieu)
    duong_bay.SoHieu = data['SoHieu']
    duong_bay.ThongTin = data['ThongTin']
    duong_bay.MaSanBay = data['MaSanBay']
    duong_bay.MaChuyenBay = data['MaChuyenBay']
    db.session.commit()
    return jsonify({'message': 'Duong bay updated!'})

@app.route('/delete_duong_bay/<string:so_hieu>', methods=['POST'])
def delete_duong_bay(so_hieu):
    duong_bay = DuongBay.query.get_or_404(so_hieu)
    db.session.delete(duong_bay)
    db.session.commit()
    return jsonify({'message': 'Duong bay deleted!'})
@app.route('/get_nhanviens', methods=['GET'])
def get_nhanviens():
    nhanviens = NhanVien.query.all()
    nhanviens_list = [
        {
            'MaNhanVien': nv.MaNhanVien,
            'ChucVu': nv.ChucVu,
            'Ten': nv.Ten,
            'SoDienThoai': nv.SoDienThoai,
            'MaHangHangKhong': nv.MaHangHangKhong,
            'MaSanBay': nv.MaSanBay
        } for nv in nhanviens
    ]
    return jsonify(nhanviens_list)
@app.route('/add_nhanvien', methods=['POST'])
def add_nhanvien():
    data = request.json
    new_nhanvien = NhanVien(
        MaNhanVien=data['MaNhanVien'],
        ChucVu=data['ChucVu'],
        Ten=data['Ten'],
        SoDienThoai=data['SoDienThoai'],
        MaHangHangKhong=data['MaHangHangKhong'],
        MaSanBay=data['MaSanBay']
    )
    db.session.add(new_nhanvien)
    db.session.commit()
    return jsonify({'message': 'Nhân viên added successfully!'})
@app.route('/edit_nhanvien/<string:MaNhanVien>', methods=['POST'])
def edit_nhanvien(MaNhanVien):
    data = request.json
    nhanvien = NhanVien.query.get_or_404(MaNhanVien)
    nhanvien.ChucVu = data['ChucVu']
    nhanvien.Ten = data['Ten']
    nhanvien.SoDienThoai = data['SoDienThoai']
    nhanvien.MaHangHangKhong = data['MaHangHangKhong']
    nhanvien.MaSanBay = data['MaSanBay']
    db.session.commit()
    return jsonify({'message': 'Nhân viên updated successfully!'})
@app.route('/delete_nhanvien/<string:MaNhanVien>', methods=['POST'])
def delete_nhanvien(MaNhanVien):
    nhanvien = NhanVien.query.get_or_404(MaNhanVien)
    db.session.delete(nhanvien)
    db.session.commit()
    return jsonify({'message': 'Nhân viên deleted successfully!'})
@app.route('/get_hanhkhachs', methods=['GET'])
def get_hanhkhachs():
    hanhkhachs = HanhKhach.query.all()
    hanhkhachs_list = [
        {
            'MaHanhKhach': hk.MaHanhKhach,
            'Ten': hk.Ten,
            'SoDienThoai': hk.SoDienThoai,
            'DiaChi': hk.DiaChi
        } for hk in hanhkhachs
    ]
    return jsonify(hanhkhachs_list)
@app.route('/add_hanhkhach', methods=['POST'])
def add_hanhkhach():
    data = request.json
    new_hanhkhach = HanhKhach(
        MaHanhKhach=data['MaHanhKhach'],
        Ten=data['Ten'],
        SoDienThoai=data['SoDienThoai'],
        DiaChi=data['DiaChi']
    )
    db.session.add(new_hanhkhach)
    db.session.commit()
    return jsonify({'message': 'Hành khách added successfully!'})
@app.route('/edit_hanhkhach/<string:MaHanhKhach>', methods=['POST'])
def edit_hanhkhach(MaHanhKhach):
    data = request.json
    hanhkhach = HanhKhach.query.get_or_404(MaHanhKhach)
    hanhkhach.Ten = data['Ten']
    hanhkhach.SoDienThoai = data['SoDienThoai']
    hanhkhach.DiaChi = data['DiaChi']
    db.session.commit()
    return jsonify({'message': 'Hành khách updated successfully!'})
@app.route('/delete_hanhkhach/<string:MaHanhKhach>', methods=['POST'])
def delete_hanhkhach(MaHanhKhach):
    hanhkhach = HanhKhach.query.get_or_404(MaHanhKhach)
    db.session.delete(hanhkhach)
    db.session.commit()
    return jsonify({'message': 'Hành khách deleted successfully!'})
@app.route('/get_chuyenbays', methods=['GET'])
def get_chuyenbays():
    chuyenbays = ChuyenBay.query.all()
    chuyenbays_list = [
        {
            'MaChuyenBay': cb.MaChuyenBay,
            'TenChuyenBay': cb.TenChuyenBay,
            'MaHangHangKhong': cb.MaHangHangKhong,
            'MaHieu': cb.MaHieu,
            'DiemDen': cb.DiemDen,
            'LichTrinh': cb.LichTrinh
        } for cb in chuyenbays
    ]
    return jsonify(chuyenbays_list)
@app.route('/add_chuyenbay', methods=['POST'])
def add_chuyenbay():
    data = request.json
    new_chuyenbay = ChuyenBay(
        MaChuyenBay=data['MaChuyenBay'],
        TenChuyenBay=data['TenChuyenBay'],
        MaHangHangKhong=data['MaHangHangKhong'],
        MaHieu=data['MaHieu'],
        DiemDen=data['DiemDen'],
        LichTrinh=data['LichTrinh']
    )
    db.session.add(new_chuyenbay)
    db.session.commit()
    return jsonify({'message': 'Chuyến bay added successfully!'})
@app.route('/edit_chuyenbay/<string:MaChuyenBay>', methods=['POST'])
def edit_chuyenbay(MaChuyenBay):
    data = request.json
    chuyenbay = ChuyenBay.query.get_or_404(MaChuyenBay)
    chuyenbay.TenChuyenBay = data['TenChuyenBay']
    chuyenbay.MaHangHangKhong = data['MaHangHangKhong']
    chuyenbay.MaHieu = data['MaHieu']
    chuyenbay.DiemDen = data['DiemDen']
    chuyenbay.LichTrinh = data['LichTrinh']
    db.session.commit()
    return jsonify({'message': 'Chuyến bay updated successfully!'})
@app.route('/delete_chuyenbay/<string:MaChuyenBay>', methods=['POST'])
def delete_chuyenbay(MaChuyenBay):
    chuyenbay = ChuyenBay.query.get_or_404(MaChuyenBay)
    db.session.delete(chuyenbay)
    db.session.commit()
    return jsonify({'message': 'Chuyến bay deleted successfully!'})
@app.route('/get_vemaybays', methods=['GET'])
def get_vemaybays():
    vemaybays = VeMayBay.query.all()
    vemaybays_list = [
        {
            'MaVe': ve.MaVe,
            'MaHanhKhach': ve.MaHanhKhach,
            'MaChuyenBay': ve.MaChuyenBay,
            'LoaiVe': ve.LoaiVe,
            'GiaVe': str(ve.GiaVe),  # Convert to string for JSON serialization
            'ChoNgoi': ve.ChoNgoi
        } for ve in vemaybays
    ]
    return jsonify(vemaybays_list)
@app.route('/add_vemaybay', methods=['POST'])
def add_vemaybay():
    data = request.json
    new_vemaybay = VeMayBay(
        MaVe=data['MaVe'],
        MaHanhKhach=data['MaHanhKhach'],
        MaChuyenBay=data['MaChuyenBay'],
        LoaiVe=data['LoaiVe'],
        GiaVe=data['GiaVe'],
        ChoNgoi=data['ChoNgoi']
    )
    db.session.add(new_vemaybay)
    db.session.commit()
    return jsonify({'message': 'Vé máy bay added successfully!'})

@app.route('/edit_vemaybay/<string:MaVe>', methods=['POST'])
def edit_vemaybay(MaVe):
    data = request.json
    vemaybay = VeMayBay.query.get_or_404(MaVe)
    vemaybay.MaHanhKhach = data['MaHanhKhach']
    vemaybay.MaChuyenBay = data['MaChuyenBay']
    vemaybay.LoaiVe = data['LoaiVe']
    vemaybay.GiaVe = data['GiaVe']
    vemaybay.ChoNgoi = data['ChoNgoi']
    db.session.commit()
    return jsonify({'message': 'Vé máy bay updated successfully!'})
@app.route('/delete_vemaybay/<string:MaVe>', methods=['POST'])
def delete_vemaybay(MaVe):
    vemaybay = VeMayBay.query.get_or_404(MaVe)
    db.session.delete(vemaybay)
    db.session.commit()
    return jsonify({'message': 'Vé máy bay deleted successfully!'})
@app.route('/execute_sql', methods=['POST'])
def execute_sql():
    sql_query = request.form['sql_query']
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text(sql_query))
            if result.returns_rows:
                rows = result.fetchall()
                column_names = result.keys()
                return jsonify({'status': 'success', 'data': [dict(zip(column_names, row)) for row in rows]})
            else:
                connection.commit()
                return jsonify({'status': 'success', 'data': 'Query executed successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})
if __name__ == '__main__':
    app.run(debug=True)

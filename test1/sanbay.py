from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:29092005@localhost/test2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class DuongBay(db.Model):
    __tablename__ = 'duong_bay'
    SoHieu = db.Column(db.String(10), primary_key=True)
    ThongTin = db.Column(db.String(255))
    MaSanBay = db.Column(db.String(10))
    MaChuyenBay = db.Column(db.String(10))

class DuongBayForm(FlaskForm):
    SoHieu = StringField('Số Hiệu', validators=[DataRequired()])
    ThongTin = StringField('Thông Tin', validators=[DataRequired()])
    MaSanBay = StringField('Mã Sân Bay', validators=[DataRequired()])
    MaChuyenBay = StringField('Mã Chuyến Bay', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    form = DuongBayForm()
    return render_template('index.html', form=form)

@app.route('/get_duong_bays', methods=['GET'])
def get_duong_bays():
    duong_bays = DuongBay.query.all()
    duong_bay_list = [{'SoHieu': db.SoHieu, 'ThongTin': db.ThongTin, 'MaSanBay': db.MaSanBay, 'MaChuyenBay': db.MaChuyenBay} for db in duong_bays]
    return jsonify(duong_bay_list)

@app.route('/add_duong_bay', methods=['POST'])
def add_duong_bay():
    data = request.get_json()
    new_duong_bay = DuongBay(
        SoHieu=data['SoHieu'],
        ThongTin=data['ThongTin'],
        MaSanBay=data['MaSanBay'],
        MaChuyenBay=data['MaChuyenBay']
    )
    db.session.add(new_duong_bay)
    db.session.commit()
    return jsonify({'message': 'New duong bay added!'})

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

if __name__ == '__main__':
    app.run(debug=True)

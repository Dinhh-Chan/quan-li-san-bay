
import app
from app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from app import SanBay, HangHangKhong,NhanVien, HanhKhach , ChuyenBay , VeMayBay ,DuongBay
from datetime import datetime, timedelta

def init_db():
    db.drop_all()
    db.create_all()
    sanbay_data = [
        SanBay(MaSanBay='SBA1', TenSanBay='Noi Bai International', DiaChiSanBay='Hanoi'),
        SanBay(MaSanBay='SBA2', TenSanBay='Tan Son Nhat International', DiaChiSanBay='Ho Chi Minh City'),
        SanBay(MaSanBay='SBA3', TenSanBay='Da Nang International', DiaChiSanBay='Da Nang'),
        SanBay(MaSanBay = 'SBA4', TenSanBay = 'Cam Ranh International', DiaChiSanBay ='Khanh Hoa'),
        SanBay(MaSanBay = 'SBA5',TenSanBay = 'Phu Quoc International', DiaChiSanBay ='Phu Quoc'),
        SanBay(MaSanBay = 'SBA6', TenSanBay =  'Cat Bi International', DiaChiSanBay ='Hai Phong'),
        SanBay(MaSanBay = 'SBA7',TenSanBay = 'Can Tho International', DiaChiSanBay ='Can Tho'),
        SanBay(MaSanBay = 'SBA8', TenSanBay = 'Lien Khuong International', DiaChiSanBay ='Da Lat'),
        SanBay(MaSanBay = 'SBA9',TenSanBay = 'Phu Bai International', DiaChiSanBay ='Hue'),
        SanBay(MaSanBay = 'SBA10', TenSanBay = 'Dong Hoi Airport', DiaChiSanBay ='Quang Binh'),
        SanBay(MaSanBay = 'SBA11', TenSanBay = 'Thanh Hoa Airport', DiaChiSanBay ='Thanh Hoa'),
        SanBay(MaSanBay = 'SBA12',TenSanBay = 'Vinh Airport', DiaChiSanBay ='Nghe An'),
        SanBay(MaSanBay = 'SBA13', TenSanBay = 'Buon Ma Thuot Airport', DiaChiSanBay ='Dak Lak'),
        SanBay(MaSanBay = 'SBA14',TenSanBay = 'Con Dao Airport', DiaChiSanBay ='Ba Ria - Vung Tau'),
        SanBay(MaSanBay = 'SBA15',TenSanBay = 'Rach Gia Airport', DiaChiSanBay ='Kien Giang'),
       
    ]
    hang_hang_khong_data = [
    HangHangKhong(MaHangHangKhong='HHA1', TenHangHangKhong='Vietnam Airlines', XuatXu='Vietnam', ChuSoHuu='Vietnam Government'),
    HangHangKhong(MaHangHangKhong='HHA2', TenHangHangKhong='VietJet Air', XuatXu='Vietnam', ChuSoHuu='Private'),
    HangHangKhong(MaHangHangKhong='HHA3', TenHangHangKhong='Bamboo Airways', XuatXu='Vietnam', ChuSoHuu='FLC Group'),
    HangHangKhong(MaHangHangKhong='HHA4', TenHangHangKhong='Jetstar Pacific Airlines', XuatXu='Vietnam', ChuSoHuu='Vietnam Airlines'),
    HangHangKhong(MaHangHangKhong='HHA5', TenHangHangKhong='Vasco', XuatXu='Vietnam', ChuSoHuu='Vietnam Airlines'),
    HangHangKhong(MaHangHangKhong='HHA6', TenHangHangKhong='Korean Air', XuatXu='South Korea', ChuSoHuu='Hanjin Group'),
    HangHangKhong(MaHangHangKhong='HHA7', TenHangHangKhong='Singapore Airlines', XuatXu='Singapore', ChuSoHuu='Temasek Holdings'),
    HangHangKhong(MaHangHangKhong='HHA8', TenHangHangKhong='AirAsia', XuatXu='Malaysia', ChuSoHuu='Tune Group'),
    HangHangKhong(MaHangHangKhong='HHA9', TenHangHangKhong='Cathay Pacific', XuatXu='Hong Kong', ChuSoHuu='Swire Group'),
    HangHangKhong(MaHangHangKhong='HHA10', TenHangHangKhong='Qatar Airways', XuatXu='Qatar', ChuSoHuu='Government of Qatar'),
    HangHangKhong(MaHangHangKhong='HHA11', TenHangHangKhong='Lufthansa', XuatXu='Germany', ChuSoHuu='Private'),
    HangHangKhong(MaHangHangKhong='HHA12', TenHangHangKhong='Air France', XuatXu='France', ChuSoHuu='Air France-KLM Group'),
    HangHangKhong(MaHangHangKhong='HHA13', TenHangHangKhong='Emirates', XuatXu='UAE', ChuSoHuu='Government of Dubai'),
    HangHangKhong(MaHangHangKhong='HHA14', TenHangHangKhong='Turkish Airlines', XuatXu='Turkey', ChuSoHuu='Government of Turkey'),
    HangHangKhong(MaHangHangKhong='HHA15', TenHangHangKhong='British Airways', XuatXu='United Kingdom', ChuSoHuu='International Airlines Group')
]
    nhan_vien_data = [
    NhanVien(MaNhanVien='NV01', ChucVu='Pilot', Ten='Nguyen Van A', SoDienThoai='0123456789', MaHangHangKhong='HHA1', MaSanBay='SBA1'),
    NhanVien(MaNhanVien='NV02', ChucVu='Flight Attendant', Ten='Tran Thi B', SoDienThoai='0123456790', MaHangHangKhong='HHA1', MaSanBay='SBA1'),
    NhanVien(MaNhanVien='NV03', ChucVu='Security', Ten='Le Van C', SoDienThoai='0123456791', MaHangHangKhong='HHA2', MaSanBay='SBA2'),
    NhanVien(MaNhanVien='NV04', ChucVu='Maintenance', Ten='Pham Thi D', SoDienThoai='0123456792', MaHangHangKhong='HHA2', MaSanBay='SBA2'),
    NhanVien(MaNhanVien='NV05', ChucVu='Pilot', Ten='Hoang Van E', SoDienThoai='0123456793', MaHangHangKhong='HHA3', MaSanBay='SBA3'),
    NhanVien(MaNhanVien='NV06', ChucVu='Flight Attendant', Ten='Nguyen Thi F', SoDienThoai='0123456794', MaHangHangKhong='HHA3', MaSanBay='SBA3'),
    NhanVien(MaNhanVien='NV07', ChucVu='Pilot', Ten='Tran Van G', SoDienThoai='0123456795', MaHangHangKhong='HHA4', MaSanBay='SBA4'),
    NhanVien(MaNhanVien='NV08', ChucVu='Security', Ten='Le Thi H', SoDienThoai='0123456796', MaHangHangKhong='HHA4', MaSanBay='SBA4'),
    NhanVien(MaNhanVien='NV09', ChucVu='Maintenance', Ten='Pham Van I', SoDienThoai='0123456797', MaHangHangKhong='HHA5', MaSanBay='SBA5'),
    NhanVien(MaNhanVien='NV10', ChucVu='Pilot', Ten='Hoang Thi J', SoDienThoai='0123456798', MaHangHangKhong='HHA5', MaSanBay='SBA5'),
    NhanVien(MaNhanVien='NV11', ChucVu='Flight Attendant', Ten='Nguyen Van K', SoDienThoai='0123456799', MaHangHangKhong='HHA6', MaSanBay='SBA6'),
    NhanVien(MaNhanVien='NV12', ChucVu='Security', Ten='Tran Thi L', SoDienThoai='0123456800', MaHangHangKhong='HHA6', MaSanBay='SBA6'),
    NhanVien(MaNhanVien='NV13', ChucVu='Maintenance', Ten='Le Van M', SoDienThoai='0123456801', MaHangHangKhong='HHA7', MaSanBay='SBA7'),
    NhanVien(MaNhanVien='NV14', ChucVu='Pilot', Ten='Pham Thi N', SoDienThoai='0123456802', MaHangHangKhong='HHA7', MaSanBay='SBA7'),
    NhanVien(MaNhanVien='NV15', ChucVu='Flight Attendant', Ten='Hoang Van O', SoDienThoai='0123456803', MaHangHangKhong='HHA8', MaSanBay='SBA8')
]
    hanh_khach_data = [
    HanhKhach(MaHanhKhach='HK01', Ten='Nguyen Van P', SoDienThoai='0987654321', DiaChi='Hanoi'),
    HanhKhach(MaHanhKhach='HK02', Ten='Tran Thi Q', SoDienThoai='0987654322', DiaChi='Ho Chi Minh City'),
    HanhKhach(MaHanhKhach='HK03', Ten='Le Van R', SoDienThoai='0987654323', DiaChi='Da Nang'),
    HanhKhach(MaHanhKhach='HK04', Ten='Pham Thi S', SoDienThoai='0987654324', DiaChi='Khanh Hoa'),
    HanhKhach(MaHanhKhach='HK05', Ten='Hoang Van T', SoDienThoai='0987654325', DiaChi='Phu Quoc'),
    HanhKhach(MaHanhKhach='HK06', Ten='Nguyen Thi U', SoDienThoai='0987654326', DiaChi='Hai Phong'),
    HanhKhach(MaHanhKhach='HK07', Ten='Tran Van V', SoDienThoai='0987654327', DiaChi='Can Tho'),
    HanhKhach(MaHanhKhach='HK08', Ten='Le Thi W', SoDienThoai='0987654328', DiaChi='Da Lat'),
    HanhKhach(MaHanhKhach='HK09', Ten='Pham Van X', SoDienThoai='0987654329', DiaChi='Hue'),
    HanhKhach(MaHanhKhach='HK10', Ten='Hoang Thi Y', SoDienThoai='0987654330', DiaChi='Quang Binh'),
    HanhKhach(MaHanhKhach='HK11', Ten='Nguyen Van Z', SoDienThoai='0987654331', DiaChi='Thanh Hoa'),
    HanhKhach(MaHanhKhach='HK12', Ten='Tran Thi AA', SoDienThoai='0987654332', DiaChi='Nghe An'),
    HanhKhach(MaHanhKhach='HK13', Ten='Le Van BB', SoDienThoai='0987654333', DiaChi='Dak Lak'),
    HanhKhach(MaHanhKhach='HK14', Ten='Pham Thi CC', SoDienThoai='0987654334', DiaChi='Ba Ria - Vung Tau'),
    HanhKhach(MaHanhKhach='HK15', Ten='Hoang Van DD', SoDienThoai='0987654335', DiaChi='Kien Giang')
]
    chuyen_bay_data = [
    ChuyenBay(MaChuyenBay='CB001', TenChuyenBay='VN101', MaHangHangKhong='HHA1', MaHieu='VN101', DiemDen='Da Nang', LichTrinh='09:00 AM - 11:30 AM'),
    ChuyenBay(MaChuyenBay='CB002', TenChuyenBay='VN102', MaHangHangKhong='HHA1', MaHieu='VN102', DiemDen='Ho Chi Minh City', LichTrinh='10:00 AM - 12:30 PM'),
    ChuyenBay(MaChuyenBay='CB003', TenChuyenBay='VN103', MaHangHangKhong='HHA1', MaHieu='VN103', DiemDen='Hai Phong', LichTrinh='11:00 AM - 01:30 PM'),
    ChuyenBay(MaChuyenBay='CB004', TenChuyenBay='VN104', MaHangHangKhong='HHA1', MaHieu='VN104', DiemDen='Can Tho', LichTrinh='12:00 PM - 02:30 PM'),
    ChuyenBay(MaChuyenBay='CB005', TenChuyenBay='VN105', MaHangHangKhong='HHA1', MaHieu='VN105', DiemDen='Da Lat', LichTrinh='01:00 PM - 03:30 PM'),
    ChuyenBay(MaChuyenBay='CB006', TenChuyenBay='VN106', MaHangHangKhong='HHA1', MaHieu='VN106', DiemDen='Hue', LichTrinh='02:00 PM - 04:30 PM'),
    ChuyenBay(MaChuyenBay='CB007', TenChuyenBay='VN107', MaHangHangKhong='HHA1', MaHieu='VN107', DiemDen='Quang Binh', LichTrinh='03:00 PM - 05:30 PM'),
    ChuyenBay(MaChuyenBay='CB008', TenChuyenBay='VN108', MaHangHangKhong='HHA1', MaHieu='VN108', DiemDen='Thanh Hoa', LichTrinh='04:00 PM - 06:30 PM'),
    ChuyenBay(MaChuyenBay='CB009', TenChuyenBay='VN109', MaHangHangKhong='HHA1', MaHieu='VN109', DiemDen='Nghe An', LichTrinh='05:00 PM - 07:30 PM'),
    ChuyenBay(MaChuyenBay='CB010', TenChuyenBay='VN110', MaHangHangKhong='HHA1', MaHieu='VN110', DiemDen='Dak Lak', LichTrinh='06:00 PM - 08:30 PM'),
    ChuyenBay(MaChuyenBay='CB011', TenChuyenBay='VN111', MaHangHangKhong='HHA1', MaHieu='VN111', DiemDen='Ba Ria - Vung Tau', LichTrinh='07:00 PM - 09:30 PM'),
    ChuyenBay(MaChuyenBay='CB012', TenChuyenBay='VN112', MaHangHangKhong='HHA1', MaHieu='VN112', DiemDen='Kien Giang', LichTrinh='08:00 PM - 10:30 PM'),
    ChuyenBay(MaChuyenBay='CB013', TenChuyenBay='VN113', MaHangHangKhong='HHA1', MaHieu='VN113', DiemDen='Phu Quoc', LichTrinh='09:00 PM - 11:30 PM'),
    ChuyenBay(MaChuyenBay='CB014', TenChuyenBay='VN114', MaHangHangKhong='HHA1', MaHieu='VN114', DiemDen='Nha Trang', LichTrinh='10:00 PM - 12:30 AM'),
    ChuyenBay(MaChuyenBay='CB015', TenChuyenBay='VN115', MaHangHangKhong='HHA1', MaHieu='VN115', DiemDen='Vinh', LichTrinh='11:00 PM - 01:30 AM')
]
    ve_may_bay_data = [
    VeMayBay(MaVe='V001', MaHanhKhach='HK01', MaChuyenBay='CB001', LoaiVe='Economy', GiaVe=500000, ChoNgoi='12A'),
    VeMayBay(MaVe='V002', MaHanhKhach='HK02', MaChuyenBay='CB002', LoaiVe='Economy', GiaVe=600000, ChoNgoi='12B'),
    VeMayBay(MaVe='V003', MaHanhKhach='HK03', MaChuyenBay='CB003', LoaiVe='Economy', GiaVe=700000, ChoNgoi='12C'),
    VeMayBay(MaVe='V004', MaHanhKhach='HK04', MaChuyenBay='CB004', LoaiVe='Economy', GiaVe=800000, ChoNgoi='12D'),
    VeMayBay(MaVe='V005', MaHanhKhach='HK05', MaChuyenBay='CB005', LoaiVe='Economy', GiaVe=900000, ChoNgoi='12E'),
    VeMayBay(MaVe='V006', MaHanhKhach='HK06', MaChuyenBay='CB006', LoaiVe='Business', GiaVe=1000000, ChoNgoi='1A'),
    VeMayBay(MaVe='V007', MaHanhKhach='HK07', MaChuyenBay='CB007', LoaiVe='Business', GiaVe=1100000, ChoNgoi='1B'),
    VeMayBay(MaVe='V008', MaHanhKhach='HK08', MaChuyenBay='CB008', LoaiVe='Business', GiaVe=1200000, ChoNgoi='1C'),
    VeMayBay(MaVe='V009', MaHanhKhach='HK09', MaChuyenBay='CB009', LoaiVe='Business', GiaVe=1300000, ChoNgoi='1D'),
    VeMayBay(MaVe='V010', MaHanhKhach='HK10', MaChuyenBay='CB010', LoaiVe='First Class', GiaVe=1400000, ChoNgoi='1E'),
    VeMayBay(MaVe='V011', MaHanhKhach='HK11', MaChuyenBay='CB011', LoaiVe='First Class', GiaVe=1500000, ChoNgoi='1F'),
    VeMayBay(MaVe='V012', MaHanhKhach='HK12', MaChuyenBay='CB012', LoaiVe='First Class', GiaVe=1600000, ChoNgoi='1G'),
    VeMayBay(MaVe='V013', MaHanhKhach='HK13', MaChuyenBay='CB013', LoaiVe='First Class', GiaVe=1700000, ChoNgoi='1H'),
    VeMayBay(MaVe='V014', MaHanhKhach='HK14', MaChuyenBay='CB014', LoaiVe='First Class', GiaVe=1800000, ChoNgoi='1I'),
    VeMayBay(MaVe='V015', MaHanhKhach='HK15', MaChuyenBay='CB015', LoaiVe='First Class', GiaVe=1900000, ChoNgoi='1J')
]
    duongbay_data = []
    for i in range(1, 16):
        so_hieu = f'DB{i:03}'
        thong_tin = f'Duong bay {i}'
        ma_san_bay = f'SBA{i}'
        ma_chuyen_bay = f'CB{i:03}'
        duongbay_data.append(DuongBay(SoHieu=so_hieu, ThongTin=thong_tin, MaSanBay=ma_san_bay, MaChuyenBay=ma_chuyen_bay))
    db.session.add_all(sanbay_data)
    db.session.add_all(hang_hang_khong_data)
    db.session.add_all(ve_may_bay_data)
    db.session.add_all(hanh_khach_data)
    db.session.add_all(chuyen_bay_data)
    db.session.add_all(nhan_vien_data)
    db.session.add_all(duongbay_data)
    db.session.commit()

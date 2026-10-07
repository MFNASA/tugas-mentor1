from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Konfigurasi database SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///siswa.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Registrasi routes/blueprint
    from app.routes.siswa_routes import siswa_bp
    app.register_blueprint(siswa_bp, url_prefix="/api")

    # Route root untuk info API
    @app.route("/")
    def index():
        return jsonify({
            "nama_api": "API Data Siswa",
            "versi": "1.0.0",
            "endpoints": {
                "GET    /api/siswa":        "Lihat semua siswa",
                "POST   /api/siswa":        "Tambah siswa baru",
                "PUT    /api/siswa/<id>":   "Update data siswa",
                "DELETE /api/siswa/<id>":   "Hapus siswa"
            }
        })

    # Buat tabel jika belum ada
    with app.app_context():
        db.create_all()

    return app

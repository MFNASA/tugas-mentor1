from app import db
from datetime import datetime

class Siswa(db.Model):
    __tablename__ = "siswa"

    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama       = db.Column(db.String(100), nullable=False)
    kelas      = db.Column(db.String(50),  nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Konversi model ke dictionary (untuk JSON response)."""
        return {
            "id":         self.id,
            "nama":       self.nama,
            "kelas":      self.kelas,
            "created_at": self.created_at.isoformat()
        }

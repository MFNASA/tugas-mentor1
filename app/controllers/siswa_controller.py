from flask import jsonify
from app.models.siswa import Siswa
from app import db

# ─── GET /api/siswa ────────────────────────────────────────────────────────────
def get_all_siswa():
    """Mengambil seluruh data siswa."""
    semua_siswa = Siswa.query.all()
    return jsonify({
        "status":  "success",
        "message": "Data siswa berhasil diambil",
        "data":    [s.to_dict() for s in semua_siswa]
    }), 200

# ─── POST /api/siswa ───────────────────────────────────────────────────────────
def create_siswa(body):
    """Menambahkan data siswa baru."""
    nama  = body.get("nama")
    kelas = body.get("kelas")

    if not nama or not kelas:
        return jsonify({
            "status":  "error",
            "message": "Field 'nama' dan 'kelas' wajib diisi"
        }), 400

    siswa_baru = Siswa(nama=nama, kelas=kelas)
    db.session.add(siswa_baru)
    db.session.commit()

    return jsonify({
        "status":  "success",
        "message": "Data siswa berhasil ditambahkan",
        "data":    siswa_baru.to_dict()
    }), 201

# ─── PUT /api/siswa/<id> ───────────────────────────────────────────────────────
def update_siswa(id, body):
    """Mengubah data siswa berdasarkan ID."""
    siswa = Siswa.query.get(id)

    if not siswa:
        return jsonify({
            "status":  "error",
            "message": f"Siswa dengan ID {id} tidak ditemukan"
        }), 404

    siswa.nama  = body.get("nama",  siswa.nama)
    siswa.kelas = body.get("kelas", siswa.kelas)
    db.session.commit()

    return jsonify({
        "status":  "success",
        "message": "Data siswa berhasil diubah",
        "data":    siswa.to_dict()
    }), 200

# ─── DELETE /api/siswa/<id> ────────────────────────────────────────────────────
def delete_siswa(id):
    """Menghapus data siswa berdasarkan ID."""
    siswa = Siswa.query.get(id)

    if not siswa:
        return jsonify({
            "status":  "error",
            "message": f"Siswa dengan ID {id} tidak ditemukan"
        }), 404

    db.session.delete(siswa)
    db.session.commit()

    return jsonify({
        "status":  "success",
        "message": f"Siswa '{siswa.nama}' berhasil dihapus"
    }), 200

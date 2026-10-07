from flask import Blueprint, request
from app.controllers.siswa_controller import (
    get_all_siswa,
    create_siswa,
    update_siswa,
    delete_siswa
)

siswa_bp = Blueprint("siswa", __name__)

# GET    /api/siswa        → Lihat semua siswa
@siswa_bp.route("/siswa", methods=["GET"])
def route_get_all():
    return get_all_siswa()

# POST   /api/siswa        → Tambah siswa baru
@siswa_bp.route("/siswa", methods=["POST"])
def route_create():
    body = request.get_json()
    return create_siswa(body)

# PUT    /api/siswa/<id>   → Ubah data siswa
@siswa_bp.route("/siswa/<int:id>", methods=["PUT"])
def route_update(id):
    body = request.get_json()
    return update_siswa(id, body)

# DELETE /api/siswa/<id>   → Hapus siswa
@siswa_bp.route("/siswa/<int:id>", methods=["DELETE"])
def route_delete(id):
    return delete_siswa(id)

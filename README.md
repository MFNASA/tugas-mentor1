# API Data Siswa 📚

REST API sederhana untuk manajemen data siswa sekolah, dibangun dengan **Python + Flask + SQLite**.

## 📁 Struktur Project

```
api-data-siswa/
├── app/
│   ├── __init__.py              # App factory & konfigurasi
│   ├── controllers/
│   │   └── siswa_controller.py  # Business logic CRUD
│   ├── models/
│   │   └── siswa.py             # Model database Siswa
│   └── routes/
│       └── siswa_routes.py      # Definisi endpoint API
├── requirements.txt             # Dependensi Python
├── run.py                       # Entry point aplikasi
└── README.md
```

## ⚙️ Cara Menjalankan

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Jalankan server
```bash
python run.py
```

Server akan berjalan di: `http://localhost:5000`

---

## 🔗 Endpoint API

| Method   | Endpoint          | Keterangan              |
|----------|-------------------|-------------------------|
| `GET`    | /api/siswa        | Lihat semua siswa       |
| `POST`   | /api/siswa        | Tambah siswa baru       |
| `PUT`    | /api/siswa/{id}   | Ubah data siswa         |
| `DELETE` | /api/siswa/{id}   | Hapus siswa             |

---

## 📤 Contoh Request & Response

### POST /api/siswa — Tambah Siswa

**Request Body:**
```json
{
  "nama": "Prabowo",
  "kelas": "XII RPL"
}
```

**Response (201 Created):**
```json
{
  "status": "success",
  "message": "Data siswa berhasil ditambahkan",
  "data": {
    "id": 1,
    "nama": "Prabowo",
    "kelas": "XII RPL",
    "created_at": "2026-10-07T09:43:00"
  }
}
```

# Demonstrasi Anti-Aliasing dengan Super-Sampling menggunakan Python Pillow

Proyek ini berisi dua skrip Python (`anti_aliasing.py` dan `anti_aliasing_lingkaran.py`) yang mendemonstrasikan efek anti-aliasing menggunakan teknik super-sampling. Skrip ini memanfaatkan pustaka Pillow (PIL Fork) untuk menggambar dan memanipulasi gambar.

## Deskripsi

**Aliasing** dalam grafika komputer adalah munculnya artefak visual seperti tepi bergerigi (jaggies) pada objek. **Anti-aliasing** adalah teknik untuk mengurangi efek ini, menghasilkan gambar yang terlihat lebih halus.

Skrip dalam repositori ini mengilustrasikan:
1.  Bagaimana garis dan lingkaran terlihat tanpa anti-aliasing.
2.  Bagaimana teknik **super-sampling** dapat diterapkan untuk menghasilkan anti-aliasing.
3.  Perbandingan efek anti-aliasing dengan berbagai skala super-sampling pada objek lingkaran.

## Fitur

* Demonstrasi visual efek aliasing pada garis dan lingkaran.
* Implementasi sederhana teknik anti-aliasing super-sampling.
* Perbandingan berdampingan antara gambar dengan dan tanpa anti-aliasing.
* Eksplorasi pengaruh skala super-sampling yang berbeda (2x, 4x, 8x) terhadap kualitas anti-aliasing pada lingkaran.

## Kebutuhan Sistem

* Python 3.x
* Pustaka Pillow

## Instalasi

1.  Pastikan Anda telah menginstal Python 3.x.
2.  Clone repositori ini (jika Anda mengunggahnya ke GitHub):
    ```bash
    git clone [https://github.com/rifkyadiii/anti_aliasing_grafkonm_pert12.git]
    cd [anti_aliasing_grafkom_pert12]
    ```
3.  Instal pustaka Pillow menggunakan pip:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Menjalankan

Anda dapat menjalankan masing-masing skrip secara terpisah dari terminal atau command prompt:

1.  **Untuk demonstrasi anti-aliasing pada garis:**
    ```bash
    python anti_aliasing.py
    ```
    Skrip ini akan menampilkan jendela gambar yang berisi dua versi garis: satu tanpa anti-aliasing (kiri) dan satu dengan anti-aliasing menggunakan super-sampling 4x (kanan).

2.  **Untuk demonstrasi anti-aliasing pada lingkaran dengan berbagai skala:**
    ```bash
    python anti_aliasing_lingkaran.py
    ```
    Skrip ini akan menampilkan jendela gambar yang berisi empat versi lingkaran: "Tanpa AA", "Skala 2", "Skala 4", dan "Skala 8", yang menunjukkan peningkatan kehalusan dengan meningkatnya skala super-sampling.

## Penjelasan Skrip

* **`anti_aliasing.py`**:
    * Membuat gambar garis diagonal tanpa anti-aliasing.
    * Membuat gambar garis diagonal yang sama dengan anti-aliasing menggunakan teknik super-sampling (render pada skala 4x lebih besar, lalu downsample).
    * Menampilkan kedua gambar berdampingan untuk perbandingan.

* **`anti_aliasing_lingkaran.py`**:
    * Membuat gambar lingkaran tanpa anti-aliasing sebagai baseline.
    * Membuat tiga gambar lingkaran tambahan dengan anti-aliasing menggunakan super-sampling pada skala 2x, 4x, dan 8x.
    * Setiap lingkaran pada resolusi tinggi digambar, lalu di-downsample ke ukuran target menggunakan filter `Image.LANCZOS`.
    * Menampilkan keempat gambar berdampingan dengan label untuk perbandingan efek dari skala super-sampling yang berbeda.

## Keluaran yang Diharapkan

Setelah menjalankan skrip, sebuah jendela akan muncul menampilkan gambar hasil:
* `anti_aliasing.py`: Menampilkan gambar gabungan dengan label "Kiri: Tanpa Anti-Aliasing | Kanan: Dengan Super-Sampling".
* `anti_aliasing_lingkaran.py`: Menampilkan gambar gabungan dengan beberapa lingkaran, masing-masing diberi label sesuai dengan metode atau skala anti-aliasing yang diterapkan.

---

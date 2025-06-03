from PIL import Image, ImageDraw

# Ukuran gambar akhir
width, height = 200, 200

# ----------------------------------------
# Tanpa Anti-Aliasing (Baseline)
# ----------------------------------------
img_raw = Image.new("RGB", (width, height), "white")
draw_raw = ImageDraw.Draw(img_raw)
draw_raw.ellipse((20, 20, 180, 180), fill="blue")

# List skala yang akan dieksperimenkan
scales = [2, 4, 8]
# List untuk menyimpan gambar-gambar anti-aliased
anti_aliased_images = []

# Tambahkan gambar tanpa anti-aliasing ke daftar untuk perbandingan
anti_aliased_images.append({"image": img_raw, "label": "Tanpa AA"})

# ----------------------------------------
# Eksperimen dengan Berbagai Skala Super Sampling
# ----------------------------------------
for scale in scales:
    # Buat gambar resolusi tinggi untuk super-sampling
    img_supersample = Image.new("RGB", (width * scale, height * scale), "white")
    draw_high = ImageDraw.Draw(img_supersample)

    # Gambar lingkaran pada resolusi tinggi
    draw_high.ellipse(
       (20 * scale, 20 * scale, 180 * scale, 180 * scale),
       fill="blue"
    )

    # Downsampling untuk anti-aliasing
    img_aa = img_supersample.resize((width, height), Image.LANCZOS)
    anti_aliased_images.append({"image": img_aa, "label": f"Skala {scale}"})

# ----------------------------------------
# Gabungkan semua gambar untuk perbandingan
# ----------------------------------------
# Hitung lebar total yang dibutuhkan untuk semua gambar + jarak antar gambar
total_width = (width * len(anti_aliased_images)) + (20 * (len(anti_aliased_images) - 1))
combined = Image.new("RGB", (total_width, height + 30), "gray") # Tambah tinggi untuk label

# Tempel setiap gambar ke gambar gabungan
x_offset = 0
for item in anti_aliased_images:
    combined.paste(item["image"], (x_offset, 0))

    draw_combined = ImageDraw.Draw(combined)
    text_color = "black"
    try:
        draw_combined.text((x_offset + width // 2 - 30, height + 5), item["label"], fill=text_color)
    except Exception:
        draw_combined.text((x_offset + width // 2 - 30, height + 5), item["label"], fill=text_color)


    x_offset += width + 20 # Pindah offset untuk gambar berikutnya

# Simpan hasil
combined.show()
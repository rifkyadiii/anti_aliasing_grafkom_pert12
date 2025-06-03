from PIL import Image, ImageDraw

# Ukuran gambar akhir
width, height = 200, 200

# ----------------------------------------
# Versi 1: Tanpa Anti-Aliasing
# ----------------------------------------
img_raw = Image.new("RGB", (width, height), "white")
draw_raw = ImageDraw.Draw(img_raw)

# Gambar garis miring (tanpa anti-aliasing)
draw_raw.line((20, 100, 180, 20), fill="blue", width=3)

# ----------------------------------------
# Versi 2: Dengan Anti-Aliasing (Super Sampling)
# ----------------------------------------
scale = 4
img_supersample = Image.new("RGB", (width * scale, height * scale), "white")
draw_high = ImageDraw.Draw(img_supersample)

# Gambar garis pada resolusi tinggi
draw_high.line(
   (20 * scale, 100 * scale, 180 * scale, 20 * scale),
   fill="blue",
   width=3 * scale
)

# Downsampling (anti-aliasing terjadi di sini)
img_aa = img_supersample.resize((width, height), Image.LANCZOS)

# Gabungkan kedua gambar untuk perbandingan
combined = Image.new("RGB", (width * 2 + 20, height), "gray")
combined.paste(img_raw, (0, 0))
combined.paste(img_aa, (width + 20, 0))

# Tambahkan label jika perlu (opsional)
print("Kiri: Tanpa Anti-Aliasing | Kanan: Dengan Super-Sampling")

# Simpan hasil
combined.show()
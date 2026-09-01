import os
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------------------------------------------
# Opsi 1: Jika menggunakan Google Colab & ingin mengunggah file:
# from google.colab import files
# uploaded = files.upload()
#
# Opsi 2: Jika dari Google Drive (Colab):
# from google.colab import drive
# drive.mount('/content/drive')
# -------------------------------------------------------------

# Path ke file citra
path_img1 = 'WEEK 1/KTM1D.jpg'
path_img2 = 'WEEK 1/KTM2D.jpg'

# 1. Membaca Citra menggunakan PIL
img1 = Image.open(path_img1)
img2 = Image.open(path_img2)

# 2. Mengambil Informasi Dimensi (Lebar x Tinggi x Kanal)
width1, height1 = img1.size
channels1 = len(img1.getbands())

width2, height2 = img2.size
channels2 = len(img2.getbands())

# 3. Mengambil Ukuran File (Bytes -> KB & MB)
size_bytes1 = os.path.getsize(path_img1)
size_kb1 = size_bytes1 / 1024
size_mb1 = size_kb1 / 1024

size_bytes2 = os.path.getsize(path_img2)
size_kb2 = size_bytes2 / 1024
size_mb2 = size_kb2 / 1024

# 4. Menampilkan Hasil Informasi ke Terminal / Output
print("=" * 60)
print(f"INFORMASI CITRA 1 ({os.path.basename(path_img1)}):")
print(f"- Dimensi (Lebar x Tinggi) : {width1} x {height1} piksel")
print(f"- Kanal Warna (Mode)       : {img1.mode} ({channels1} kanal)")
print(f"- Total Piksel             : {width1 * height1:,} piksel (~{(width1 * height1)/1e6:.2f} MP)")
print(f"- Ukuran File              : {size_bytes1:,} Bytes | {size_kb1:.2f} KB | {size_mb1:.2f} MB")
print("=" * 60)

print(f"INFORMASI CITRA 2 ({os.path.basename(path_img2)}):")
print(f"- Dimensi (Lebar x Tinggi) : {width2} x {height2} piksel")
print(f"- Kanal Warna (Mode)       : {img2.mode} ({channels2} kanal)")
print(f"- Total Piksel             : {width2 * height2:,} piksel (~{(width2 * height2)/1e6:.2f} MP)")
print(f"- Ukuran File              : {size_bytes2:,} Bytes | {size_kb2:.2f} KB | {size_mb2:.2f} MB")
print("=" * 60)

# 5. Menampilkan Kedua Citra Berdampingan
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].imshow(img1)
axes[0].set_title(f"KTM1D.jpg\n{width1}x{height1} px | {size_mb1:.2f} MB")
axes[0].axis('on')  # Menampilkan sumbu piksel

axes[1].imshow(img2)
axes[1].set_title(f"KTM2D.jpg\n{width2}x{height2} px | {size_kb2:.2f} KB")
axes[1].axis('on')

plt.tight_layout()
plt.show()

import streamlit as st
import math

# Menampilkan rumus matematika menggunakan LaTeX
st.latex(r"V = \pi r^2 t")


[Image of the formula for the volume of a cylinder]


def hitung_volume_tabung(r, t):
    """Menghitung Volume Tabung = pi * r^2 * t"""
    # Menggunakan math.pi untuk nilai yang lebih akurat
    volume = math.pi * r * r * t
    return volume

# --- Konfigurasi Halaman Streamlit ---

st.title("🧪 Kalkulator Volume Tabung")
st.markdown("Masukkan nilai jari-jari (r) dan tinggi (t) tabung.")

# Input Jari-jari (r)
jari_jari = st.number_input(
    "Masukkan Jari-jari (r):", 
    min_value=0.0, 
    value=5.0, 
    key="r_input", 
    format="%.2f"
)

# Input Tinggi (t)
tinggi = st.number_input(
    "Masukkan Tinggi (t):", 
    min_value=0.0, 
    value=10.0, 
    key="t_input", 
    format="%.2f"
)

# Tombol untuk memicu perhitungan
if st.button("Hitung Volume"):
    
    # Validasi input
    if jari_jari <= 0 or tinggi <= 0:
        st.error("Jari-jari dan Tinggi harus lebih besar dari nol.")
    else:
        # Panggil fungsi
        hasil_volume = hitung_volume_tabung(jari_jari, tinggi)
        
        # Tampilkan Output
        st.success(f"**Volume tabung adalah: {hasil_volume:.2f} satuan kubik**")
        st.balloons()

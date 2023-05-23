import requests
from bs4 import BeautifulSoup
import time

wallet_address = "alamat_dompet_anda"

def claim(wallet):
    url = "https://pls-faucet.com/"

    # Buat session dan dapatkan halaman klaim
    session = requests.Session()
    response = session.get(url)

    # Parsing halaman menggunakan BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Cari elemen input alamat dompet
    wallet_input = soup.find("input", {"id": "wallet"})

    if wallet_input is None:
        print("Gagal mengklaim. Halaman tidak ditemukan.")
        return

    # Isi alamat dompet
    wallet_input["value"] = wallet

    # Kirim permintaan klaim
    response = session.post(url, data=soup.form.attrs)

    # Periksa hasil klaim
    success_message = "Hadiah diklaim" in response.text

    if success_message:
        print("Berhasil mengklaim.")
    else:
        print("Gagal mengklaim.")

if __name__ == '__main__':
    while True:
        claim(wallet_address)
        print("Menunggu untuk klaim selanjutnya...")
        time.sleep(25 * 60)  # Tunggu selama 25 menit sebelum klaim berikutnya

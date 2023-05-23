import requests
import time

wallet_address = "alamat_dompet_anda"

def claim(wallet):
    url = "https://pls-faucet.com/server/claim-free"

    data = {
        "address": wallet
    }

    response = requests.get(url, params=data)
    res = response.json()

    if "error" in res and res["error"] == "wait 1 hour":
        print(f"Akun {wallet}: Perlu menunggu cooldown")
    else:
        print(f"Akun {wallet}: Hadiah diklaim")

if __name__ == '__main__':
    while True:
        claim(wallet_address)
        print("Menunggu untuk klaim selanjutnya...")
        time.sleep(25 * 60)  # Tunggu selama 25 menit sebelum klaim berikutnya

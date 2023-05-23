from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wallet_addresses = ["alamat_dompet_1", "alamat_dompet_2", "alamat_dompet_3"]  # Daftar alamat dompet yang akan digunakan
claim_attempts = 5  # Jumlah upaya klaim pada setiap alamat dompet

def claim(wallet):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode headless (tanpa GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome("/data/data/com.termux/files/usr/bin/chromedriver", options=chrome_options)  # Menggunakan path ChromeDriver di Termux
    driver.get("https://pls-faucet.com/")

    for _ in range(claim_attempts):
        # Isi alamat dompet
        wallet_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wallet")))
        wallet_input.clear()
        wallet_input.send_keys(wallet)

        # Tunggu beberapa detik agar halaman selesai memuat
        time.sleep(5)

        # Submit klaim
        claim_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "claim")))
        claim_button.click()

        # Tunggu klaim selesai
        success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "success")))

    driver.quit()

if __name__ == '__main__':
    for wallet in wallet_addresses:
        claim(wallet)
        print(f"Berhasil mengklaim pada dompet: {wallet}")
        print("Menunggu untuk klaim selanjutnya...")
        time.sleep(25 * 60)  # Tunggu selama 25 menit sebelum klaim berikutnya

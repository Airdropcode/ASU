from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

wallet_address = "alamat_dompet_anda"

def claim(wallet):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Menjalankan Chrome dalam mode headless (tanpa GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome("/storage/emulated/0/pictures/chromedriver", options=chrome_options)  # Ganti dengan path sebenarnya ke ChromeDriver di direktori yang sesuai
    driver.get("https://pls-faucet.com/")

    # Isi alamat dompet
    wallet_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "wallet")))
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
    while True:
        claim(wallet_address)
        print("Berhasil mengklaim.")
        print("Menunggu untuk klaim selanjutnya...")
        time.sleep(25 * 60)  # Tunggu selama 25 menit sebelum klaim berikutnya

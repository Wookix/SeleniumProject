from pages.download_page import DownloadPage
import time

def test_download():
    down = DownloadPage()

    down.open_download_page()
    time.sleep(1)

    filename = down.click_first_file()
    print(f"Descargando archivo: {filename}")

    # Esperar la descarga (simple)
    time.sleep(3)

    exists = down.file_exists_in_downloads(filename)
    print("¿El archivo se descargó?:", exists)

    down.close()

if __name__ == "__main__":
    test_download()

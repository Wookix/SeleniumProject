from pages.upload_page import UploadPage
import time

def test_upload():
    up = UploadPage()

    up.open_upload_page()
    time.sleep(1)

    up.upload_file("prueba.txt")
    time.sleep(1)

    msg = up.get_message()
    print("Mensaje:", msg)

    up.close()

if __name__ == "__main__":
    test_upload()

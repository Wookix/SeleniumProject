from pages.login_page import LoginPage
import time

# Usuario de prueba que ofrece la página
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

def test_login():
    login = LoginPage()
    login.open_login()
    
    login.enter_username(USERNAME)
    login.enter_password(PASSWORD)
    login.click_login()

    time.sleep(2)  # Pausa para ver el resultado en pantalla
    
    message = login.get_success_message()
    print("MENSAJE MOSTRADO:", message)

    login.close()

if __name__ == "__main__":
    test_login()

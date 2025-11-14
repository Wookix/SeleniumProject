from pages.navigation_page import NavigationPage
import time

def test_navigation():
    nav = NavigationPage()

    # Home
    nav.go_to_home()
    print("Home cargado.")
    time.sleep(1)

    # Checkboxes
    nav.go_to_checkbox()
    print("Página:", nav.get_title())
    time.sleep(1)

    # Inputs
    nav.go_to_inputs()
    print("Página:", nav.get_title())
    time.sleep(1)

    # Alerts
    nav.go_to_alerts()
    print("Página:", nav.get_title())
    time.sleep(1)

    nav.close()

if __name__ == "__main__":
    test_navigation()

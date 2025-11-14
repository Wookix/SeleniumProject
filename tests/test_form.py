from pages.form_page import FormPage
import time

def test_form():
    form = FormPage()

    # --- Inputs ---
    form.open_inputs()
    form.enter_number(12345)
    time.sleep(1)

    value = form.get_number_value()
    print("Valor ingresado en input:", value)

    # --- Dropdown ---
    form.open_dropdown()
    form.select_dropdown_option("2")  # Selecciona Option 2
    time.sleep(1)

    selected = form.get_selected_dropdown_text()
    print("Opción seleccionada:", selected)

    form.close()


if __name__ == "__main__":
    test_form()

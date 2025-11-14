from pages.table_page import TablePage
import time

def test_table():
    table = TablePage()

    table.open_table()
    time.sleep(1)

    data = table.extract_table_data()

    print("Datos extraídos de la tabla:")
    for row in data:
        print(row)

    # Guardar en CSV
    table.save_to_csv(data)

    table.close()

if __name__ == "__main__":
    test_table()

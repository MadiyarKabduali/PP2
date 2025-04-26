import psycopg2
import csv

# Подключение к БД
con = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="postgres",
    password="1234"
)

cur = con.cursor()

# Создание таблицы, если не существует
table = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
"""
cur.execute(table)
con.commit()
print("Таблица создана")

# Запрос на добавление
contact_q = """
    INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)
"""

def contact(name, phone):
    try:
        cur.execute(contact_q, (name, phone))
        con.commit()
        print(f"Контакт \"{name}\" с номером \"{phone}\" добавлен")
    except Exception as e:
        print(f"Не удалось добавить контакт: {e}")

# Меню
print("""
        Меню
      1 - Добавить контакт
      2 - Удалить контакт
      3 - Вывести таблицу
      4 - Обновить контакт
      5 - Ввести CSV файл
      6 - Drop table
      q - Выйти 
""")

while True:
    menu = input("Выберите пункт меню: ")

    if menu == "1":
        name = input("Введите имя контакта: ")
        phone = input("Введите телефон: ")
        contact(name, phone)

    elif menu == "2":
        menu_del = input("1 — удаление по имени, 2 — по номеру: ")
        if menu_del == "1":
            name = input("Имя: ")
            try:
                cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
                con.commit()
                print("Контакт удален")
            except Exception as e:
                print(f"Не удалось удалить контакт: {e}")
        elif menu_del == "2":
            phone = input("Номер: ")
            try:
                cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
                con.commit()
                print("Контакт удален")
            except Exception as e:
                print(f"Не удалось удалить контакт: {e}")

    elif menu == "3":
        try:
            cur.execute("SELECT id, name, phone FROM PhoneBook")
            rows = cur.fetchall()
            print("Список контактов:")
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Ошибка при выводе таблицы: {e}")

    elif menu == "4":
        menu_up = input("Введите 1 (обновить по имени) или 2 (по номеру): ")
        if menu_up == "1":
            old_name = input("Введите имя, которое нужно обновить: ")
            new_phone = input("Введите новый номер: ")
            try:
                cur.execute(
                    "UPDATE PhoneBook SET phone = %s WHERE name = %s",
                    (new_phone, old_name)
                )
                con.commit()
                print("Контакт обновлён")
            except Exception as e:
                print(f"Ошибка при обновлении: {e}")
        elif menu_up == "2":
            old_phone = input("Введите номер, который нужно обновить: ")
            new_name = input("Введите новое имя: ")
            try:
                cur.execute(
                    "UPDATE PhoneBook SET name = %s WHERE phone = %s",
                    (new_name, old_phone)
                )
                con.commit()
                print("Контакт обновлён")
            except Exception as e:
                print(f"Ошибка при обновлении: {e}")

    elif menu == "5":
        fpath = input("Введите путь к CSV-файлу: ")
        try:
            with open(fpath, newline='', encoding='utf-8') as csvf:
                read = csv.DictReader(csvf)
                for row in read:
                    cur.execute(
                        "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)",
                        (row['name'], row['phone'])
                    )
            con.commit()
            print("CSV импорт завершён")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")
    elif menu == "6":
        try:
            cur.execute("Drop table PhoneBook")
            print("Уничтожение завершено")
            con.commit()
        except: 
            print("Не")


    elif menu == "q":
        print("Выход...")
        break

    else:
        print("Неверный пункт меню. Повторите ввод.")

# Закрытие соединения
cur.close()
con.close()

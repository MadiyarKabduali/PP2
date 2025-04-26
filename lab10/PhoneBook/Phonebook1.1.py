import psycopg2
import csv

# Connect to DB
con = psycopg2.connect(
    host="localhost",
    database="PhoneBook",
    user="postgres",
    password="1234"
)

cur = con.cursor()

# Create table if not exists
table = """
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
"""
cur.execute(table)
print("Таблица создана")

# Insert query
contact_q = """
    INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)
"""

def contact(name, phone):
    try:
        cur.execute(contact_q, (name, phone))
        con.commit()
        print(f"Контакт \"{name}\" с номером \"{phone}\" добавлен")
    except:
        print("Не удалось добавить контакт")

print("""
        Меню
      1 - Добавить контакт
      2 - Удалить контакт
      3 - Вывести таблицу
      4 - обновить контакт
      5 - Ввести csv файл
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
            delq = "DELETE FROM PhoneBook WHERE name = %s"
            try:
                cur.execute(delq, (name,))
                con.commit()
                print("Контакт удален")
            except:
                print("Не удалось удалить контакт")
        elif menu_del == "2":
            phone = input("Номер: ")
            delq = "DELETE FROM PhoneBook WHERE phone = %s"
            try:
                cur.execute(delq, (phone,))
                con.commit()
                print("Контакт удален")
            except:
                print("Не удалось удалить контакт")

    elif menu == "3":
        cur.execute("SELECT id, name, phone FROM PhoneBook")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif menu == "4":
        menu_up=("Введите 1(по имени) или 2(по номеру):")
        if menu_up == 1:
            old_name = input("Введите имя, которое нужно обновить: ")
            new_phone = input("Введите новый номер: ")
            cur.execute(
                    "UPDATE PhoneBook SET phone = %s WHERE name = %s",
                    (new_phone, old_name)
                    )
        elif menu == 2:
            old_phone = input("Введите номер, который нужно обновить: ")
            new_name = input("Введите новое имя: ")
            cur.execute(
                    "UPDATE PhoneBook SET name = %s WHERE phone = %s",
                    (new_name, old_phone)
                )
        else:
            break
    elif menu == 5:
        fpath = input("Введите путь csv")
        with open(fpath, newline='') as csvf:
            read = csv.DictReader(csvf)
            for row in read():
                cur.execute(
                    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                            (row['name'], row['phone'])
                )
    elif menu == "q":
        break
    else:
        break

# Закрыть соединение
con.close()

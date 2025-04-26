import psycopg2

#connect to db 

con = psycopg2.connect(
    host = "Localhost",
    database = "PhoneBook",
    user = "postgres",
    password = "1234"
)

#cursor 

cur = con.cursor()

pars = """
    select id,name,phone from PhoneBook 
"""

table = """
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """
contact_q = """
        insert into PhoneBook (name,phone) VALUES (%s, %s) 
"""
try:
    cur.execute(table)
    print("Table created")
except:
    print("Table not created")
def contact(name,phone):
    try:
        cur.execute(contact_q,(name,phone))
        print(f"contact \"{name}\" with \"{phone}\" is created")
    except:
        print("cant insert contact")
print("""
        Меню
      1 - Добавить контакт
      2 - Удалить контакт
      3 - Вывести таблицу
      q - выйти 
      """)
while True:
    menu = input()
    if menu == 1:
        name = input("Введите имя контакта : ")
        phone = input("Введите телефон : ")
        contact(name,phone)
    elif menu == 2:
        menu_del = input("1 удаление по имени, 2 по номеру")
        if menu_del == 1:
            name = input("Имя: ")
            delq = f"""
delete from PhoneBook where name = {name}
    """
            try:
                cur.execute(delq)
                print("контакт удален")
            except:
                print("немогу удалить")
        elif menu_del == 2:
            phone == input("Номер: ")
            delq = f"""
delete from PhoneBook where phone = {phone}
    """
            try:
                cur.execute(delq)
                print("контакт удален")
            except:
                print("немогу удалить")
        elif menu == 3:
            cur.execute(pars)
            for row in cur.fetchall():
                print(row)
        elif menu == "q":
            break
#close the connection 
con.close()
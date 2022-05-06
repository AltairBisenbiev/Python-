import csv
import psycopg2
from config import config

phone_list = []

def read_csv():
    with open('phone.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'name: {row[0]}, number: {row[1]}')
                phone_list.append((row[0], row[1]))
                line_count += 1

def insert():
    sql = "INSERT INTO phonebook VALUES(%s, %s)"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.executemany(sql, phone_list)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_con():
    print("Enter name and phone number separated by space")
    s = input().split()
    sql = f"INSERT INTO phonebook VALUES('{s[0]}', '{s[1]}')"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def change():
    print('Type "name" if you want to change name\nType "number" if you want to change number')
    c = input()
    sql = 'SELECT * FROM phonebook'
    if c == 'name':
        print("Type NAME you want to change and NAME you want it to be changed to")
        s = input().split()
        sql = (f"UPDATE phonebook SET name = '{s[1]}' WHERE name = '{s[0]}'")
    elif c == 'number':
        print("Type the NAME whose number you want to change and NUMBER you want to change to")
        s = input().split()
        sql = f"UPDATE phonebook SET phone_number = '{s[1]}' WHERE name = '{s[0]}'"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql, (s[0], s[1]))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def delete():
    print("Type NAME of a person whose data you want to delete")
    s = input()
    sql = f"DELETE FROM phonebook WHERE name = '{s}'"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql, (s[0], s[1]))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def show():
    sql = "SELECT * FROM phonebook"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print('number  phone_number\n')
        for x in result:
            print(*x)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def show_byname():
    print('Enter name: ')
    name = input()
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.callproc('show_table', (name, ))
        result = cursor.fetchall()
        print('number  phone_number\n')
        for x in result:
            print(*x)
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def update():
    print('Enter name: ')
    name = input()
    print('Enter number: ')
    number = input()
    sql = f"CALL add_user('{name}', '{number}');"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        for x in result:
            print(*x)
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def update_many():
    print('Enter number of new contacts: ')
    n = int(input())
    print("Enter contacts' names and phone numbers seperated by space: " )
    names = []
    numbers = []
    for i in range(0, n):
        name, number = input().split()
        names.append(name)
        numbers.append(number)
    s1 = ", ".join(["'" + str(i) + "'" for i in names])
    s2 = ", ".join(["'" + str(i) + "'" for i in numbers])
    sql = f"SELECT * FROM add_many(ARRAY [{s1}], ARRAY [{s2}], {n});"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql, (s1, s2))
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        print("The following entries are wrong: ")
        for x in result:
            print(*x)
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_byname():
    print('Enter name: ')
    name = input()
    sql = f"CALL delete_byname('{name}');"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def show_pag():
    print('Enter the number of contacts you want to see and page number: ')
    lim, offs = list(map(int, input().split()))
    sql = f"SELECT * FROM show_pag({lim}, {offs});"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        for x in result:
            print(*x)
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if conn is not None:
            conn.close()

def main():
    read_csv()
    while True:
        print('Push:\n1 - insert from csv,\n2 - insert from console,\n3 - change info,\n4 - delete data,\n5 - show table,\n6 - exit,\n7 - show by name\n8 - update if exists\n9 - insert many(correct number check)\n10 - delete(function)\n11 - pagination')
        command = input()
        #tasks of Lab 10
        if command == '1':
            insert()
        if command == '2':
            insert_con()
        if command == '3':
            change()
        if command == '4':
            delete()
        if command == '5':
            show()
        if command == '6':
            break
        #tasks of Lab 11
        if command == '7':
            show_byname()
        if command == '8':
            update()
        if command == '9':
            update_many()
        if command == '10':
            delete_byname()
        if command == '11':
            show_pag()

main()
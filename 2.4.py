# coding=Windows_1251
import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
migr_dir = os.path.join(current_dir, migrations)

def searching():
    search = input('Введите строку:')
    counter = int()
    sql_list = os.listdir(migr_dir)
    for f in sql_list:
        if f.endswith(".sql"):
            if f in sql_list
            for line in f:
                if search in f:
                    print(f)
                    counter += 1
                else:
                    sql_list.remove(f)

    print(counter)

if __name__ == '__main__':
    while True:
        searching()


            # sql_list.append(os.path.join(migr_dir, file))

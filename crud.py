from sqlalchemy import create_engine
from sqlalchemy import delete

engine = create_engine("postgresql://postgres:43511@localhost:5432/postgres")
connection = engine.connect()

options = ['1. Province', '2. District', '3. Municipality', '4. Province District', '5. District Municipality',
           '6. Exit']
inner_option = ['a. Create', 'b. Update', 'c. Delete', 'd. Go back']


def insert_province():
    stmt = 'INSERT INTO province(province_name) VALUES(%s)'
    province = input('Enter province name:')
    connection.execute(stmt, (province,))


def display_province():
    stmt = 'SELECT * FROM province'
    results = connection.execute(stmt).fetchall()
    for result in results:
        print(result[0])


def update_province():
    province = input('Enter province name:')
    stmt = 'SELECT * FROM province WHERE province_name = %s;'
    rows = connection.execute(stmt, (province,)).rowcount
    if rows == 0:
        print("Please provide valid province name")
        update_province()
    else:
        new_province = input('Enter new province name:')
        stmt = 'UPDATE province SET province_name = %s WHERE province_name=%s'
        connection.execute(stmt, (new_province, province))


def delete_province():
    province = input("Enter province name:")
    stmt = 'DELETE FROM province WHERE province_name = %s;'
    rows = connection.execute(stmt, (province,)).rowcount
    if rows == 0:
        print("Please provide valid province name")
        delete_province()

    # getting all district name lying in the province
    district_stmt = 'SELECT district_name from district where province_name = %s'
    districts = connection.execute(district_stmt, (province,)).fetchall()
    municipality_stmt = 'DELETE FROM municipality WHERE district_name = %s'
    # looping through districts to delete records from municipality table
    for district in districts:
        print(district[0])
        connection.execute(municipality_stmt, (district,))
    # deleting districts lying in the province
    stmt = 'DELETE FROM district WHERE province_name = %s'
    connection.execute(stmt, (province,))


def display_district():
    stmt = 'SELECT * FROM district'
    results = connection.execute(stmt).fetchall()
    for result in results:
        print(result[0])


def insert_district():
    province = input('Enter province name:')
    stmt = 'SELECT * FROM province WHERE province_name = %s;'
    rows = connection.execute(stmt, (province,)).rowcount
    if rows == 0:
        print("Please provide valid province name as listed")
        insert_district()
    else:
        district = input('Enter district name:')
        stmt = 'INSERT INTO district(district_name,province_name) VALUES(%s,%s)'
        connection.execute(stmt, (district, province))


def update_district():
    district = input('Enter district name:')
    stmt = 'SELECT * FROM district WHERE district_name = %s;'
    rows = connection.execute(stmt, (district,)).rowcount
    if rows == 0:
        print("Please provide valid district name")
        update_district()
    else:
        new_district = input('Enter new district name:')
        stmt = 'UPDATE district SET district_name = %s WHERE district_name=%s'
        connection.execute(stmt, (new_district, district))


def delete_district():
    district = input("Enter district name:")
    stmt = 'DELETE FROM district WHERE district_name = %s;'
    rows = connection.execute(stmt, (district,)).rowcount
    if rows == 0:
        print("Please provide valid district name")
        delete_district()
    stmt = 'DELETE FROM municipality WHERE district_name = %s'
    connection.execute(stmt, (district,))


def display_municipality():
    stmt = 'SELECT * FROM municipality'
    results = connection.execute(stmt).fetchall()
    for result in results:
        print(result[0])


def insert_municipality():
    district = input('Enter district name:')
    stmt = 'SELECT * FROM district WHERE district_name = %s;'
    rows = connection.execute(stmt, (district,)).rowcount
    if rows == 0:
        print("Please provide valid district name as listed")
        insert_municipality()
    else:
        municipality = input('Enter municipality name:')
        stmt = 'INSERT INTO municipality(municipality_name,district_name) VALUES(%s,%s)'
        connection.execute(stmt, (municipality, district))


def update_municipality():
    municipality = input('Enter municipality name:')
    stmt = 'SELECT * FROM municipality WHERE municipality_name = %s;'
    rows = connection.execute(stmt, (municipality,)).rowcount
    if rows == 0:
        print("Please provide valid municipality name")
        update_municipality()
    else:
        new_municipality = input('Enter new municipality name:')
        stmt = 'UPDATE municipality SET municipality_name = %s WHERE municipality_name=%s'
        connection.execute(stmt, (new_municipality, municipality))


def delete_municipality():
    municipality = input("Enter municipality name:")
    stmt = 'DELETE FROM municipality WHERE municipality_name = %s;'
    rows = connection.execute(stmt, (municipality,)).rowcount
    if rows == 0:
        print("Please provide valid municipality name")
        delete_municipality()

def display_province_district():
    province = input("Enter province name:")
    stmt = 'SELECT * FROM province WHERE province_name = %s;'
    rows = connection.execute(stmt, (province,)).rowcount
    if rows == 0:
        print("Please provide valid province name")
        display_province_district()
    else:
        stmt = 'SELECT district_name FROM district WHERE province_name = %s'
        results = connection.execute(stmt, (province,)).fetchall()
        for result in results:
            print(result[0])


def display_district_municipality():
    district = input("Enter district name:")
    stmt = 'SELECT * FROM district WHERE district_name = %s;'
    rows = connection.execute(stmt, (district,)).rowcount
    if rows == 0:
        print("Please provide valid district name")
        display_district_municipality()
    else:
        stmt = 'SELECT municipality_name FROM municipality WHERE district_name = %s'
        results = connection.execute(stmt, (district,)).fetchall()
        for result in results:
            print(result[0])


def main():
    while True:
        print('#######################################')
        print("All operations")
        print('#######################################')
        for option in options:
            print(option)
        input_option = int(input("Enter a Option: "))
        if input_option == 1:
            print('#######################################')
            print("Province Options")
            for option in inner_option:
                print(option)
            input_option = input("Enter a Option:")
            if input_option == 'a':
                insert_province()

            elif input_option == 'b':
                print('\nAvailable provinces')
                display_province()
                update_province()

            elif input_option == 'c':
                display_province()
                delete_province()

            elif input_option == 'd':
                continue

        elif input_option == 2:
            print('#######################################')
            print("District Options")
            for option in inner_option:
                print(option)
            input_option = input("Enter a Option:")
            if input_option == 'a':
                display_province()
                insert_district()

            elif input_option == 'b':
                print('\nAvailable districts')
                display_district()
                update_district()

            elif input_option == 'c':
                display_district()
                delete_district()

            elif input_option == 'd':
                continue

        elif input_option == 3:
            print('#######################################');
            print("Municipality Options")
            for option in inner_option:
                print(option)
            input_option = input("Enter a Option:")
            if input_option == 'a':
                display_district()
                insert_municipality()

            elif input_option == 'b':
                print('\nAvailable municipalities')
                display_municipality()
                update_municipality()

            elif input_option == 'c':
                display_municipality()
                delete_municipality()

            elif input_option == 'd':
                continue

        elif input_option == 4:
            print("All provinces")
            display_province()
            display_province_district()

        elif input_option == 5:
            print('All districts')
            display_district()
            display_district_municipality()

        elif input_option == 6:
            exit()

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()

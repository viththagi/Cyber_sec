import sys
import mysql.connector

if len(sys.argv) != 2:
    print('Syntax: python sqltest.py <userid>')
else:
    mydb = mysql.connector.connect(
        user='root',
        password='root',
        host='127.0.0.1',
        database='PiDB'
    )

    mycursor = mydb.cursor()


    get_data = 'SELECT * FROM Customers WHERE userid="%s"' % (sys.argv[1])

    print('Your query: ' + get_data)
    print('Results:\n')

    mycursor.execute(get_data)

    results = mycursor.fetchall()

    for row in results:
        if len(row) == 4:
            print('[' + row[3] + ']', row[0] + '/' + row[1], row[2])
        else:
            print(row[0])

    print('------------------------------')
    mydb.close()

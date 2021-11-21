import psycopg2

try:
    ps_connection = psycopg2.connect(user="postgres",
                                     password="root",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="as1_db")

    cursor = ps_connection.cursor()

    # call stored procedure
    cursor.callproc('sagar_return_dep_people', [input("")])

    print("fechting Employee details who pushed changes to the production from function")
    result = cursor.fetchall()
    print(result)

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    if ps_connection:
        cursor.close()
        ps_connection.close()
        print("PostgreSQL connection is closed")

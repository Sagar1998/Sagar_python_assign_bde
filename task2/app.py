import psycopg2
from flask import Flask
from flask_restful import Resource, Api, reqparse
def sagar(key1):
    try:
        ps_connection = psycopg2.connect(user="postgres",
                                         password="root",
                                         host="127.0.0.1",
                                         port="5432",
                                         database="as1_db")

        cursor = ps_connection.cursor()

        # call stored procedure
        cursor.callproc('sagar_return_dep_people', [key1])

        print("fechting Employee details who pushed changes to the production from function")
        result = cursor.fetchall()
        return {"data":result}

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")
            


app = Flask(__name__)
api = Api(app)

class BarAPI(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('key1', type=str)
        args=parser.parse_args()

        return sagar(args.get('key1'))

api.add_resource(BarAPI, '/bar', endpoint='bar')

if __name__ == '__main__':
    app.run(debug=True)

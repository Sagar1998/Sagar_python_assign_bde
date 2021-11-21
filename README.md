# SAGAR KUVAR

Welcome to my Tasks for intenrship
## Installation

Download [PGAdmin4](https://www.pgadmin.org/download/) and install latest version.

```bash
pip install -r requirements.txt
```
# TASK1

##PgAdmin4

- Install pgadmin4 , use password as root and open it.
- after opening it you need to create a database you can do it by simply rightclicking on database , create new DB and name the DB as "as1_db"

![PGADMIN DB CREATE](/images/github-logo.png)

- After this you need to create new schema, right click on schema and create a new schema and name it as "test_sch"

![PGADMIN SCHEMA CREATE](/images/github-logo.png)


- now schema is created , you need to create a new table, simply copy this script below

```python

create table test_sch."apollo_org_job_function"(
organization_id varchar,
department varchar,
people int
);

```

- now download the csv file [here](https://drive.google.com/file/d/1jjv1ofJUzRjUiLcje3UhdbMfFCs7SHZI/view)

- after downloading csv file move it to D drive only eg D:/files
- after doing this , simple copy this query to load csv into table

```python
COPY persons(organization, department, people)
FROM 'D:\file\apollo_org_job_function.csv'
DELIMITER ','
CSV HEADER;
```

- now this is done write the following query in new file and run it

##SQL Query
```python
#FUNCTION
CREATE OR REPLACE FUNCTION sagar_return_dep_people (strr text)
RETURNS text
LANGUAGE sql AS
SELECT array_agg(concat( department, ':',people ))
as "dep_people" FROM  test_sch."apollo_org_job_function"
WHERE  organization_id LIKE '_______' || strr || '%' and people > 0  
$func$;
END; $$
#strr is the organization id
select * from sagar_return_dep_people(('2a'));
#/* 2a is example here we haven't used the actual user parameters.
```
##OUTPUT
![Output of PGADMIN](/images/github-logo.png)


#Python Code
```python
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

```
- input give a input like 1a , 2a ,3a ect

OUTPUT

![PYTHON CODE OUTPUT](/images/github-logo.png)


# TASK 2

- Now we have to make an API with the help of FLASK
- open simply paste this code

```python
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

```

- while checking output just make sure to add this after openning http://127.0.0.1:5000 that is

- add /bar?key1="anything" for example in our case we added  /bar?key1=1a

- output is as follows

![PYTHON CODE FLASK OUTPUT](/images/github-logo.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

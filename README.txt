ALTANA CODE REVIEW 

There are two files in package:
1. altana.py - command line tool that takes in as argument the csv file to be imported and added into datastore (Postgreqsql DB in this case)
2. api2.py - Provides APIs for the following:
- All operators associated with a given company
- All companies associated with a given operator
- All companies connected to a given company via shared operators

PRE-REQS:
- Python (3.9)
- PostGresQL
- Pandas
- Sqlalchemy
- Flask

altana.py can be run as "python altana.py <args>"
- Arguments accepted are a file path to csv file
Creates a datastore called altana-db in Postgresql

api2.py can be run as "python api2.py" - flask engine starts.
- http://127.0.0.1:5000/api/operators/company=? for All operators associated with a given company
- http://127.0.0.1:5000/api/companies/operator=? for All companies associated with a given operator
- http://127.0.0.1:5000/api/connected-companies/company=? for All companies connected to a given company via shared operators

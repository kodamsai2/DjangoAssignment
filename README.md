# DjangoAssignment

Django - For Python Web Framework  
PostgreSQL - For Database
Graphene - For GraphQL

step - 1
  In postgres(pgAdmin), create new database name "indian_banks" with username and password.

  In psql(SQL Shell), connect to the 'indian_banks' database 
  
    Run the below command to execute sql file.
 
    \i  /<file address>/indian_banks.sql
    
step - 2

  In CMD, cd to project directory
  
  To run the Django project
    
    python manage.py runserver 
 
  For graphql call's
    
    http://127.0.0.1:8000/gql
    
    query{

        branches{

                branch

                ifsc

        }  

      }

# DjangoAssignment

Django - For Python Web Framework   
PostgreSQL - For Database  
Graphene - For GraphQL  

1 - Created a django project(Banks)  
2 - Created a database in postgres(indian_banks.sql), and executed the sql file  
3 - Installed psycopg2 in django project, To operate with postgres and Edited the DATABASES in setting.py to postgres   
4 - Created a Django app(BanksAPI), generated & save Django model using below command    
           python manage.py inspectdb > models.py    
5 -  Installed graphene in django project, created a schema.py in django app and edited the file, In urls.py add the path "gql" for graphQl calls   


step - 1  

  In postgres(pgAdmin), create new database name "indian_banks" with username and   password. 
 
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

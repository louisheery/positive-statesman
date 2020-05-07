# The Positive Statesman
"Sharing 'Positive' Stories using sentiment analysis"

![Positive Statesman_LOGO](https://github.com/louisheery/positive-statesman/raw/master/file_dump/Positive%20Statesman%20Banner%20Logo.png)

![Positive Statesman](https://github.com/louisheery/positive-statesman/raw/master/file_dump/ps-homepage.png)


## How to Run the Positive Statesman
1. Clone the Repository
```
$ git clone https://github.com/louisheery/positive-statesman.git
```

2. Run Backend -- CD into correct folder and Run Django server
```
cd /<containing-folder>/positive-statesman/
python3 manage.py runserver
```
3. Run Frontend -- Run yarn dev to automatically compile the frontend with webpack
```
yarn dev
```

4. Open Project in Web Browser
Server is now running at *localhost:8000*



## Database Inspection & Troubleshooting
### How to inspect the database on django admin
1. All django database models are stored in <articles>/models.py

2. Create your superuser account
```
python3 manage.py createsuperuser
```

3. Start server (see How to run server)

4. open http://localhost:8000/admin/

5. You can now add data to the database manually

### How to inspect the database on pgAdmin 4 (Advanced)
1. All django database models are stored in <articles>/models.py

2. Download and install pgAdmin 4 on your machine if you want to inspect the database layout.
   (Download available at
   https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v4.17/macos/pgadmin4-4.17.dmg)

3. Open pgAdmin, which will launch a server and open a window in your browser.

4. Create new server by right clicking on servers (enter the following details:
    General
        Name: positive
    
    Connection
        Host: positive-db.postgres.database.azure.com
        Port: 5432
        Maintenance database: postgres
        Username: positive@positive-db
        Password: #4Flapjacks
    )

5. It will probably not allow you to connect, because your IP Address is not
   registered on Azure. So copy the IP Address you see in the error message and
   go to the Connection Security tab of the postive-db in Azure
   https://portal.azure.com/?Microsoft_Azure_Education_correlationId=a5b28028-31c4-4c7d-ac99-513592a5f536&Microsoft_Azure_Education_newA4E=true#@ImperialLondon.onmicrosoft.com/resource/subscriptions/57ac705c-2e64-40d5-ae70-4dee04d00caa/resourceGroups/positive-statesman/providers/Microsoft.DBforPostgreSQL/servers/positive-db/connectionSecurity
   (not sure if this link works for you, but you can give it a try)
   Then add your IP address and don't forget to press save

6. Now go back to the pgAdmin page and try to connect again.

7. Now you should have access to the server. On the server are 4 different
   databases. The one of interest is the "positive" database. By clicking on
   positive/schemas/tables you can find all tables in the database.

8. Please don't delete anything!!!

### How to seed database with categories
Navigate to the root directory and run the following command 
```
python manage.py seed_categories
```

### How to reset database
*Step 1*: go into the articles/migrations folders and delete all migrations (not the __init__.py and the other special file)
*Step 2*: delete db.sqlite
*Step 3*: run the following commands
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py seed_categories
*Step 4*: go to endpoint /api/fetch-articles

### How to print an ER-Diagram

1. Install: brew install graphviz

2. Execute: python3 manage.py graph_models articles -o file_dump/diagrams/er_diagram_`date "+%Y%m%d-%H%M%S"`.svg

3. You can now find the svg file in file_dump/diagrams/

### If there are any errors running yarn watch
1. You may need to update yarn (npm) packages

```
yarn install
```

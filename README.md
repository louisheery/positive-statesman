# The Positive Statesman
"Sharing 'Positive' Stories using sentiment analysis"

![Positive Statesman](https://raw.githubusercontent.com/louisheery/positive-statesman/master/file_dump/Positive%20Statesman%20Banner%20Logo.png?token=ADUEJK6FUP3XRTBJZ7DZKC26VAJMG)


![Positive Statesman](https://github.com/louisheery/positive-statesman/raw/master/file_dump/ps-homepage.png)

## Git Tutorial
## How to Push Code to Github
1. Update your 'Local' version of 'Master' Branch
```
git pull origin master
```

2. Create a new 'Local' version of a seperate Branch for which you are currently working on i.e. 'adding-react-router' Branch
```
git checkout -b adding-react-router
```

3. Push your 'adding-react-router' Branch to the 'Online' version. This automatically creates a pull request for 'adding-react-router' on Online version to be merged into 'Master' on Online version.
```
git push origin adding-react-router
```

4. Someone else will review the pull request and merge it to the Master of Online version at some point in the future.

5. And run a cleanup to delete this temporary 'adding-react-router' from the Local machine (this can only be done once the branch is merged)
```
git sweep
```

## How to run server
1. Start the server
```
python3 manage.py runserver
```

Server is now running at localhost:8000/

### If there are any errors running server do the following

1. Activate the correct python environment
```
source env/bin/activate
```

2. Install any missing requirements
```
pip3 install -r requirements.txt
```

## How to automatically compile frontend code as you work
1. Run yarn dev to automatically compile the frontend with webpack
```
yarn dev
```

### If there are any errors running yarn watch
1. You may need to update yarn (npm) packages

```
yarn install
```

## How to read and write to database

1. See https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

2. I didn't have a look at how to access it through the API yet

## How to inspect the database on django admin
1. All django database models are stored in <articles>/models.py

2. Create your superuser account
```
python3 manage.py createsuperuser
```

3. Start server (see How to run server)

4. open http://localhost:8000/admin/

5. You can now add data to the database manually

## How to inspect the database on pgAdmin 4 (Advanced)
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

## How to seed database with categories
Navigate to the root directory and run the following command 
```
python manage.py seed_categories
```

## How to reset database
*Step 1*: go into the articles/migrations folders and delete all migrations (not the __init__.py and the other special file)
*Step 2*: delete db.sqlite
*Step 3*: run the following commands
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py seed_categories
*Step 4*: go to endpoint /api/fetch-articles

## How to print an ER-Diagram

1. Install: brew install graphviz

2. Execute: python3 manage.py graph_models articles -o file_dump/diagrams/er_diagram_`date "+%Y%m%d-%H%M%S"`.svg

3. You can now find the svg file in file_dump/diagrams/
## Repo Contents

### Libraries and Technologies to research
- NLP: NLP Toolkit, Bert, Vader, Google BERT
- NLP Datasets [Google Dataset Search](https://toolbox.google.com/datasetsearch/search?query=positive%20sentiment)
- Backend Hosting:
- Backend Libraries: Django
- Frontend: React
- Hosting: Azure
- News APIs: TheGuardian, NewsAPI, Aylien
- Project Management: Slack, Trello, Basecamp

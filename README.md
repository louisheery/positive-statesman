# The Positive Statesman
"Sharing 'Positive' Stories using sentiment analysis"

![Positive Statesman_LOGO](https://github.com/louisheery/positive-statesman/raw/master/file_dump/Positive%20Statesman%20Banner%20Logo.png)

![Positive Statesman](https://github.com/louisheery/positive-statesman/raw/master/file_dump/ps-homepage.png)


## Before you run the Positive Statesman locally for the first time
1. Clone the Repository
```
$ git clone https://github.com/louisheery/positive-statesman.git
```

2. cd into the repository
```
cd /<containing-folder>/positive-statesman/
```

3. Install python requirements
```
pip3 install -r requirements.txt
```

4. Install JavaScript packages
```
yarn install
```

5. Apply database migrations to local SQLite database
```
python3 manage.py migrate --fake-initial
python3 manage.py makemigrations
python3 manage.py migrate
```

6. Seed categories
```
python3 manage.py seed_categories
```

## How to run the Positive Statesman

1. Start a local server
```
python3 manage.py runserver
```

2. The server is now running at http://127.0.0.1:8000/. Opening it in a
   browser will show you the web application

## How to fill the local SQLite database with new articles

1. Fetch 100 articles from Alyien API (this might take a few minutes)
```
python3 manage.py generate_articles
```

## How to inspect the local SQLite database

1. All django database models are stored in articles/models.py

2. Create your superuser account
```
python3 manage.py createsuperuser
```

3. Start a local server (See "How to run the Positive Statesman")

4. Go to http://127.0.0.1:8000/admin and login with your previously created 
   superuser account


## How to run frontend in developer mode (showing changes directly in browser)

1. Run frontend in developer mode
```
yarn dev
```

## How to run frontend testing framework

1. Run jest
```
yarn jest --coverage
```

2. Inspect coverage report in console or HTML version in coverage/lcov-report/index.html

## How to print an ER-Diagram

1. Install the graphviz package
```
brew install graphviz
```

2. Print ER-Diagram
```
python3 manage.py graph_models articles -o file_dump/diagrams/er_diagram_`date "+%Y%m%d-%H%M%S"`.svg
```

3. You can now find the svg file in file_dump/diagrams/

## Directory structure

The React frontend can be found in frontend/src/

# The Positive Statesman
GitHub Repo for MSc Group Project: "Sharing 'Positive' Stories using sentiment analysis"

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

## Repo Contents

### Libraries and Technologies to research
- NLP: NLP Toolkit, Bert, Vadar, Google BERT
- NLP Datasets [Google Dataset Search](https://toolbox.google.com/datasetsearch/search?query=positive%20sentiment)
- Backend Hosting:
- Backend Libraries: Django
- Frontend: React
- Hosting: Azure
- News APIs: TheGuardian, NewsAPI, Aylien
- Project Management: Slack, Trello, Basecamp

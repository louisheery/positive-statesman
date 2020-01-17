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

## Quickstart for Azure CLI
### Only required once
1. Install the Azure CLI
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest

2. Login to Azure CLI
```
az login
```

3. Create an Azure CLI deployment user
Items wrapped in '<' and '>' need to be replaced with your choices
If your password uses special characters wrap it within quotes as such 'password'
```
az webapp deployment user set --user-name <username> --password <password>
```

## How to add Azure remotes
### Only required once
1. Add the frontend remote
```
git remote add frontend https://positive-statesman.scm.azurewebsites.net:443/positive-statesman.git
```

2. Add the backend remote
```
git remote add backend https://positive-statesman-api.scm.azurewebsites.net:443/positive-statesman-api.git
```

## How to Push Code to Azure
1. Update your 'Local' version of 'Master' Branch
```
git pull origin master
```

2. Make sure you are in the positive-statesman/ directory

3. Push the corresponding folder to the corresponding azure remote.

### Frontend
```
git subtree push --prefix frontend frontend master
```


### Backend
```
git subtree push --prefix backend backend master
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

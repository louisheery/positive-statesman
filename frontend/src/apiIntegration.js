async function fetchArticles(articleLimit = "", articleOffset = "", articleCategory = "", articleSentimentMin = "", articleSentimentMax = "", articlePublisher = "", ) {
  if (articleCategory != null) {
    articleCategory = "category=" + articleCategory;
  }

  if (articlePublisher != null) {
    articlePublisher = "publisher=" + articlePublisher;
  }

  if (articleLimit != null) {
    articleLimit = "&limit=" + articleLimit;
  }

  if (articleOffset != null) {
    articleOffset = "&offset=" + articleOffset;
  }

  if (articleSentimentMin != null) {
    articleSentimentMin = "&sentiment_score_min=" + articleSentimentMin;
  }

  if (articleSentimentMax != null) {
    articleSentimentMax = "&sentiment_score_max=" + articleSentimentMax;
  }
  //const response = await fetch(`/api/articles?${articleCategory}&${articlePublisher}&${articleLimit}&${articleOffset}&${articleSentimentMin}&${articleSentimentMax}`);
  const response = await fetch(`/api/articles/`)
  const articles = await response.json();
  return articles;
}

// MaxC: This is not optimal and needs to be changed to a POST method. We
// shouldn't be writing to the database on a GET request. A POST method does
// however require csrf token authentication and is therefore put on hold for the 
// moment  
async function userFeedback(pk, vote) {
  console.log("Vote Button pressed: pk=" + String(pk) + " & vote=" + vote)
  await fetch(`/api/user-feedback/${pk}/${vote}/`)
  /*fetch(`/api/user-feedback/1/1/`, {
    method: 'POST',
    body: JSON.stringify({ pk: pk, vote: vote })
  })*/
}

export { fetchArticles, userFeedback }
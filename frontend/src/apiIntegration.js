async function fetchArticles(articleLimit = "", articleOffset = "", articleCategory = "", articleSentimentMin = "", articleSentimentMax = "", articlePublisher = "",) {
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

export { fetchArticles }
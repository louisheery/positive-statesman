import Cookies from 'js-cookie';

async function getCsrfToken() {
  const csrftoken = Cookies.get('csrftoken');
  if (csrftoken) {
    return csrftoken;
  }

  const response = await fetch(`/csrf/`, {
    credentials: 'include',
  });
  const data = await response.json();
  return data.csrfToken;
}

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
  const response = await fetch(`/api/articles?${articleCategory}&${articlePublisher}&${articleLimit}&${articleOffset}&${articleSentimentMin}&${articleSentimentMax}`);
  const articles = await response.json();
  return articles;
}

async function postToBackend(endpoint, method, data) {
  const response = await fetch(`/api/${endpoint}/`, {
    method: method,
    headers: { 'X-CSRFToken': await getCsrfToken() },
    credentials: 'include',
    body: JSON.stringify(data),
  });
  const jsonResponse = await response.json();
  return jsonResponse;
}

export { getCsrfToken, fetchArticles, postToBackend }
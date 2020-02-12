const allowedParams = ['category', 'publisher', 'limit', 'offset', 'sentiment_score_min', 'sentiment_score_max'];

async function fetchArticles(params = {}) {
  let query = '/api/articles/';
  let first = true;
  allowedParams.forEach(param => {
    if (params[param]) {
      query += first ? '?' : '&'
      query += `${param}=${params[param]}` 
      first = false;
    }
  });
  
  const response = await fetch(query)
  const articles = response.json();
  return articles;
}

export { fetchArticles }
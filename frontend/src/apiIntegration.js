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

async function fetchArticles(fetchRequest, articleToReturn = "") {
    const response = await fetch(`/api/articles/${articleToReturn}`);
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
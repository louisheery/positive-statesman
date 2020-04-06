const allowedParams = ['category', 'publisher', 'limit', 'offset', 'sentiment_score_min', 'sentiment_score_max'];

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].replace(/^([\s]*)|([\s]*)$/g, '');
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

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

async function userFeedback(pk, vote) {
  console.log("Vote Button pressed: pk=" + String(pk) + " & vote=" + vote)
  var csrftoken = getCookie('csrftoken');

  fetch(`/api/user-feedback/`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ "pk": pk, "vote": vote })
  }).then((response) => {
    console.log(response);
    response.json().then((data) => {
      console.log(data);
    });
  });
}

async function addArticle(url) {
  console.log("User submitted url: " + String(url))
  var csrftoken = getCookie('csrftoken');

  fetch(`/api/submit-article/`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ "url": url })
  }).then((response) => {
    console.log(response);
    response.json().then((data) => {
      console.log(data);
    });
  });
}

async function searchArticle(input) {
  try {
    var response = await fetch(`/api/search-articles/?search=` + String(input), {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    return await response.json()
  } catch (err) {
    return null
  }
}

async function getTimeSeriesData(param, begin, end) {
  try {
    var response = await fetch(`/api/analytics/?param=` + String(param) + "&begin=" + String(begin) + "&end=" + String(end), {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    return await response.json()
  } catch (err) {
    return null
  }
}




export { fetchArticles, userFeedback, addArticle, searchArticle, getTimeSeriesData, getCookie }

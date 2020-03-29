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
  console.log("User searched for: " + String(input))
  var csrftoken = getCookie('csrftoken');
  return "searchResult"
  fetch(`/api/search/`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ "input": input })
  }).then((response) => {
    console.log(response);

    if (response.status !== 404) {
      throw new Error("Search request couldn't be resolved from API");
    } else {
      //response.json().then((data) => {
      //  console.log(data);
      //});
      return "This will be the search result"
    }
  });
}


export { fetchArticles, userFeedback, addArticle, searchArticle }
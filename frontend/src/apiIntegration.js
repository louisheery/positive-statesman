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

// MaxC: We definitely need a POST request here because we cannot attach a
// different URL to the URL which is used for the API fetch request. Who ever
// does this part should also change the userFeedback function above to a POST 
// request
async function addStory(url) {
  console.log("User submitted url: " + String(url))
  var csrftoken = getCookie('csrftoken');

  fetch(`/api/submit-article/`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({ "url": url})
  }).then((response) => {
    console.log(response);
    response.json().then((data) => {
        console.log(data);
    });
});
}

export { fetchArticles, userFeedback, addStory }
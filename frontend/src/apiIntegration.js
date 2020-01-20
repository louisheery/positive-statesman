import Cookies from 'js-cookie';

const API_HOST = process.env.REACT_APP_API_HOST;

async function getCsrfToken() {
    const csrftoken = Cookies.get('csrftoken');
    if (csrftoken) {
        return csrftoken;
    }

    const response = await fetch(`${API_HOST}/csrf/`, {
        credentials: 'include',
    });
    const data = await response.json();
    return data.csrfToken;
}


async function fetchArticles(fetchRequest, articleToReturn = "") {
    
    /*

    this.authTokenStore.get()
        .then(authToken => {
            return fetch(this.serverUrl + '/REST/search?searchTerms=' + text, {
                method: 'get',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                    'X-Client-Auth-Token': authToken
                }
            })
        })
        .then(this._checkStatus)
        .then(this._parseJSON)
        .then(serverGetSearchSuccess)
        .catch(serverGetSearchError);
*/
    // let articles = fetch(`${API_HOST}/articles`)
    // .then(r => r.json())
    // .then(data => return data);

    const response = await fetch(`${API_HOST}/articles/${articleToReturn}`);
    const articles = await response.json();
    // console.log(articles);
    return articles;

/*
var data
    fetch('http://localhost:8000/articles/')
        .then(response => {
            return response.json()
        })
        .then((data) => { (data ? data = JSON.parse(data) : data = {})})
        .catch((error) => {("ERROR")})
    console.log("HELLO", data)
    return data
    */
}


/*
const endpoint = 'http://example.com/php/phpGetPost.php';

fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify(data)
})
    .then((resp) => resp.json())
    .then(function (response) {
        console.info('fetch()', response);
        return response;
    });
*/

/*
fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
    .then(response => response.json())
    .then(rowArticles => this.setState({ rowArticles }));
*/

async function postToBackend(endpoint, method, data) {
    const response = await fetch(`${API_HOST}/${endpoint}/`, {
        method: method,
        headers: { 'X-CSRFToken': await getCsrfToken() },
        credentials: 'include',
        body: JSON.stringify(data),
    });
    const jsonResponse = await response.json();
    return jsonResponse;
}

export { getCsrfToken, fetchArticles, postToBackend }
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


async function loginUser(username, password) {
    console.log("User to be logged in -- Username: " + String(username) + " , Password: " + String(password))
    var csrftoken = getCookie('csrftoken');

    fetch(`/api/login/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ "username": username, "password": password })
    }).then((response) => {
        console.log(response);
        response.json().then((data) => {
            console.log(data);
        });
    });
}


// export { loginUser, logoutUser, signupUser }
export { loginUser }
import { LOGIN_TRUE, LOGIN_FALSE, LOGIN_PENDING, DATA_USER_CATEGORY, DATA_USER_PUBLISHER, DATA_ALL_CATEGORY, DATA_ALL_PUBLISHER } from '../states/states';

// Cookie Fetcher Function
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

// FUNCTION: Log in User with Credentials 'username' and 'password'
export const logIn = (username, password) => dispatch => {

    //var csrftoken = getCookie('csrftoken');

    dispatch({ type: LOGIN_PENDING});

    fetch(`/api/login/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "username": username, "password": password })
    })
        .then((response) => {
            if (response.status == 200) {
                localStorage.setItem("token", JSON.stringify("LOGGEDIN"));
                localStorage.setItem("expirationDate", new Date(new Date().getTime() + 3600 * 1000));
                dispatch({ type: LOGIN_TRUE });
        } else {
            dispatch({ type: LOGIN_FALSE });
        }}
        )
};

// FUNCTION: Log Out Current User
export const logOut = () => (dispatch, getState) => {

    dispatch({type: LOGIN_PENDING})

    fetch(`/api/logout/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: {}
    }).then((response) => {
            if (response.status == 200) {
                localStorage.removeItem("token");
                localStorage.removeItem("expirationDate");
                dispatch({ type: LOGIN_FALSE });
            }
        }).catch((response) => {
            dispatch({ type: LOGIN_TRUE });
        });
};


// FUNCTION: Signup in User with Credentials 'username' and 'email' and 'password'
export const signupUser = (username, email, password) => dispatch => {

    //var csrftoken = getCookie('csrftoken');

    dispatch({ type: LOGIN_PENDING});

    fetch(`/api/signup/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password })
    })
        .then((response) => {
            if (response.status == 200) {
                localStorage.setItem("token", "LOGGEDIN");
                localStorage.setItem("expirationDate", new Date(new Date().getTime() + 3600 * 1000));
                dispatch({ type: LOGIN_TRUE });
            } else if (response.status == 404) {
                dispatch( { type: LOGIN_FALSE })
            }}
        ).catch(() => {
            dispatch({ type: LOGIN_FALSE });
        });

}


export const checkLoggedIn = () => dispatch => {

    if (localStorage.getItem("token") === undefined) {
        dispatch({ type: LOGIN_FALSE });
    } else {
        if (new Date(localStorage.getItem('expirationDate')) <= new Date() ) {
            dispatch( { type: LOGIN_FALSE });
        } else {
            dispatch ( {type: LOGIN_TRUE });

        }
    }
}




// FUNCTION: Edit User Preferences Data for User

export const userEditData = (requestType, dataType, dataId = null) => (dispatch, getState) => {

    var csrftoken = getCookie('csrftoken');

    fetch(`/api/popular/${dataType}/`, {
        method: requestType,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: requestType == 'GET' ? null : (dataType == 'category' ? JSON.stringify({ "id": dataId }) : JSON.stringify({ "name": dataId }))
    }).then((response) => {
        
        if (response.status == 200) {

            if (requestType == 'GET') {

                dispatch({ type: dataType == 'category' ? DATA_USER_CATEGORY : DATA_USER_PUBLISHER, payload: response.data, });
            } else {
                // ELSE: If was an ADD/DELETE Request
            }

        } else if (response.status == 500) {
            //dispatch({ type: LOGIN_FALSE })
        }

    }
    ).catch(() => {
    });

}


export const userFetchData = (requestType, dataType) => (dispatch, getState) => {
    getAsyncData(dispatch, getState, requestType, dataType)
}



async function getAsyncData(dispatch, getState, requestType, dataType) {
    try {
        var csrftoken = getCookie('csrftoken');

        const response = await fetch(`/api/popular/${dataType}/`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
        })
        
        let data = await response.json();
        var obj = data.info
        var result

        if (dataType == 'category') {
            result = Object.keys(obj).map(function (key) {
                return [obj[key]['id'], obj[key]['name'], obj[key]['tax_id']];
            });
        } else {
            result = Object.keys(obj).map(function (key) {
                return [obj[key]['name'], obj[key]['tax_id']];
            });
        }
        dispatch({ type: dataType == 'category' ? DATA_USER_CATEGORY : DATA_USER_PUBLISHER, payload: result });
        
    } catch (err) {
        console.log(err)
    }
}

// FUNCTION: Get All Possible Data for Categories/Publishers

export const avaliableData = (dataType) => (dispatch, getState) => {

    fetch(`/api/all/${dataType}/`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: {}
    }).then((response) => {
        if (response.status == 200) {
            dispatch({ type: dataType == 'category' ? DATA_ALL_CATEGORY : DATA_ALL_PUBLISHER, payload: response.data, });

        } else if (response.status == 500) {
            //dispatch({ type: LOGIN_FALSE })
        }
    }
    ).catch(() => {
        console.log("AUTHENTICATION ERROR for DATA");
    });

}
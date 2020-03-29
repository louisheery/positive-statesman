import axois from "axios";
import { ADD_CATEGORY_TRUE, DEL_CATEGORY_TRUE, ADD_PUBLISHER_TRUE, DEL_PUBLISHER_TRUE, ADD_CATEGORY_FALSE, DEL_CATEGORY_FALSE, ADD_PUBLISHER_FALSE, DEL_PUBLISHER_FALSE, LOGIN_TRUE, LOGIN_FALSE, SIGNUP_TRUE, SIGNUP_FALSE, LOGOUT_TRUE, DATA_LOADING, DATA_TRUE, AUTH_PROBLEM } from '../states/states';

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

    console.log("User to be logged in -- Username: " + String(username) + " , Password: " + String(password))

    var csrftoken = getCookie('csrftoken');
    
    axois.post(`/api/login`, JSON.stringify({ "username": username, "password": password }), {
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        }}).then((response) => {dispatch({
        type: LOGIN_TRUE,
        payload: response.data,
    });
    console.log("LOGGEDIN", response)
    }).catch((response) => {dispatch({type: LOGIN_FALSE,});
        console.log("NOTLOGGEDIN!!!")
    });
    
};

// FUNCTION: Log Out Current User
export const logOut = () => (dispatch, getState) => {

    console.log("User to be logged out")
    var csrftoken = getCookie('csrftoken');

    const header = {
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        }
    }

    if (getState().auth != null) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }

    axois.post(`/api/logout`, null, header).then(() => {
        dispatch({
            type: LOGOUT_TRUE,
        });
        console.log("LOGOUT TRUE");
    }).catch(() => {
        console.log("LOGOUT FALSE");
    });

};


// FUNCTION: Signup in User with Credentials 'username' and 'email' and 'password'
export const signupUser = (username, email, password) => dispatch => {

    var csrftoken = getCookie('csrftoken');

    axois.post(`/api/signup`, JSON.stringify({ 'username': username, 'email': email, 'password': password }), {
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        }
    }).then((response) => {
        dispatch({
            type: SIGNUP_TRUE,
            payload: response.data,
        });
        console.log("SUCCESS SIGNUP")
    }).catch(() => {
        dispatch({ type: SIGNUP_FALSE, });
        console.log("FAILED SIGNUP")
    });

}


// FUNCTION: Get User Preferences Data for User with Credentials 'username' and 'password'
export const getUserData = () => (dispatch, getState) => {

    console.log("User data being fetched");
    dispatch({ type: DATA_LOADING });

    const header = {
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    }

    if (getState().auth) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }
        
    axois.get(`/api/account/category`, header).then((response) => {
        dispatch({
            type: DATA_TRUE,
            payload: response.data,
        });

        console.log("JSONSNSN", response.data)
    }).catch((error) => {
        dispatch({ type: AUTH_PROBLEM, });
        console.log(error, "ERROR")
    });

};

// FUNCTION: Add to User Preferences Data for User with Credentials 'username' and 'password'
export const addUserData = () => (dispatch, getState, type, value) => {

    console.log("User data being added for type: ", type);
    dispatch({ type: DATA_LOADING });

    const header = {
        headers: {
            "Content-Type": "application/json"
        }
    }

    if (getState().auth != null) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }

    const url = `/api/account/` + type;

    axois.post(url, JSON.stringify({ 'id': value }), {
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        }
    }).then((response) => {
        dispatch({
            type: (type == 'category') ? ADD_CATEGORY_TRUE : ADD_PUBLISHER_TRUE,
        });
        console.log("SUCCESS ADD ", type)
    }).catch(() => {
        dispatch({
            type: (type == 'category') ? ADD_CATEGORY_FALSE : ADD_PUBLISHER_FALSE,
        });
        console.log("FAILED ADD", type)
    });

};

// FUNCTION: Delete from User Preferences Data for User with Credentials 'username' and 'password'
export const delUserData = () => (dispatch, getState, type, value) => {

    console.log("User data being added for type: ", type);
    dispatch({ type: DATA_LOADING });

    const header = {
        headers: {
            "Content-Type": "application/json"
        }
    }

    if (getState().auth != null) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }

    const url = `/api/account/` + type;

    axois.delete(url, JSON.stringify({ 'id': value }), {
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        }
    }).then((response) => {
        dispatch({
            type: (type == 'category') ? DEL_CATEGORY_TRUE : DEL_PUBLISHER_TRUE,
        });
        console.log("SUCCESS DEL ", type)
    }).catch(() => {
        dispatch({
            type: (type == 'category') ? DEL_CATEGORY_FALSE : DEL_PUBLISHER_FALSE,
        });
        console.log("FAILED DEL ", type)
    });

};
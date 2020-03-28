import axois from "axios";
import { LOGIN_TRUE, LOGIN_FALSE, SIGNUP_TRUE, SIGNUP_FALSE, LOGOUT_TRUE, DATA_LOADING, DATA_TRUE, AUTH_PROBLEM } from '../states/states';
import Axios from "axios";
// import getCookie from '../../apiIntegration';

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



export const getUserData = () => (dispatch, getState) => {

    console.log("User data being fetched");
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
        
    axois.get(`/api/account/category`, header).then((response) => {
        dispatch({
            type: DATA_TRUE,
            payload: response.data,
        });
    }).catch((error) => {
        dispatch({ type: AUTH_PROBLEM, });
        console.log(error, "ERROR")
    });

};
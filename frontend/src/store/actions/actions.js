// REACT LIBRARIES
import React, { Component } from 'react'
import ReactGA from "react-ga";
import axois from "axios";
import { withRouter, Redirect } from "react-router-dom";

import history from '../../components/history';

import { LOGIN_TRUE, LOGIN_FALSE, LOGIN_PENDING, LOGIN_DONE } from '../states/states';

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
                console.log("LOGGED11_a IN", response);
                //history.push("/"); // CHANGE THIS
        } else {
            dispatch({ type: LOGIN_FALSE });
            console.log("NOT-aLOGGEDIN");
        }}
        )
};

// FUNCTION: Log Out Current User
export const logOut = () => (dispatch, getState) => {

    console.log("User to be logged out")

    dispatch({type: LOGIN_PENDING})

    fetch(`/api/logout/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: {}
    }).then((response) => {
            if (response.data.status == 200) {
                localStorage.removeItem("token");
                localStorage.removeItem("expirationDate");
                dispatch({ type: LOGIN_FALSE });
                console.log("LOGGED OUT");
                history.push("/"); // CHANGE THIS
            }
        }).catch(() => {
            dispatch({ type: LOGIN_TRUE });
            console.log("LOGOUT OUT FALSE");
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
                console.log("SIGNUP TRUE; LOGIN TRUE", response);
                history.push("/"); // CHANGE THIS
            } else if (response.status == 401) {
                localStorage.removeItem("token");
                localStorage.removeItem("expirationDate");
                //dispatch({ type: SIGNUP_FALSE });
                dispatch( { type: LOGIN_FALSE })
                console.log("SIGNUP ERROR", response);
                history.push("/signup"); // CHANGE THIS
            }}
        ).catch(() => {
            dispatch({ type: LOGIN_FALSE });
            console.log("SIGNUP FALSE; LOGIN FALSE");
        });

}


export const checkLoggedIn = () => dispatch => {

    if (localStorage.getItem("token") === undefined) {
        dispatch({ type: LOGIN_FALSE });
        console.log("DISPATCH: LOGIN_FALSE1")
    } else {
        if (new Date(localStorage.getItem('expirationDate')) <= new Date() ) {
            dispatch( { type: LOGIN_FALSE });
            console.log("DISPATCH: LOGIN_FALSE2", localStorage.getItem('expirationDate'))
        } else {
            dispatch ( {type: LOGIN_TRUE });
            console.log("DISPATCH: LOGIN_TRUE999")

        }
    }
}




// FUNCTION: Get User Preferences Data for User with Credentials 'username' and 'password'
export const getUserData = () => (dispatch, getState) => {

    console.log("User data being fetched");
    //dispatch({ type: DATA_LOADING });
/*
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
        */
    axois.get(`/api/popular/category/`, getCSRF(getState)).then((response) => {
        //dispatch({type: DATA_TRUE,payload: response.data,});

        //console.log("JSONSNSN", response.data)
    }).catch(() => {
        // dispatch({ type: AUTH_PROBLEM, });
        //console.log(error, "ERROR")
    });

};

export const getCSRF = getState => {
    
    var token;

    if (getState().auth == null) {
        token = null;
    } else {
        token = getState().auth.token;
    }

    const config = {
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (token) {
        config.headers["Authorization"] = `Token ${token}`;
    }

    return config;
};

// FUNCTION: Add to User Preferences Data for User with Credentials 'username' and 'password'
export const addUserData = (type, value) => (dispatch, getState) => {
/*
    console.log("User data being added for type: ", type);
    dispatch({ type: DATA_LOADING });

    const header = {
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }

    if (getState().auth != null) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }

    const url = `/api/popular/` + type + `/`;

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
*/
};

// FUNCTION: Delete from User Preferences Data for User with Credentials 'username' and 'password'
export const delUserData = (type, value) => (dispatch, getState) => {
/*
    console.log("User data being added for type: ", type);
    dispatch({ type: DATA_LOADING });

    const header = {
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    }

    if (getState().auth != null) {
        const csrftoken = getState().auth.token;

        if (csrftoken) {
            header.headers['Authorization'] = `Token ${csrftoken}`;
        }
    }

    const url = `/api/popular/` + type + `/`;

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
*/
};
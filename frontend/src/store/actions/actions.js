// REACT LIBRARIES
import React, { Component } from 'react'
import ReactGA from "react-ga";
import axios from 'axios';
import { withRouter, Redirect } from "react-router-dom";

import { LOGIN_TRUE, LOGIN_FALSE, LOGIN_PENDING, LOGIN_DONE, DATA_USER_CATEGORY, DATA_USER_PUBLISHER, DATA_ALL_CATEGORY, DATA_ALL_PUBLISHER } from '../states/states';

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
            if (response.status == 200) {
                localStorage.removeItem("token");
                localStorage.removeItem("expirationDate");
                dispatch({ type: LOGIN_FALSE });
                console.log("LOGGED OUT");
            }
        }).catch((response) => {
            dispatch({ type: LOGIN_TRUE });
            console.log("LOGOUT OUT FALSE", response);
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
            } else if (response.status == 404) {
                dispatch( { type: LOGIN_FALSE })
                console.log("SIGNUP ERROR", response);
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




// FUNCTION: Get User Preferences Data for User

export const userData = (requestType, dataType, dataId = null) => (dispatch, getState) => {

    console.log("User data being fetched/edited");

    console.log("8888888", requestType, dataType, dataId, "888");

    var csrftoken = getCookie('csrftoken');

    fetch(`/api/popular/category/`, {
        method: requestType,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: requestType == 'GET' ? null : JSON.stringify({"id": dataId})
    }).then((response) => {

        console.log("DATA SUCCESS9990909", response);

        
        if (response.status == 200) {
            console.log("DATA SUCCESS", response);
            console.log("JASDHSAKDHSAKDJ", response.status);
            console.log("000", response.data)

            console.log("APPLE", requestType)
            if (requestType == 'GET') {
                
                console.log("66666666666");
                dispatch({ type: dataType == 'category' ? DATA_USER_CATEGORY : DATA_USER_PUBLISHER, payload: response.data, });
            } else {
                // ELSE: If was an ADD/DELETE Request
                // then GET Updated Dataset; and save to Redux Store.
                console.log("@@@");
                //this.userData('GET', dataType, null);
            }

        } else if (response.status == 500) {
            //dispatch({ type: LOGIN_FALSE })
            console.log("AUTHENTICATION ERROR for DATA", response);
        }

    }
    ).catch(() => {
        console.log("DATA ERROR");
    });

}


export const userGETData = (requestType, dataType) => (dispatch, getState) => {
    console.log("AA")
    getAsyncData(dispatch, getState, requestType, dataType)
}



async function getAsyncData(dispatch, getState, requestType, dataType) {
    try {
        var csrftoken = getCookie('csrftoken');

        const response = await fetch(`/api/popular/category/`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
        })
        
        
        let data = await response.json();
        var obj = data.info
        var result = Object.keys(obj).map(function (key) {
            return [obj[key]['id'], obj[key]['name'], obj[key]['tax_id']];
        });
        
        //.then((response) => response)
        //console.log("101", data.json(), "101")
        dispatch({ type: dataType == 'category' ? DATA_USER_CATEGORY : DATA_USER_PUBLISHER, payload: result });
        
    } catch (err) {
        console.log(err, "101")
    }
};
/*

export function userGETData (dispatch, requestType, dataType) {
    return async dispatch => {

    console.log("User data being fetched/editedwq890123901283");

    console.log("8888888", requestType, dataType, "888");


    try {

    var csrftoken = getCookie('csrftoken');

    const data = await fetch(`/api/popular/category/`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
    }).then((response) => response.data)

    console.log("ZZ", data)
    

        if (data.status == 200) {
            //console.log("11111DATA SUCCESS", data.json());
            console.log("11111JASDHSA123KDHSAKDJ", data.status);
            console.log("000", data.info)

                console.log("APPLE", requestType)
                if (requestType == 'GET') {

                    console.log("66666666666");
                    dispatch({ type: dataType == 'category' ? DATA_USER_CATEGORY : DATA_USER_PUBLISHER, payload: data.data, });
                } else {
                    // ELSE: If was an ADD/DELETE Request
                    // then GET Updated Dataset; and save to Redux Store.
                    console.log("@@@");
                    //this.userData('GET', dataType, null);
                }

        } else if (data.status == 500) {
                //dispatch({ type: LOGIN_FALSE })
            console.log("AUTHENTICATION ERROR for DATA", data);
            }

    } catch (error) {
        console.log("111DATA ERROR", error);
    }
}
}
*/
// FUNCTION: Get All Possible Data for Categories/Publishers

export const avaliableData = (dataType) => (dispatch, getState) => {

    console.log("User data being fetched/edited");

    fetch(`/api/all/` + dataType, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: {}
    }).then((response) => {
        if (response.status == 200) {
            console.log("DATA SUCCESS", response);
            dispatch({ type: dataType == 'category' ? DATA_ALL_CATEGORY : DATA_ALL_PUBLISHER, payload: response.data, });

        } else if (response.status == 500) {
            //dispatch({ type: LOGIN_FALSE })
            console.log("AUTHENTICATION ERROR for DATA", response);
        }
    }
    ).catch(() => {
        console.log("AUTHENTICATION ERROR for DATA");
    });

}
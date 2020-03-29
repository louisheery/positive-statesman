import { DATA_LOADING, DATA_TRUE, LOGOUT_TRUE, LOGIN_FALSE, LOGIN_TRUE, SIGNUP_TRUE, SIGNUP_FALSE, AUTH_PROBLEM, AUTH_TRUE, AUTH_WAITING } from '../states/states';
import { } from "../actions/actions";

const initialState = {
    token: localStorage.getItem("token"),
    account: null,
    isLoggedIn: false,
    isPending: false,
}


const reducer = (state = initialState, action) => {
    
    const newState = {...state};

    switch(action.type) {
        case LOGIN_TRUE:
        case SIGNUP_TRUE:
            localStorage.setItem("token", action.payload.token);
            newState.isLoggedIn = true;
            newState.isPending = false;
            break;

        case AUTH_WAITING:
            newState.isPending = true;
            break;

        case AUTH_TRUE:
            newState.isPending = false;
            newState.isLoggedIn = true;
            newState.account = action.payload;
            break;

        case AUTH_PROBLEM:
        case LOGIN_FALSE:
        case LOGOUT_TRUE:
        case SIGNUP_FALSE:
            localStorage.removeItem("token");
            newState.token = null;
            newState.account = null;
            newState.isLoggedIn = false;
            newState.isPending = false;
            break;

        case DATA_LOADING:
            newState.isPending = true;
            break;

        case DATA_TRUE:
            newState.isPending = false;
            newState.isLoggedIn = true;
            newState.account = action.payload;
            break;

        default:
            break;
    }

    return newState;
}

export default reducer;
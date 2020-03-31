import { LOGIN_TRUE, LOGIN_FALSE } from '../states/states';
import { } from "../actions/actions";

const initialState = {
    isLoggedIn: null,
}


export default function(state = initialState, action) {

    switch(action.type) {
        case LOGIN_TRUE:
            return {
                ...state,
                isLoggedIn: true
            };

        case LOGIN_FALSE:
            return {
                ...state,
                isLoggedIn: false
            };

        default:
            return state;
    }
}
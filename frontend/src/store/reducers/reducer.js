import { LOGIN_TRUE, LOGIN_FALSE, DATA_USER_CATEGORY, DATA_USER_PUBLISHER, DATA_ALL_CATEGORY, DATA_ALL_PUBLISHER } from '../states/states';
import { } from "../actions/actions";

const initialState = {
    isLoggedIn: null,
    allCategories: null,
    allPublishers: null,
    userCategories: null,
    userPublishers: null,
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

        case DATA_USER_CATEGORY:
            return {
                ...state,
                userCategories: action.payload

            };

        case DATA_USER_PUBLISHER:
            return {
                ...state,
                userPublishers: action.payload
            }

        case DATA_ALL_CATEGORY:
            return {
                ...state,
                allCategories: action.payload
            }

        case DATA_ALL_PUBLISHER:
            return {
                ...state,
                allPublishers: action.payload
            }

        default:
            return state;
    }
}
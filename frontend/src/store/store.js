// Redux Imports
import reducer from './reducers/reducer';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';

// Redux Store
const initialState = {};
const store = createStore(reducer, initialState, composeWithDevTools(applyMiddleware(thunk)));

export default store;
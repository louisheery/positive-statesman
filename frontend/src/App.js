import React from 'react';
import Root from './components/Root.js'
import ReactGA from "react-ga";


// REDUX LIBRARIES
import reducer from './store/reducers/reducer';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import store from "./store/store";
import { getUserData } from './store/actions/actions';

class App extends React.Component {

  componentDidMount() {
    ReactGA.initialize('UA-158792560-1');
    store.dispatch(getUserData());
  }

  render() {
    return (
      <Provider store={store}>
        <Root />
      </Provider>
    )
  }
}

export default App;
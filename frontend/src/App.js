import React from 'react';
import Root from './components/Root.js'
import ReactGA from "react-ga";

class App extends React.Component {

  componentDidMount() {
    ReactGA.initialize('UA-158792560-1');
  }

  render() {
    return (
      <Root />
    )
  }
}

export default App;
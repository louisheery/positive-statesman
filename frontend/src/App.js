import React from 'react';
import HeaderBar from './components/HeaderBar';
import NewsFeed from './components/NewsFeed';
import './App.css';

class App extends React.Component {

  state = {
  }

  render() {
    return (
      <div>
        <HeaderBar />
        <NewsFeed />
      </div>
    )
  }
}

export default App;
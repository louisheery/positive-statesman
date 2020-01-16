import React from 'react';
import HeaderBar from './components/HeaderBar';
import NewsFeed from './components/NewsFeed';
import './App.css';
import AddArticlePopup from './components/AddArticlePopup';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.handleArticlePopupOpening = this.handleArticlePopupOpening.bind(this);
    this.state = {
      addArticlePopupIsOpen: false,
    };
  }

  handleArticlePopupOpening() {
    this.setState({addArticlePopupIsOpen: !this.state.addArticlePopupIsOpen})
  }

  render() {
    return (
      <div>
        <HeaderBar addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
        <NewsFeed addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />
        <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
      </div>
    )
  }
}

export default App;
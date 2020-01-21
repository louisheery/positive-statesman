// REACT LIBRARIES
import React from 'react';


// REACT COMPONENTS
import NewsFeed from '../articles/NewsFeed';
import NewsTickerBar from '../headers/NewsTickerBar'
import AddArticlePopup from '../popups/AddArticlePopup';

// STYLE

import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import GoogleButton from 'react-google-button';

// API
import { fetchArticles } from '../../apiIntegration';



class Home extends React.Component {

  constructor(props) {
    super(props);
    this.handleArticlePopupOpening = this.handleArticlePopupOpening.bind(this);
    this.state = {
      addArticlePopupIsOpen: false,
      userIsLoggedIn: false,
      loginPageDisplayed: false,
    };
  }

  handleArticlePopupOpening() {
    this.setState({ addArticlePopupIsOpen: !this.state.addArticlePopupIsOpen })
  }

  render() {
    return (
      <div>
        <NewsTickerBar />
        <NewsFeed addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />
        <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
      </div>
    )
  }
}

export default Home;

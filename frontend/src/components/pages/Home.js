// REACT LIBRARIES
import React from 'react';


// REACT COMPONENTS
import NewsFeed from '../articles/NewsFeed';
import NewsTickerBar from '../headers/NewsTickerBar'
import AddArticlePopup from '../popups/AddArticlePopup';

// STYLE


import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/pages/Home.js';

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

    const { classes } = this.props;
    
    return (
      <div>
        <NewsTickerBar />
        <NewsFeed addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />
        <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
      </div>
    )
  }
}

export default withStyles(styles)(Home)

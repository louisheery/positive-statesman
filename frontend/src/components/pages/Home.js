// REACT LIBRARIES
import React from 'react';

// REACT COMPONENTS
import NewsFeedOld from '../articles/NewsFeedOld';
import NewsFeed from '../articles/NewsFeed';
import NewsTickerBar from '../headers/NewsTickerBar'
import AddArticlePopup from '../popups/AddArticlePopup';

// STYLE
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Home.js';
import NewsFeedTop from '../articles/NewsFeedTop';
import Hidden from '@material-ui/core/Hidden';

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
        <Hidden only={['xs', 'sm']}>
          <NewsTickerBar />
        </Hidden>
        <Hidden only={['md', 'lg', 'xl']}>
          <div style={{ height: '160px' }}></div>
        </Hidden>

        <NewsFeed />
        {/*<NewsFeedOld addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />*/}
        <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
      </div>
    )
  }
}

export default withStyles(styles)(Home)

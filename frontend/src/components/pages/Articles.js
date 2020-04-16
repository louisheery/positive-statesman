// REACT LIBRARIES
import React, { Component } from 'react';
import ReactGA from "react-ga";

// INTERNAL REACT COMPONENTS
import NewsFeed from '../newsfeed/NewsFeed';
// import NewsTickerBar from '../headers/NewsTickerBar'

// EXTERNAL REACT LIBRARIES & COMPONENTS
// import Hidden from '@material-ui/core/Hidden';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/pages/Articles.js';

class ArticlePage extends Component {
  
  componentDidMount() {
    ReactGA.pageview(`${this.props.pageName}`);
  }

  render() {
    const { classes } = this.props;
    return (
      <div>
        {/* News Ticker Bar is hidden until it is linked to API */}
        {/*
        <Hidden only={['xs', 'sm']}>
          <NewsTickerBar />
        </Hidden>
        <Hidden only={['md', 'lg', 'xl']}>
          <div className={classes.mainDiv}></div>
        </Hidden>
                <div className={classes.mainPadding}></div>
        */}        

        <NewsFeed pageName={this.props.pageName} categoryId={this.props.categoryId} publisherId={this.props.publisherId} />
      </div>
    )
  }
}

export default withStyles(styles)(ArticlePage)

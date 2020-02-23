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
import styles from '../../../src/assets/styles/components/pages/Category.js';

class Category extends Component {
  
  componentDidMount() {
    ReactGA.pageview(`${this.props.categoryName}`);
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
        */}
        <div className={classes.mainPadding}></div>
        <NewsFeed categoryName={this.props.categoryName} categoryId={this.props.categoryId} />
      </div>
    )
  }
}

export default withStyles(styles)(Category)

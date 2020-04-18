// REACT LIBRARIES
import React, { Component } from 'react'
import ReactGA from "react-ga";

// INTERNAL REACT COMPONENTS
import NewsFeed from '../newsfeed/NewsFeed'
// import NewsTickerBar from '../headers/NewsTickerBar'

// REDUX LIBRARIES
import reducer from '../../store/reducers/reducer';
import { Provider } from 'react-redux';
import { getUserData } from '../../store/actions/actions';

// EXTERNAL REACT LIBRARIES & COMPONENTS
// import Hidden from '@material-ui/core/Hidden';

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Home.js'


class Home extends Component {

  componentDidMount() {
    ReactGA.pageview(`homepage`);
    //store.dispatch(getUserData());
  }

  render() {
    return (
      <div>
        {/* News Ticker Bar is being hidden until it is linked to API */}
        {/*
        <Hidden only={['xs', 'sm']}>
          <NewsTickerBar />
        </Hidden>
        <Hidden only={['md', 'lg', 'xl']}>
          <div className={classes.mainDiv}></div>
        </Hidden>
        */}
        <NewsFeed categoryName={this.props.categoryName} categoryId={this.props.categoryId} />
      </div>
    )
  }
}

export default withStyles(styles)(Home)

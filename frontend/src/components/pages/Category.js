// REACT LIBRARIES
import React, { Component } from 'react';

// INTERNAL REACT COMPONENTS
import NewsFeedCategory from '../newsfeed/NewsFeedCategory';
// import NewsTickerBar from '../headers/NewsTickerBar'

// EXTERNAL REACT LIBRARIES & COMPONENTS
// import Hidden from '@material-ui/core/Hidden';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Category.js';

class Category extends Component {


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
                <NewsFeedCategory categoryName={this.props.categoryName} categoryId={this.props.categoryId} />
                <p></p>
            </div>
        )
    }
}

export default withStyles(styles)(Category)

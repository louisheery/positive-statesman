import React, { Component } from 'react';
import NewsFeedCategory from '../articles/NewsFeedCategory';
import NewsTickerBar from '../headers/NewsTickerBar'

import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/pages/Category.js';
import Hidden from '@material-ui/core/Hidden';

class Category extends Component {


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

                <NewsFeedCategory />

            </div>
        )
    }
}

export default withStyles(styles)(Category)

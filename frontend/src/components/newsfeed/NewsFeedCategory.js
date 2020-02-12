// REACT LIBRARIES
import React, { Component } from 'react';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeedCategory.js';

const newsFeedDictionary = {
    QUERY_TODAY: ['', 'Trending Today', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_THISWEEK: ['', 'Trending This Week', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_THISMONTH: ['', 'Trending This Month', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ALLTIME: ['', 'Trending All Time', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_USA: ['', 'Trending in USA', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_UK: ['', 'Trending in UK', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_WORLD: ['', 'Trending Worldwide', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
}



class NewsFeedCategory extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_TODAY, newsFeedDictionary.QUERY_THISWEEK, newsFeedDictionary.QUERY_THISMONTH, newsFeedDictionary.QUERY_ALLTIME, newsFeedDictionary.QUERY_USA, newsFeedDictionary.QUERY_UK, newsFeedDictionary.QUERY_WORLD,],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            <div className={classes.grid}>

                <NewsFeedHeader />
                {/* Maps each of the Items in homeScreenNewsFeedRows array to Component instances */}
                {
                    this.state.homeScreenNewsFeedRows.map((newsFeedRow, i) => {
                        return (
                            <NewsFeedRow key={Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowFetchData={newsFeedRow[2]} />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeedCategory)
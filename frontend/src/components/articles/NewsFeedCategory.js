import React, { Component } from 'react';
import NewsFeedRow from './NewsFeedRow';
import NewsFeedTop from '../articles/NewsFeedTop';
import { withStyles } from '@material-ui/core/styles';

import styles from '../../assets/styles/components/articles/NewsFeedCategory.js';

const newsFeedDictionary = {
    QUERY_TODAY: ['', 'Trending Today'],
    QUERY_THISWEEK: ['art', 'Trending This Week'],
    QUERY_THISMONTH: ['crime', 'Trending This Month'],
    QUERY_ALLTIME: ['disaster', 'Trending All Time'],
    QUERY_USA: ['economics', 'Trending in USA'],
    QUERY_UK: ['education', 'Trending in UK'],
    QUERY_WORLD: ['environment', 'Trending Worldwide'],
}



class NewsFeedNew extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_TODAY, newsFeedDictionary.QUERY_THISWEEK, newsFeedDictionary.QUERY_THISMONTH, newsFeedDictionary.QUERY_ALLTIME, newsFeedDictionary.QUERY_USA, newsFeedDictionary.QUERY_UK, newsFeedDictionary.QUERY_WORLD, ],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            // NewsFeed = ClassName
            <div className={classes.grid}>
                
                <NewsFeedTop />
                {
                    this.state.homeScreenNewsFeedRows.map((newsFeedRow, i) => {
                        return (
                            <NewsFeedRow key={newsFeedRow[0] + Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowColor={{backgroundColor: 'white'}}  />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeedNew)
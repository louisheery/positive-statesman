// REACT LIBRARIES
import React, { Component } from 'react';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeed.js';


class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            newsFeedDictionary: {
                QUERY_TODAY: ['', 'Trending Today', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_THISWEEK: ['', 'Trending This Week', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_THISMONTH: ['', 'Trending This Month', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_ALLTIME: ['', 'Trending All Time', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_USA: ['', 'Trending in USA', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_UK: ['', 'Trending in UK', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_WORLD: ['', 'Trending Worldwide', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],

                QUERY_ARTARTICLES: ['/art', 'Art, Culture & Entertainment', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_BUSINESSARTICLES: ['/business', 'Business', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_POLITICSARTICLES: ['/politics', 'Law, Government & Politics', {limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_SCIENCEARTICLES: ['/science', 'Science', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_SPORTARTICLES: ['/sport', 'Sport', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_TECHARTICLES: ['/tech', 'Technology', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_TRAVELARTICLES: ['/travel', 'Travel', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
            },
        }

        if (this.props.categoryId === '') {
            this.childState = {
                newsFeedRow: [this.state.newsFeedDictionary.QUERY_BUSINESSARTICLES, this.state.newsFeedDictionary.QUERY_POLITICSARTICLES, this.state.newsFeedDictionary.QUERY_SPORTARTICLES, this.state.newsFeedDictionary.QUERY_TECHARTICLES, this.state.newsFeedDictionary.QUERY_SCIENCEARTICLES, this.state.newsFeedDictionary.QUERY_ARTARTICLES, this.state.newsFeedDictionary.QUERY_TRAVELARTICLES,]
            }
        } else {
            this.childState = {
                newsFeedRow: [this.state.newsFeedDictionary.QUERY_TODAY, this.state.newsFeedDictionary.QUERY_THISWEEK, this.state.newsFeedDictionary.QUERY_THISMONTH, this.state.newsFeedDictionary.QUERY_ALLTIME, this.state.newsFeedDictionary.QUERY_USA, this.state.newsFeedDictionary.QUERY_UK, this.state.newsFeedDictionary.QUERY_WORLD,],
            }

        }
    }


    render() {

        const { classes } = this.props;

        return (
            <div className={classes.grid}>

                <NewsFeedHeader categoryName={this.props.categoryName} categoryId={this.props.categoryId} />
                {
                    this.childState.newsFeedRow.map((newsFeedRow, i) => {
                        return (
                            <NewsFeedRow key={Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowFetchData={newsFeedRow[2]} />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeed)
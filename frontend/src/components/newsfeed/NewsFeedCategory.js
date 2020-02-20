// REACT LIBRARIES
import React, { Component } from 'react';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeedCategory.js';



class NewsFeedCategory extends Component {

    constructor(props) {
        super(props)

        this.state = {
            newsFeedDictionary: {
                QUERY_TODAY: ['', 'Trending Today', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_THISWEEK: ['', 'Trending This Week', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_THISMONTH: ['', 'Trending This Month', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_ALLTIME: ['', 'Trending All Time', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_USA: ['', 'Trending in USA', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_UK: ['', 'Trending in UK', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
                QUERY_WORLD: ['', 'Trending Worldwide', { category: this.props.categoryId, limit: 6, offset: 0, sentiment_score_min: 0.8 }],
            },
        }

        this.childState = {
            newsFeedRow: [this.state.newsFeedDictionary.QUERY_TODAY, this.state.newsFeedDictionary.QUERY_THISWEEK, this.state.newsFeedDictionary.QUERY_THISMONTH, this.state.newsFeedDictionary.QUERY_ALLTIME, this.state.newsFeedDictionary.QUERY_USA, this.state.newsFeedDictionary.QUERY_UK, this.state.newsFeedDictionary.QUERY_WORLD,],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            <div className={classes.grid}>

                <NewsFeedHeader categoryName={this.props.categoryName} categoryId={this.props.categoryId} />
                {/* Maps each of the Items in homeScreenNewsFeedRows array to Component instances */}
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

export default withStyles(styles)(NewsFeedCategory)
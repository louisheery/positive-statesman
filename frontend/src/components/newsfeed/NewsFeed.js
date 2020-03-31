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

        const { categoryId } = this.props;

        this.state = {
            newsFeedDictionary: {
                QUERY_TODAY: ['', 'Trending Today', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                QUERY_THISWEEK: ['', 'Trending This Week', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 50, 73, 1)'],
                QUERY_THISMONTH: ['', 'Trending This Month', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                QUERY_ALLTIME: ['', 'Trending All Time', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 209, 56, 1)'],
                QUERY_USA: ['', 'Trending in USA', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                QUERY_UK: ['', 'Trending in UK', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                QUERY_WORLD: ['', 'Trending Worldwide', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],

                QUERY_ARTARTICLES: ['/art', 'Art, Culture & Entertainment', { category: 'iab-qagIAB1', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                QUERY_BUSINESSARTICLES: ['/business', 'Business', { category: 'iab-qagIAB3', limit: 6, offset: 0, sentiment_score_min: 0.5 }],
                QUERY_POLITICSARTICLES: ['/politics', 'Law, Government & Politics', { category: 'iab-qagIAB11', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                QUERY_SCIENCEARTICLES: ['/science', 'Science', { category: 'iab-qagIAB15', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 209, 56, 1)'],
                QUERY_SPORTARTICLES: ['/sport', 'Sport', { category: 'iab-qagIAB17', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                QUERY_TECHARTICLES: ['/tech', 'Technology', { category: 'iab-qagIAB19', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                QUERY_TRAVELARTICLES: ['/travel', 'Travel', { category: 'iab-qagIAB20', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],
            },
        }

        if (categoryId === '') {
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
                            <NewsFeedRow key={Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowFetchData={newsFeedRow[2]} itemColor={newsFeedRow[3]} />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeed)
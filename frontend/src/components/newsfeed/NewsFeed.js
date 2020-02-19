// REACT LIBRARIES
import React, { Component } from 'react';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeed.js';

const newsFeedDictionary = {
    QUERY_TOPARTICLES: ['', 'Top Articles', { limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ARTARTICLES: ['art', 'Art, Culture & Entertainment', { category: 'iptc-qagIAB1', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_BUSINESSARTICLES: ['/business', 'Business', { category: 'iptc-qagIAB3', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_POLITICSARTICLES: ['/politics', 'Law, Government & Politics', { category: 'iptc-qagIAB11', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SCIENCEARTICLES: ['/science', 'Science', { category: 'iptc-qagIAB15', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SPORTARTICLES: ['/sport', 'Sport', { category: 'iptc-qagIAB17', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_TECHARTICLES: ['/tech', 'Technology', { category: 'iptc-qagIAB19', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_TRAVELARTICLES: ['/travel', 'Travel', { category: 'iptc-qagIAB20', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
}

class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_BUSINESSARTICLES,
                                    newsFeedDictionary.QUERY_POLITICSARTICLES,
                                    newsFeedDictionary.QUERY_SPORTARTICLES,
                                    newsFeedDictionary.QUERY_TECHARTICLES,
                                    newsFeedDictionary.QUERY_SCIENCEARTICLES,
                                    newsFeedDictionary.QUERY_ARTARTICLES,
                                    newsFeedDictionary.QUERY_TRAVELARTICLES,
                                ],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            <div className={classes.grid}>

                <NewsFeedHeader categoryName={'Top Stories'} />
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

export default withStyles(styles)(NewsFeed)
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
    QUERY_ARTARTICLES: ['art', 'Art, Culture & Entertainment', { category: 'iptc-subjectcode01000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_CRIMEARTICLES: ['crime', 'Crime, Law & Justice', { category: 'iptc-subjectcode02000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_DISASTERARTICLES: ['disaster', 'Distaster & Accident', { category: 'iptc-subjectcode03000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ECONARTICLES: ['economics', 'Economy, Business & Finance', { category: 'iab-qagIAB3', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_EDUARTICLES: ['education', 'Education', { category: 'iptc-subjectcode05000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ENVIRONARTICLES: ['environment', 'Environmental Issues', { category: 'iptc-subjectcode06000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_HEALTHARTICLES: ['health', 'Health', { category: 'iptc-subjectcode07000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_HUMANARTICLES: ['human', 'Human Interest', { category: 'iptc-subjectcode08000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_LABOURARTICLES: ['labour', 'Labour', { category: 'iptc-subjectcode09000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_LIFESTYLEARTICLES: ['lifestyle', 'Lifestyle', { category: 'iptc-subjectcode10000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_POLITICSARTICLES: ['politics', 'Politics', { category: 'iab-qagIAB11', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_RELIGIONARTICLES: ['religion', 'Religion', { category: 'iptc-subjectcode12000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SCITECHARTICLES: ['scitech', 'Science & Technology', { category: 'iptc-subjectcode13000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SOCIALISSUESARTICLES: ['socialissues', 'Social Issues', { category: 'iptc-subjectcode14000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SPORTARTICLES: ['sport', 'Sport', { category: 'iab-qagIAB17', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_CONFLICTARTICLES: ['conflict', 'Unrest, Conflicts & War', { category: 'iptc-subjectcode16000000', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_WEATHERARTICLES: ['weather', 'Weather', { category: 'iab-qagIAB15-10	', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
}

class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_POLITICSARTICLES, newsFeedDictionary.QUERY_ECONARTICLES, newsFeedDictionary.QUERY_SPORTARTICLES, newsFeedDictionary.QUERY_WEATHERARTICLES],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            <div className={classes.grid}>

                <NewsFeedHeader />
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
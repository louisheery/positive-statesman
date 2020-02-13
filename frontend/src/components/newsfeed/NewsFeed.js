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
    QUERY_ARTARTICLES: ['art', 'Art, Culture & Entertainment', { category: 'arts, culture and entertainment', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_CRIMEARTICLES: ['crime', 'Crime, Law & Justice', { category: 'crime, law and justice', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_DISASTERARTICLES: ['disaster', 'Distaster & Accident', { category: 'disaster and accident', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ECONARTICLES: ['economics', 'Economy, Business & Finance', { category: 'economy, business and finance', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_EDUARTICLES: ['education', 'Education', { category: 'education', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_ENVIRONARTICLES: ['environment', 'Environmental Issues', { category: 'environmental issue', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_HEALTHARTICLES: ['health', 'Health', { category: 'health', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_HUMANARTICLES: ['human', 'Human Interest', { category: 'human interest', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_LABOURARTICLES: ['labour', 'Labour', { category: 'labour', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_LIFESTYLEARTICLES: ['lifestyle', 'Lifestyle', { category: 'lifestyle and leisure', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_POLITICSARTICLES: ['politics', 'Politics', { category: 'politics', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_RELIGIONARTICLES: ['religion', 'Religion', { category: 'religion and belief', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SCITECHARTICLES: ['scitech', 'Science & Technology', { category: 'science and technology', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SOCIALISSUESARTICLES: ['socialissues', 'Social Issues', { category: 'social issue', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_SPORTARTICLES: ['sport', 'Sport', { category: 'sport', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_CONFLICTARTICLES: ['conflict', 'Unrest, Conflicts & War', { category: 'unrest, conflicts and war', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
    QUERY_WEATHERARTICLES: ['weather', 'Weather', { category: 'weather', limit: 6, offset: 0, sentiment_score_min: 0.8 }],
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
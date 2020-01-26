import React, { Component } from 'react';
import NewsFeedRow from './NewsFeedRow';
import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/articles/NewsFeed.js';

const newsFeedDictionary = {
    QUERY_TOPARTICLES: ['/', 'Top Articles'],
    QUERY_ARTARTICLES: ['/art', 'Art, Culture & Entertainment'],
    QUERY_CRIMEARTICLES: ['/crime', 'Crime, Law & Justice'],
    QUERY_DISASTERARTICLES: ['/disaster', 'Distaster & Accident'],
    QUERY_ECONARTICLES: ['/econ', 'Economy, Business & Finance'],
    QUERY_EDUARTICLES: ['/edu', 'Education'],
    QUERY_ENVIRONARTICLES: ['/environ', 'Environmental Issues'],
    QUERY_HEALTHARTICLES: ['/health', 'Health'],
    QUERY_HUMANARTICLES: ['/human', 'Human Interest'],
    QUERY_LABOURARTICLES: ['/labour', 'Labour'],
    QUERY_LIFESTYLEARTICLES: ['/lifestyle', 'Lifestyle'],
    QUERY_POLITICSARTICLES: ['/politics', 'Politics'],
    QUERY_RELIGIONARTICLES: ['/religion', 'Religion'],
    QUERY_SCITECHARTICLES: ['/scitech', 'Science & Technology'],
    QUERY_SOCIALISSUESARTICLES: ['/socialissues', 'Social Issues'],
    QUERY_SPORTARTICLES: ['/sport', 'Sport'],
    QUERY_CONFLICTARTICLES: ['/conflict', 'Unrest, Conflicts & War'],
    QUERY_WEATHERARTICLES: ['/weather', 'Weather'],
}


class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_TOPARTICLES, newsFeedDictionary.QUERY_TOPARTICLES, newsFeedDictionary.QUERY_TOPARTICLES, newsFeedDictionary.QUERY_TOPARTICLES, newsFeedDictionary.QUERY_TOPARTICLES],
        }
    }


    render() {

        const { classes } = this.props;

        return (
            // NewsFeed = ClassName
            <div className={classes.grid}>
                {
                    this.state.homeScreenNewsFeedRows.map((newsFeedRow, i) => {
                        return (
                            <NewsFeedRow key={newsFeedRow[0] + Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeed)
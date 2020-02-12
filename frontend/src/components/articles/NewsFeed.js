import React, { Component } from 'react';
import NewsFeedRow from './NewsFeedRow';
import NewsFeedTop from '../articles/NewsFeedTop';
import { withStyles } from '@material-ui/core/styles';

import styles from '../../assets/styles/components/articles/NewsFeed.js';

/*
const newsFeedDictionary = {
    QUERY_TOPARTICLES: ['', 'Top Articles', { backgroundColor: 'rgba(230, 25, 75, 0.25)'}],
    QUERY_ARTARTICLES: ['art', 'Art, Culture & Entertainment', { backgroundColor: 'rgba(250, 190, 190, 0.25)'}],
    QUERY_CRIMEARTICLES: ['crime', 'Crime, Law & Justice', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_DISASTERARTICLES: ['disaster', 'Distaster & Accident', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_ECONARTICLES: ['economics', 'Economy, Business & Finance', { backgroundColor: 'rgba(0, 128, 128, 0.25)' }],
    QUERY_EDUARTICLES: ['education', 'Education', { backgroundColor: 'rgba(255, 225, 25, 0.25)'}],
    QUERY_ENVIRONARTICLES: ['environment', 'Environmental Issues', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_HEALTHARTICLES: ['health', 'Health', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_HUMANARTICLES: ['human', 'Human Interest', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_LABOURARTICLES: ['labour', 'Labour', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_LIFESTYLEARTICLES: ['lifestyle', 'Lifestyle', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_POLITICSARTICLES: ['politics', 'Politics', { backgroundColor: 'rgba(0, 128, 128, 0.25)'}],
    QUERY_RELIGIONARTICLES: ['religion', 'Religion', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_SCITECHARTICLES: ['scitech', 'Science & Technology', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_SOCIALISSUESARTICLES: ['socialissues', 'Social Issues', { backgroundColor: 'rgba(170, 110, 40, 0.25)'}],
    QUERY_SPORTARTICLES: ['sport', 'Sport', { backgroundColor: 'rgba(0, 128, 128, 0.25)' }],
    QUERY_CONFLICTARTICLES: ['conflict', 'Unrest, Conflicts & War', {backgroundColor: 'rgba(255, 255, 255, 0.25)'}],
    QUERY_WEATHERARTICLES: ['weather', 'Weather', { backgroundColor: 'rgba(0, 128, 128, 0.25)' }],
}
*/

const newsFeedDictionary = {
    QUERY_TOPARTICLES: ['', 'Top Articles', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_ARTARTICLES: ['art', 'Art, Culture & Entertainment', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_CRIMEARTICLES: ['crime', 'Crime, Law & Justice', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_DISASTERARTICLES: ['disaster', 'Distaster & Accident', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_ECONARTICLES: ['economics', 'Economy, Business & Finance', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_EDUARTICLES: ['education', 'Education', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_ENVIRONARTICLES: ['environment', 'Environmental Issues', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_HEALTHARTICLES: ['health', 'Health', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_HUMANARTICLES: ['human', 'Human Interest', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_LABOURARTICLES: ['labour', 'Labour', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_LIFESTYLEARTICLES: ['lifestyle', 'Lifestyle', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_POLITICSARTICLES: ['politics', 'Politics', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_RELIGIONARTICLES: ['religion', 'Religion', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_SCITECHARTICLES: ['scitech', 'Science & Technology', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_SOCIALISSUESARTICLES: ['socialissues', 'Social Issues', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_SPORTARTICLES: ['sport', 'Sport', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_CONFLICTARTICLES: ['conflict', 'Unrest, Conflicts & War', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
    QUERY_WEATHERARTICLES: ['weather', 'Weather', { backgroundColor: 'rgba(255, 255, 255, 1.0)' }],
}

class NewsFeedNew extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_POLITICSARTICLES, newsFeedDictionary.QUERY_ECONARTICLES, newsFeedDictionary.QUERY_SPORTARTICLES, newsFeedDictionary.QUERY_WEATHERARTICLES],
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
                            <NewsFeedRow key={newsFeedRow[0] + Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowColor={newsFeedRow[2]} />
                        );
                    })
                }
            </div>
        )
    }
}

export default withStyles(styles)(NewsFeedNew)
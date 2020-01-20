import React, { Component } from 'react';
import NewsFeedRow from './NewsFeedRow';


const newsFeedDictionary = {
    QUERY_TOPARTICLES: ['articles', 'Top Articles'],
    QUERY_ARTARTICLES: ['articles/art', 'Art, Culture & Entertainment'],
    QUERY_CRIMEARTICLES: ['articles/crime', 'Crime, Law & Justice'],
    QUERY_DISASTERARTICLES: ['articles/disaster', 'Distaster & Accident'],
    QUERY_ECONARTICLES: ['articles/econ', 'Economy, Business & Finance'],
    QUERY_EDUARTICLES: ['articles/edu', 'Education'],
    QUERY_ENVIRONARTICLES: ['articles/environ', 'Environmental Issues'],
    QUERY_HEALTHARTICLES: ['articles/health', 'Health'],
    QUERY_HUMANARTICLES: ['articles/human', 'Human Interest'],
    QUERY_LABOURARTICLES: ['articles/labour', 'Labour'],
    QUERY_LIFESTYLEARTICLES: ['articles/lifestyle', 'Lifestyle'],
    QUERY_POLITICSARTICLES: ['articles/politics', 'Politics'],
    QUERY_RELIGIONARTICLES: ['articles/religion', 'Religion'],
    QUERY_SCITECHARTICLES: ['articles/scitech', 'Science & Technology'],
    QUERY_SOCIALISSUESARTICLES: ['articles/socialissues', 'Social Issues'],
    QUERY_SPORTARTICLES: ['articles/sport', 'Sport'],
    QUERY_CONFLICTARTICLES: ['articles/conflict', 'Unrest, Conflicts & War'],
    QUERY_WEATHERARTICLES: ['articles/weather', 'Weather'],
}



class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [newsFeedDictionary.QUERY_TOPARTICLES, newsFeedDictionary.QUERY_ECONARTICLES, newsFeedDictionary.QUERY_POLITICSARTICLES, newsFeedDictionary.QUERY_SPORTARTICLES, newsFeedDictionary.QUERY_ENVIRONARTICLES],
        }
    }


    render() {
        return (
            // NewsFeed = ClassName
            <div className="NewsFeedGrid">
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

export default NewsFeed
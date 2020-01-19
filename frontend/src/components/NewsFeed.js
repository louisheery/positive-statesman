import React, { Component } from 'react';
import NewsFeedRow from './NewsFeedRow';

const QUERY_TOPARTICLES = '/articles'
const QUERY_ARTARTICLES = '/articles/art'
const QUERY_CRIMEARTICLES = '/articles/crime'
const QUERY_DISASTERARTICLES = '/articles/disaster'
const QUERY_ECONARTICLES = '/articles/econ'
const QUERY_EDUARTICLES = '/articles/edu'
const QUERY_ENVIRONARTICLES = '/articles/environ'
const QUERY_HEALTHARTICLES = '/articles/health'
const QUERY_HUMANARTICLES = '/articles/human'
const QUERY_LABOURARTICLES = '/articles/labour'
const QUERY_LIFESTYLEARTICLES = '/articles/lifestyle'
const QUERY_POLITICSARTICLES = '/articles/politics'
const QUERY_RELIGIONARTICLES = '/articles/religion'
const QUERY_SCITECHARTICLES = '/articles/scitech'
const QUERY_SOCIALISSUESARTICLES = '/articles/socialissues'
const QUERY_SPORTARTICLES = '/articles/sport'
const QUERY_CONFLICTARTICLES = '/articles/conflict'
const QUERY_WEATHERARTICLES = '/articles/weather'

class NewsFeed extends Component {

    constructor(props) {
        super(props)

        this.state = {
            homeScreenNewsFeedRows: [QUERY_TOPARTICLES, QUERY_ECONARTICLES, QUERY_POLITICSARTICLES],
        }
    }


    render() {

        return (
        // NewsFeed = ClassName
            <div className="NewsFeedGrid">
                    {
                        this.state.homeScreenNewsFeedRows.map((newsFeedRow, i) => {
                            return (
                                <NewsFeedRow key={newsFeedRow + Math.random() + i} newsFeedRow={newsFeedRow} />
                            );
                        })
                    }
            </div>


        )
    }
}

export default NewsFeed
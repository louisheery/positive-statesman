// REACT LIBRARIES
import React, { Component } from 'react';

// REDUX LIBRARIES
import { connect } from 'react-redux';
import PropTypes from "prop-types";
import { userFetchData } from '../../store/actions/actions';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

import { defaultCategoryNames } from '../Settings'
import { categoryDictionary } from '../Settings'
import { publisherDictionary } from '../Settings'

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeed.js';

class NewsFeed extends Component {

    static propTypes = {
        isLoggedIn: PropTypes.bool,
        userCategories: PropTypes.array,
        userPublishers: PropTypes.array,
        userFetchData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        const { isLoggedIn } = this.props;

        if (isLoggedIn) {
            this.props.userFetchData('GET', 'category');
            this.props.userFetchData('GET', 'publisher');
        }
    }

    vlookup(matrix, origin, destination, publisher) {
        for (var key in matrix) {
            if (matrix[key][origin] == publisher) {
                return matrix[key][destination];
            }
        }
        return '';
    }

    render() {
        const { classes, pageName, categoryId, publisherId, userCategories, userPublishers } = this.props;

        var userCodes;
        var userNewsFeedData = [];

        // A: Publisher Page
        if (publisherId !== undefined) {

            userCodes = defaultCategoryNames

            for (i = 0; i < userCodes.length; i = i + 1) {
                var categoryURL = this.vlookup(categoryDictionary, 1, 0, userCodes[i]);
                var categoryName = userCodes[i];
                var categoryCode = this.vlookup(categoryDictionary, 1, 2, userCodes[i]);
                console.log(categoryURL, categoryName, categoryCode)
                userNewsFeedData.push([categoryURL, categoryName, { category: categoryCode, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0 }, 'rgba(227, 216, 0, 1)'])
            }


            // B: Home Page
        } else if (categoryId === '') {

            // B1: Home Page with User Not Logged in OR Home Page with User Logged in and No preferences Setup
            if (userCategories == null) {

                userCodes = defaultCategoryNames

                for (i = 0; i < userCodes.length; i = i + 1) {
                    var categoryURL = this.vlookup(categoryDictionary, 1, 0, userCodes[i]);
                    var categoryName = userCodes[i];
                    var categoryCode = this.vlookup(categoryDictionary, 1, 2, userCodes[i]);
                    console.log(categoryURL, categoryName, categoryCode)
                    userNewsFeedData.push([categoryURL, categoryName, { category: categoryCode, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0 }, 'rgba(227, 216, 0, 1)'])
                }



                // B2: Home Page with User Logged In and Preferences Setup
            } else {

                userNewsFeedData.push(['/', 'Recommended Stories', { category: 'recommended', limit: 6, offset: 0, sentiment_score_min: 0 }])

                if (userPublishers != null) {

                    var userPublishersCodes = userPublishers.map(function (x) { return x[1] })
                    for (var i = 0; i < userPublishersCodes.length; i = i + 1) {
                        var publisherURL = this.vlookup(publisherDictionary, 1, 0, userPublishersCodes[i]);
                        var publisherName = userPublishersCodes[i];
                        var publisherCode = this.vlookup(publisherDictionary, 1, 2, userPublishersCodes[i]);
                        userNewsFeedData.push([publisherURL, publisherName, { publisher: publisherCode, limit: 6, offset: 0, sentiment_score_min: 0 }, 'rgba(227, 216, 0, 1)'])
                    }

                }
                if (userCategories != null) {

                    userCodes = userCategories.map(function (x) { return x[1] })
                    var remainingCategoriesCodes = defaultCategoryNames.filter(x => !userCodes.includes(x));
                    userCodes = userCodes.concat(remainingCategoriesCodes)

                    for (i = 0; i < userCodes.length; i = i + 1) {
                        var categoryURL = this.vlookup(categoryDictionary, 1, 0, userCodes[i]);
                        var categoryName = userCodes[i];
                        var categoryCode = this.vlookup(categoryDictionary, 1, 2, userCodes[i]);
                        userNewsFeedData.push([categoryURL, categoryName, { category: categoryCode, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'])
                    }
                }
            }

            // C: Category Page
        } else {

            for (i = 0; i < 6; i = i + 1) {
                userNewsFeedData.push(['', '', { category: categoryCode, limit: 6, offset: 6 * i, sentiment_score_min: 0.5 }])
            }
        }




        return (
            <div className={classes.grid}>

                <NewsFeedHeader pageName={pageName} categoryId={categoryId} publisherId={publisherId} />


                {
                    userNewsFeedData.map((newsFeedRow, i) => {
                        return (

                            <NewsFeedRow key={Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowFetchData={newsFeedRow[2]} newFeedRowNumber={i} />
                        );
                    })
                }
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        isLoggedIn: state.reducer.isLoggedIn,
        userCategories: state.reducer.userCategories,
        userPublishers: state.reducer.userPublishers,
    };
};

export default connect(mapStateToProps, { userFetchData })(withStyles(styles)(NewsFeed))

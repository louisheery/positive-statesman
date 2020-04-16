// REACT LIBRARIES
import React, { Component } from 'react';

// REDUX LIBRARIES
import { connect } from 'react-redux';
import PropTypes from "prop-types";
import { userFetchData } from '../../store/actions/actions';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeed.js';

class NewsFeed extends Component {

    constructor(props) {
        super(props)

        const { categoryId, publisherId } = this.props;

        this.state = {
            newsFeedDictionary: {
                QUERY_TODAY: ['', 'Trending Today', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                QUERY_THISWEEK: ['', 'Trending This Week', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 50, 73, 1)'],
                QUERY_THISMONTH: ['', 'Trending This Month', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                QUERY_ALLTIME: ['', 'Trending All Time', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 209, 56, 1)'],
                QUERY_USA: ['', 'Trending in USA', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                QUERY_UK: ['', 'Trending in UK', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                QUERY_WORLD: ['', 'Trending Worldwide', { category: categoryId, publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],

                xRECOMMEND: ['/', 'Recommended Stories', { category: 'recommended', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 0, 0, 0.4)'],
                x180: ['/arts', 'Art, Culture & Entertainment', { category: 'iab-qagIAB1', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                x219: ['/business', 'Business', { category: 'iab-qagIAB3', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 50, 73, 1)'],
                x237: ['/politics', 'Law, Government & Politics', { category: 'iab-qagIAB11', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                x212: ['/science', 'Science', { category: 'iab-qagIAB15', limit: 6, offset: 0, sentiment_score_min: 0.0 }, 'rgba(0, 209, 56, 1)'],
                x128: ['/sport', 'Sport', { category: 'iab-qagIAB17', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                x84: ['/tech', 'Technology', { category: 'iab-qagIAB19', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                x181: ['/travel', 'Travel', { category: 'iab-qagIAB20', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],
            },
        }

    }

    static propTypes = {
        isLoggedIn: PropTypes.bool,
        userCategories: PropTypes.array,
        userPublishers: PropTypes.array,
        userFetchData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        if (this.props.isLoggedIn) {
            this.props.userFetchData('GET', 'category');
            this.props.userFetchData('GET', 'publisher');
        }
    }

    render() {

        const { classes, categoryId, publisherId } = this.props;

        var newsFeedState;

        // A: Publisher Page
        if (this.props.publisherId !== undefined) {
            newsFeedState = {
                newsFeedRow: [this.state.newsFeedDictionary.x219, this.state.newsFeedDictionary.x237, this.state.newsFeedDictionary.x128, this.state.newsFeedDictionary.x84, this.state.newsFeedDictionary.x212, this.state.newsFeedDictionary.x180, this.state.newsFeedDictionary.x181,]
            }

        // B: Home Page
        } else if (this.props.categoryId === '') {

            // B1: Home Page with User Not Logged in OR Home Page with User Logged in and No preferences Setup
            if (this.props.userCategories == null) {

                newsFeedState = {

                    newsFeedRow: [this.state.newsFeedDictionary.x219, this.state.newsFeedDictionary.x237, this.state.newsFeedDictionary.x128, this.state.newsFeedDictionary.x84, this.state.newsFeedDictionary.x212, this.state.newsFeedDictionary.x180, this.state.newsFeedDictionary.x181,]
                }

            // B2: Home Page with User Logged In and Preferences Setup
            } else {

                var recommendationCode = ['xRECOMMEND']

                var userCategoriesCodes = this.props.userCategories.map(function (x) { return 'x' + x[0] })

                let allCategoriesCodes = ['x180', 'x219', 'x237', 'x212', 'x128', 'x84', 'x181']
                let remainingCategoriesCodes = allCategoriesCodes.filter(x => !userCategoriesCodes.includes(x));

                if (this.props.isLoggedIn) {
                    userCategoriesCodes = recommendationCode.concat(userCategoriesCodes);
                }
                userCategoriesCodes = userCategoriesCodes.concat(remainingCategoriesCodes)

                var userCategoriesData = [];
                for (var i = 0; i < userCategoriesCodes.length; i = i + 1) {
                    var code = userCategoriesCodes[i]
                    userCategoriesData.push(this.state.newsFeedDictionary[code])
                }

                newsFeedState = {

                    newsFeedRow: userCategoriesData
                }
            }

        // C: Category Page
        } else {

            newsFeedState = {
                newsFeedRow: [this.state.newsFeedDictionary.QUERY_TODAY, this.state.newsFeedDictionary.QUERY_THISWEEK, this.state.newsFeedDictionary.QUERY_THISMONTH, this.state.newsFeedDictionary.QUERY_ALLTIME, this.state.newsFeedDictionary.QUERY_USA, this.state.newsFeedDictionary.QUERY_UK, this.state.newsFeedDictionary.QUERY_WORLD,],
            }
        }

            return (
                <div className={classes.grid}>

                    <NewsFeedHeader pageName={this.props.pageName} categoryId={this.props.categoryId} />


                    {
                        newsFeedState.newsFeedRow.map((newsFeedRow, i) => {
                            return (
                                <NewsFeedRow key={Math.random() + i} newsFeedRow={newsFeedRow[0]} newsFeedRowTitle={newsFeedRow[1]} newsFeedRowFetchData={newsFeedRow[2]} itemColor={newsFeedRow[3]} />
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

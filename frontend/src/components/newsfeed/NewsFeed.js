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
                QUERY_A: ['', '', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                QUERY_B: ['', '', { category: categoryId, limit: 6, offset: 6, sentiment_score_min: 0.5 }, 'rgba(0, 50, 73, 1)'],
                QUERY_C: ['', '', { category: categoryId,  limit: 6, offset: 12, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                QUERY_D: ['', '', { category: categoryId,  limit: 6, offset: 18, sentiment_score_min: 0.5 }, 'rgba(0, 209, 56, 1)'],
                QUERY_E: ['', '', { category: categoryId, limit: 6, offset: 24, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                QUERY_F: ['', '', { category: categoryId, limit: 6, offset: 30, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],

                xRECOMMEND: ['/', 'Recommended Stories', { category: 'recommended', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 0, 0, 0.4)'],
                x180: ['/arts', 'Art, Culture & Entertainment', { category: 'iab-qagIAB1', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(227, 216, 0, 1)'],
                x219: ['/business', 'Business', { category: 'iab-qagIAB3', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 50, 73, 1)'],
                x237: ['/politics', 'Law, Government & Politics', { category: 'iab-qagIAB11', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(112, 0, 27, 1)'],
                x212: ['/science', 'Science', { category: 'iab-qagIAB15', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: 0.0 }, 'rgba(0, 209, 56, 1)'],
                x128: ['/sport', 'Sport', { category: 'iab-qagIAB17', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(43, 128, 255, 1)'],
                x84: ['/technology', 'Technology', { category: 'iab-qagIAB19', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(139, 0, 194, 1)'],
                x181: ['/travel', 'Travel', { category: 'iab-qagIAB20', publisher: publisherId,limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 186, 93, 1)'],
                x183: ['/autos', 'Automotive', { category: 'iab-qagIAB2', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 186, 93, 1)'],

                x112: ['/careers', 'Careers', { category: 'iab-qagIAB4', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(227, 216, 0, 1)'],
                x69: ['/familyparenting', 'Family & Parenting', { category: 'iab-qagIAB6', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 50, 73, 1)'],
                x154: ['/education', 'Education', { category: 'iab-qagIAB5', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 50, 73, 1)'],
                x340: ['/healthfitness', 'Health & Fitness', { category: 'iab-qagIAB7', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(112, 0, 27, 1)'],
                x131: ['/food', 'Food', { category: 'iab-qagIAB8', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.0 }, 'rgba(0, 209, 56, 1)'],
                x40: ['/hobbies', 'Hobbies & Interests', { category: 'iab-qagIAB9', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(43, 128, 255, 1)'],
                x326: ['/homegarden', 'Home & Garden', { category: 'iab-qagIAB10', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(139, 0, 194, 1)'],
                x162: ['/news', 'General News', { category: 'iab-qagIAB12', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 186, 93, 1)'],
                x96: ['/personalfinance', 'Personal Finance', { category: 'iab-qagIAB13', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 186, 93, 1)'],
                x298: ['/society', 'Society', { category: 'iab-qagIAB14', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(227, 216, 0, 1)'],
                x192: ['/pets', 'Pets', { category: 'iab-qagIAB16', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(0, 50, 73, 1)'],
                x376: ['/stylefashion', 'Style & Fashion', { category: 'iab-qagIAB18', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: categoryId == '' ? 0.5 : 0 }, 'rgba(112, 0, 27, 1)'],
                x308: ['/realestate', 'Real Estate', { category: 'iab-qagIAB21', publisher: publisherId, limit: 6, offset: 0, sentiment_score_min: 0.0 }, 'rgba(0, 209, 56, 1)'],
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
                console.log(this.props.userCategories)

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
                newsFeedRow: [this.state.newsFeedDictionary.QUERY_A, this.state.newsFeedDictionary.QUERY_B, this.state.newsFeedDictionary.QUERY_C, this.state.newsFeedDictionary.QUERY_D, this.state.newsFeedDictionary.QUERY_E, this.state.newsFeedDictionary.QUERY_F],
            }
        }
            return (
                <div className={classes.grid}>

                    <NewsFeedHeader pageName={this.props.pageName} categoryId={this.props.categoryId} publisherId={this.props.publisherId} />


                    {
                        newsFeedState.newsFeedRow.map((newsFeedRow, i) => {
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

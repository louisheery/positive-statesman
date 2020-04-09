// REACT LIBRARIES
import React, { Component } from 'react';

// REDUX LIBRARIES
import reducer from '../../store/reducers/reducer';
import { connect, Provider } from 'react-redux';
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import store from "../../store/store";
import { userGETData, avaliableData } from '../../store/actions/actions';

// INTERNAL REACT COMPONENTS
import NewsFeedRow from './NewsFeedRow';
import NewsFeedHeader from './NewsFeedHeader';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeed.js';
import Typography from 'material-ui/styles/typography';

class NewsFeed extends Component {

    constructor(props) {
        super(props)

        const { categoryId } = this.props;

        this.state = {
            newsFeedDictionary: {
                QUERY_TODAY: ['', 'Trending Today', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                QUERY_THISWEEK: ['', 'Trending This Week', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 50, 73, 1)'],
                QUERY_THISMONTH: ['', 'Trending This Month', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                QUERY_ALLTIME: ['', 'Trending All Time', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 209, 56, 1)'],
                QUERY_USA: ['', 'Trending in USA', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                QUERY_UK: ['', 'Trending in UK', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                QUERY_WORLD: ['', 'Trending Worldwide', { category: categoryId, limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],

                x180: ['/art', 'Art, Culture & Entertainment', { category: 'iab-qagIAB1', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(227, 216, 0, 1)'],
                x219: ['/business', 'Business', { category: 'iab-qagIAB3', limit: 6, offset: 0, sentiment_score_min: 0.5 }],
                x237: ['/politics', 'Law, Government & Politics', { category: 'iab-qagIAB11', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(112, 0, 27, 1)'],
                x212: ['/science', 'Science', { category: 'iab-qagIAB15', limit: 6, offset: 0, sentiment_score_min: 0.0 }, 'rgba(0, 209, 56, 1)'],
                x128: ['/sport', 'Sport', { category: 'iab-qagIAB17', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(43, 128, 255, 1)'],
                x84: ['/tech', 'Technology', { category: 'iab-qagIAB19', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(139, 0, 194, 1)'],
                x181: ['/travel', 'Travel', { category: 'iab-qagIAB20', limit: 6, offset: 0, sentiment_score_min: 0.5 }, 'rgba(0, 186, 93, 1)'],
            },
        }

    }

    static propTypes = {
        userCategories: PropTypes.array,
        userPublishers: PropTypes.array,
        userGETData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        this.props.userGETData('GET', 'category');
    }

    render() {

        const { classes, categoryId } = this.props;

        var newsFeedState;


        

        if (this.props.categoryId === '') {

            if (this.props.userCategories == null) {

                newsFeedState = {

                    newsFeedRow: [this.state.newsFeedDictionary.x219, this.state.newsFeedDictionary.x237, this.state.newsFeedDictionary.x128, this.state.newsFeedDictionary.x84, this.state.newsFeedDictionary.x212, this.state.newsFeedDictionary.x180, this.state.newsFeedDictionary.x181,]


                }
            } else {

                var userCategoriesCodes = this.props.userCategories.map(function (x) { return 'x' + x[0] })

                let allCategoriesCodes = ['x180', 'x219', 'x237', 'x212', 'x128', 'x84', 'x181']
                let remainingCategoriesCodes = allCategoriesCodes.filter(x => !userCategoriesCodes.includes(x));

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
        } else {
            newsFeedState = {
                newsFeedRow: [this.state.newsFeedDictionary.QUERY_TODAY, this.state.newsFeedDictionary.QUERY_THISWEEK, this.state.newsFeedDictionary.QUERY_THISMONTH, this.state.newsFeedDictionary.QUERY_ALLTIME, this.state.newsFeedDictionary.QUERY_USA, this.state.newsFeedDictionary.QUERY_UK, this.state.newsFeedDictionary.QUERY_WORLD,],
            }
        }

            return (
                <div className={classes.grid}>

                    <NewsFeedHeader categoryName={this.props.categoryName} categoryId={this.props.categoryId} />


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
            userCategories: state.reducer.userCategories,
            userPublishers: state.reducer.userPublishers,
        };
    };

export default connect(mapStateToProps, { userGETData })(withStyles(styles)(NewsFeed))

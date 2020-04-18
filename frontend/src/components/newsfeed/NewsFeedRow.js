// REACT LIBRARIES
import React, { Component } from 'react';

// OTHER LIBRARIES
import { fetchArticles } from '../../apiIntegration';

// INTERNAL REACT COMPONENTS
import NewsFeedItem from './NewsFeedItem';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Grid from '@material-ui/core/Grid';
import withWidth from '@material-ui/core/withWidth';
import Typography from '@material-ui/core/Typography';
import { Link } from '@material-ui/core';
import { NavLink } from 'react-router-dom';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeedRow.js';

function rowNumberToColour(rowNumber) {

    while (rowNumber > 8) {
        rowNumber = rowNumber - 8;
    }

    switch (rowNumber) {
        case 1:
            return 'rgba(0, 50, 73, 1)'
        case 2:
            return 'rgba(112, 0, 27, 1)'
        case 3:
            return 'rgba(0, 209, 56, 1)'
        case 4:
            return 'rgba(43, 128, 255, 1)'
        case 5:
            return 'rgba(139, 0, 194, 1)'
        case 6:
            return 'rgba(0, 186, 93, 1)'
        case 7:
            return 'rgba(32, 32, 222, 0.4)'
        case 8:
            return 'rgba(227, 216, 0, 1)'
        
        default:
            return 'rgba(0, 0, 0, 0.4)'
    }
};

class NewsFeedRow extends Component {

    _isMounted = false;

    constructor(props) {
        super(props)

        this.state = {
            articles: [],  // articles to be displayed in row

        }
    }

    async componentDidMount() {

        this._isMounted = true;

        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data
        var fetchedArticles = await fetchArticles(this.props.newsFeedRowFetchData)
        if (this._isMounted) {
            this.setState({ articles: fetchedArticles })
        }

    }

    componentWillUnmount() {
        this._isMounted = false;
    }



    render() {

        const { classes } = this.props;

        // this.state.articles
        // this.props.Articles

        var categoryNames = ['Art, Culture & Entertainment', 'Business', 'Law, Government & Politics', 'Science', 'Sport', 'Technology', 'Travel', 'Careers', 'Education', 'Family & Parenting', 'Health & Fitness','Food', 'Hobbies & Interests','Home & Garden','General News', 'Personal Finance', 'Society', 'Pets', 'Style & Fashion', 'Real Estate',]


        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES
        var sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.articles, 'sentiment_score').reverse();

        Object.size = function (obj) {
            var size = 0, key;
            for (key in obj) {
                if (obj.hasOwnProperty(key)) size++;
            }
            return size;
        };

        

        return (

            <div>

                {(Object.size(sortedArticles) > 1) ? (

                    <div className={classes.container}>
                        {(() => {
                            if (categoryNames.includes(this.props.newsFeedRowTitle)) {
                                return (
                                    <NavLink to={`/categories${this.props.newsFeedRow}`} className={classes.hyperlinkTitle}>
                                        <Typography className={classes.hyperlinkTitle} variant="h5">{this.props.newsFeedRowTitle}</Typography>
                                    </NavLink>
                                )
                            } else if (this.props.newsFeedRowTitle == '') {
                                return (
                                    <div></div>
                                )
                            } else {
                                return (
                                    <Typography className={classes.nonHyperlinkTitle} variant="h5">{this.props.newsFeedRowTitle}</Typography>
                                )
                            }
                        })()}

                        <div className={classes.subContainer}>
                            <Grid container className={classes.gridList}>
                                {
                                    sortedArticles.slice(0, this.props.width == 'xs' ? 1 : this.props.width == 'sm' ? 2 : this.props.width == 'md' ? 3 : 4).map((article, i) => {
                                        return (<NewsFeedItem key={i} article={article} itemColor={rowNumberToColour(this.props.newFeedRowNumber)} isHeaderItem={false} />)
                                    })
                                }
                            </Grid>
                        </div>
                    </div>


                ) : (
                        <div>
                        </div>
                    )
                }

            </div>


        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedRow))

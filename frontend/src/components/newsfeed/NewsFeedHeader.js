// REACT LIBRARIES
import React, { Component } from 'react';

// OTHER LIBRARIES
import { fetchArticles } from '../../apiIntegration';

// INTERNAL REACT COMPONENTS
import NewsFeedItem from './NewsFeedItem';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import withWidth from '@material-ui/core/withWidth';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/newsfeed/NewsFeedHeader.js';

class NewsFeedHeader extends Component {

    constructor(props) {
        super(props)
        this.state = {
            topArticles: [],  // articles to be displayed in row
        }
    }

    async componentDidMount() {
        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data

        var topArticles = await fetchArticles({ limit: 6, offset: 0, category: this.props.categoryId, publisher: this.props.publisherId, sentiment_score_min: 0.5 })
        this.setState({ topArticles: topArticles })
    }

    render() {
        const { classes } = this.props;

        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES

        var sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.topArticles, 'sentiment_score').reverse();

        Object.size = function (obj) {
            var size = 0, key;
            for (key in obj) {
                if (obj.hasOwnProperty(key)) size++;
            }
            return size;
        };

        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    {this.props.pageName}
                </Typography>

                {(Object.size(sortedArticles) > 1) ? (

                <Grid container>
                    {
                        sortedArticles.slice(0, this.props.width == 'xs' ? 2 : this.props.width == 'sm' ? 4 : 6).map((article, i) => {
                            return (<NewsFeedItem key={i} article={article} width={this.props.width} isHeaderItem={true} />)
                        })
                    }
                </Grid>
                ) : (
                    <div>
                        <Typography variant="subtitle1">
                                No articles found for this {this.props.categoryId == '' ? 'category' : 'publisher'} <span role="img" aria-label="sad">🙁</span>
                        </Typography>
                        <Link href={"/overview"}>
                        <Typography variant="subtitle2">
                            Click here to view other categories and publishers.
                        </Typography>
                            </Link>
                        </div>
                )}
            </div>
        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedHeader))
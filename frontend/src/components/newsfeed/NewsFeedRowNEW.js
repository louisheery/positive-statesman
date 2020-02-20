// REACT LIBRARIES
import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

// OTHER LIBRARIES
import { fetchArticles } from '../../apiIntegration';
import moment from 'moment';

// INTERNAL REACT COMPONENTS
import ArticleVote from './ArticleVote';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { Button } from '@material-ui/core';
import withWidth from '@material-ui/core/withWidth';
import Link from '@material-ui/core/Link';
import GridListTileBar from '@material-ui/core/GridListTileBar';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField'

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeedRow.js';

class NewsFeedRow extends Component {

    constructor(props) {
        super(props)

        this.state = {
            articles: [],  // articles to be displayed in row

        }
    }

    async componentDidMount() {
        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data
        /*
                fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
                    .then(response => response.json())
                    .then(articles => this.setState({ articles }));
        
        */

        var fetchedArticles = await fetchArticles(this.props.newsFeedRowFetchData)
        this.setState({ articles: fetchedArticles })

    }



    render() {

        const { classes } = this.props;

        // this.state.articles
        // this.props.Articles


        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES
        var sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.articles, 'sentiment_score').reverse();

        var numberRowColumns;

        switch (this.props.width) {
            case 'xs':
                numberRowColumns = 1;
                break;
            case 'sm':
                numberRowColumns = 2;
                break;
            case 'md':
                numberRowColumns = 3;
                break;
            case 'lg':
                numberRowColumns = 4;
                break;
            default:
                numberRowColumns = 5;
                break;
        }

        return (
            <div className={classes.container}>

                <NavLink to={`/${this.props.newsFeedRow}`} className={classes.rowTitle}>
                    <Typography className={classes.sectionTitle} variant="h5">{this.props.newsFeedRowTitle}</Typography>
                </NavLink>
                <div>
                    <GridList className={classes.gridList} cellHeight={180} rows={2} cols={numberRowColumns} spacing={20}>

                        {
                            sortedArticles.map((article, i) => {

                                var positivityTextStyle

                                var positivityScorePcnt = Math.round(((article.sentiment_score + 1) * 100 / 2));

                                if (positivityScorePcnt > 70) {
                                    positivityTextStyle = { color: 'green' };
                                }
                                else if (positivityScorePcnt > 50) {
                                    positivityTextStyle = { color: 'orange' };
                                }
                                else {
                                    positivityTextStyle = { color: 'red' };
                                }

                                return (



                                    <GridListTile key={Math.random() + i} cols={1} rows={1}>
                                        <Paper square={true} style={{ height: '170px', borderTop: '1px solid black', borderBottom: '1px solid black' }}>
                                            <div>
                                                <Link href={article.url}>
                                                    <Typography className={classes.otherTopArticleTitle}>{article.title}</Typography>
                                                </Link>
                                                {/*<span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span>*/}

                                                <Typography>{article.publisher}{"   -   "}{moment(`${article.publish_date}`).fromNow()}</Typography>
                                                <ArticleVote articleId={article.id} />
                                                <Typography style={positivityTextStyle}>{positivityScorePcnt}%</Typography>


                                            </div>
                                        </Paper>
                                    </GridListTile>


                                )
                            })
                        }
                    </GridList>
                </div>
            </div>


        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedRow))

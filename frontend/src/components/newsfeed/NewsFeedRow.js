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

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/newsfeed/NewsFeedRow.js';

class NewsFeedRow extends Component {

    constructor(props) {
        super(props)

        this.state = {
            rowArticles: [],  // articles to be displayed in row

        }
    }

    async componentDidMount() {
        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data
        /*
                fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
                    .then(response => response.json())
                    .then(rowArticles => this.setState({ rowArticles }));
        
        */

<<<<<<< HEAD:frontend/src/components/articles/NewsFeedRow.js
        var fetchedArticles = await fetchArticles({limit: 6, offset: 0})
=======
        var fetchedArticles = await fetchArticles(this.props.newsFeedRowFetchData)
>>>>>>> 1bfae5399f9a62c093e4f8cd1a50bcbe3755db55:frontend/src/components/newsfeed/NewsFeedRow.js
        this.setState({ rowArticles: fetchedArticles })

    }



    render() {

        const { classes } = this.props;

        // this.state.rowArticles
        // this.props.Articles


        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES
        var sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.rowArticles, 'sentiment_score').reverse();

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
                    <GridList className={classes.gridList} cellHeight={150} rows={2} cols={numberRowColumns} spacing={20}>

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
                                        <Link href={article.url}>
                                            <GridListTileBar
                                                style={{ backgroundColor: 'white' }}

                                                title={<span>{article.title}</span>}
                                                titlePosition='top'
                                                rows={3}
                                                classes={{
                                                    root: classes.otherTopArticleRoot,
                                                    title: classes.otherTopArticleTitle,
                                                }}
                                            />
                                        </Link>

                                        <GridListTileBar
                                            style={{ backgroundColor: 'white' }}
                                            subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
                                            rows={3}
                                            classes={{
                                                root: classes.otherTopArticleSecondaryRoot,
                                                subtitle: classes.otherTopArticleSecondarySubtitle,
                                            }}
                                        />


                                        <GridListTileBar
                                            style={{ backgroundColor: 'white' }}
                                            className={classes.voteBar}
                                            titlePosition="bottom"
                                            title={
                                                <div className={classes.otherArticleTileVoteDiv}>
                                                    <span style={{ float: 'left', display: 'inline-block' }}>

                                                        <ArticleVote />

                                                    </span>
                                                    <span style={{ float: 'right', display: 'inline-block' }}>

                                                        <Button className={classes.positivityScore} variant="outlined" color="primary" disableElevation disabled>
                                                            <span role="img" style={positivityTextStyle}>{positivityScorePcnt}%</span>
                                                        </Button>

                                                    </span>
                                                </div>
                                            }
                                        />
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

// REACT LIBRARIES
import React, { Component } from 'react';

// OTHER LIBRARIES
import moment from 'moment';
import { fetchArticles } from '../../apiIntegration';

// INTERNAL REACT COMPONENTS
import ArticleVote from './ArticleVote';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { Button } from '@material-ui/core';
import Link from '@material-ui/core/Link';
import withWidth from '@material-ui/core/withWidth';
import GridListTileBar from '@material-ui/core/GridListTileBar';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/newsfeed/NewsFeedHeader.js';

class NewsFeedHeader extends Component {

    constructor(props) {
        super(props)

        this.state = {
            topArticle: [],  // articles to be displayed in row
            topArticles: [],  // articles to be displayed in row

        }
    }

    async componentDidMount() {
        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data
<<<<<<< HEAD:frontend/src/components/articles/NewsFeedTop.js
        /*
                fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
                    .then(response => response.json())
                    .then(rowArticles => this.setState({ rowArticles }));
        
        */

        var topArticle = await fetchArticles({limit: 1, offset: 0, category: this.props.newsFeedRow, sentiment_score_min: 0.8, sentiment_score_max: 0.95})
        this.setState({ topArticle: topArticle })
        var topArticles = await fetchArticles({limit: 4, offset: 1, category: this.props.newsFeedRow, sentiment_score_min: 0.9})
=======
        var topArticle = await fetchArticles({ limit: 1, offset: 0, category: this.props.newsFeedRow, sentiment_score_min: 0.8, sentiment_score_max: 0.95 })
        this.setState({ topArticle: topArticle })
        var topArticles = await fetchArticles({ limit: 4, offset: 1, category: this.props.newsFeedRow, sentiment_score_min: 0.9 })
>>>>>>> 1bfae5399f9a62c093e4f8cd1a50bcbe3755db55:frontend/src/components/newsfeed/NewsFeedHeader.js
        this.setState({ topArticles: topArticles })

    }



    render() {

        const { classes } = this.props;

        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES
        var sorter = require('sort-json-array');
        var sortedArticle = sorter(this.state.topArticle, 'sentiment_score').reverse();

        sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.topArticles, 'sentiment_score').reverse();

        var numberTopColumns;
        var topArticleShown;
        var numberOtherTopColumns;


        switch (this.props.width) {
            case 'xs':
                numberTopColumns = 1.5;
                topArticleShown = false;
                numberOtherTopColumns = 3;
                break;
            case 'sm':
                numberTopColumns = 3;
                topArticleShown = false;
                numberOtherTopColumns = 1.5;
                break;
            case 'md':
                numberTopColumns = 5;
                topArticleShown = true;
                numberOtherTopColumns = 1.5;
                break;
            case 'lg':
                numberTopColumns = 5;
                topArticleShown = true;
                numberOtherTopColumns = 1.5;
                break;
            default:
                numberTopColumns = 5;
                topArticleShown = true;
                numberOtherTopColumns = 1.5;
                break;
        }

        return (
            <div className={classes.container}>
                <Typography variant="h4">Top Stories</Typography>

                <div className={classes.gridRoot}>
                    <GridList className={classes.subContainer} cellHeight={160} cols={numberTopColumns}>


                        {topArticleShown && (
                            <GridList className={classes.gridList} cellHeight={160} cols={2} rows={2}>

                                {
                                    sortedArticle.map((article, i) => {

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

                                            <GridListTile key={Math.random() + i} cols={2} rows={2}>
                                                <img className={classes.articleTileImage} src={article.image_url} alt={article.title} />
                                                <Link href={article.url}>
                                                    <GridListTileBar
                                                        title={<span>{article.title}</span>}
                                                        subtitle={<span><span className={classes.articleTileSubtitle}>{article.text_full}</span></span>}
                                                        titlePosition='top'
                                                        rows={3}
                                                        classes={{
                                                            root: classes.topArticleRoot,
                                                            title: classes.topArticleTitle,
                                                            subtitle: classes.topArticleSubtitle,
                                                        }}
                                                    />
                                                </Link>

                                                <GridListTileBar
                                                    subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', display: 'inline-block', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
                                                    rows={3}
                                                    classes={{
                                                        root: classes.topArticleSecondaryRoot,
                                                        subtitle: classes.topArticleSecondarySubtitle,
                                                    }}
                                                />


                                                <GridListTileBar
                                                    className={classes.voteBar}
                                                    titlePosition="bottom"
                                                    title={
                                                        <div className={classes.articleTileVoteDiv}>
                                                            <span style={{ float: 'left', display: 'inline-block' }}>

                                                                <ArticleVote />

                                                            </span>
                                                            <span style={{ float: 'right', display: 'inline-block' }}>

                                                                <Button className={classes.positivityScore} variant="outlined" color="primary" disableElevation disabled>
                                                                    <span role="img" style={positivityTextStyle}>{positivityScorePcnt}% Positivity</span>
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
                        )}

                        <GridList className={classes.gridList} cellHeight={160} rows={2} cols={3} >

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


                                        <GridListTile key={Math.random() + i} cols={numberOtherTopColumns} rows={1}>
                                            <img src={article.image_url} alt={article.title} className={classes.otherArticleTileImage} />
                                            <Link href={article.url}>
                                                <GridListTileBar
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
                                                subtitle={<span><span style={{float: 'left', display: 'inline-block', marginTop: '10px'}}>{article.publisher}</span><span style={{float: 'right', display: 'inline-block', marginTop: '10px'}}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
                                                rows={3}
                                                classes={{
                                                    root: classes.otherTopArticleSecondaryRoot,
                                                    subtitle: classes.otherTopArticleSecondarySubtitle,
                                                }}
                                            />



                                            <GridListTileBar
                                                className={classes.voteBar}
                                                titlePosition="bottom"
                                                title={
                                                    <div className={classes.otherTopArticleSecondaryVoteDiv}>
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
                    </GridList>
                </div>
            </div>


        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedHeader))
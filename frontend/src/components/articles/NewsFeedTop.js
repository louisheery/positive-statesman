import React, { Component } from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { fetchArticles } from '../../apiIntegration';
import { withStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import { Button } from '@material-ui/core';
import moment from 'moment';
import Link from '@material-ui/core/Link';
import withWidth from '@material-ui/core/withWidth';
import Hidden from '@material-ui/core/Hidden';
import ArticleVote from './ArticleVote';

import GridListTileBar from '@material-ui/core/GridListTileBar';

import styles from '../../../src/assets/styles/components/articles/NewsFeedTop.js';

class NewsFeedRow extends Component {

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
        /*
                fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
                    .then(response => response.json())
                    .then(rowArticles => this.setState({ rowArticles }));
        
        */

        var topArticle = await fetchArticles(1, 0, this.props.newsFeedRow, 0.8, 0.95)
        this.setState({ topArticle: topArticle })
        var topArticles = await fetchArticles(4, 1, this.props.newsFeedRow, 0.9)
        this.setState({ topArticles: topArticles })

    }



    render() {

        const { classes } = this.props;

        // this.state.rowArticles
        // this.props.Articles


        // NOTE: STILL NEED TO FIX THIS SORTING
        // CURRENTLY IT CAN'T DEAL WITH NEGATIVE SENTIMENT_SCORES
        var sorter = require('sort-json-array');
        var sortedArticle = sorter(this.state.topArticle, 'sentiment_score').reverse();
        console.log(sortedArticle)

        var sorter = require('sort-json-array');
        var sortedArticles = sorter(this.state.topArticles, 'sentiment_score').reverse();
        console.log(sortedArticles)

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




                                            <GridListTile key={article.image_url} cols={2} rows={2}>
                                                <img src={article.image_url} alt={article.title} style={{ height: '100%' }} />
                                                <Link href={article.url}>
                                                    <GridListTileBar
                                                        title={<span>{article.title}</span>}
                                                        subtitle={<span><span style={{ display: "inline-block" }}>{article.text_full}</span></span>}
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
                                                    subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
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
                                                        <div style={{ width: '100%' }}>
                                                            <span style={{ float: 'left', display: 'inline-block' }}>

                                                                <ArticleVote articleId={article.id} />

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


                                        <GridListTile key={article.image_url} cols={numberOtherTopColumns} rows={1}>
                                            <img src={article.image_url} alt={article.title} style={{ height: '100%', width: '100%' }} />
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
                                                subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
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
                                                    <div style={{ width: '100%' }}>
                                                        <span style={{ float: 'left', display: 'inline-block' }}>

                                                            <ArticleVote articleId={article.id}/>

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

export default withWidth()(withStyles(styles)(NewsFeedRow))

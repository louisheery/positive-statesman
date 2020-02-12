import React, { Component } from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { fetchArticles } from '../../apiIntegration';
import { withStyles } from '@material-ui/core/styles';
import { Button } from '@material-ui/core';
import moment from 'moment';
import withWidth from '@material-ui/core/withWidth';
import { NavLink } from 'react-router-dom';
import Link from '@material-ui/core/Link';
import GridListTileBar from '@material-ui/core/GridListTileBar';

import ArticleVote from './ArticleVote';

import styles from '../../../src/assets/styles/components/articles/NewsFeedRow.js';

class NewsFeedRowOld extends Component {

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

        var fetchedArticles = await fetchArticles(6, 0)
        this.setState({ rowArticles: fetchedArticles })

    }



    render() {

        const { classes, width } = this.props;

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

                <NavLink to={`/${this.props.newsFeedRow}`} style={{ textDecoration: 'none', color: 'unset' }} >
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


                                    <GridListTile key={article.image_url} cols={1} rows={1}>
                                        <img style={{ colorOverlay: 'red', opacity: '0.3', height: '100%' }} src={article.image_url} alt={article.title} />
                                        <Link href={article.url}>
                                            <GridListTileBar
                                                style={this.props.newsFeedRowColor}

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
                                            style={this.props.newsFeedRowColor}
                                            subtitle={<span><span style={{ float: 'left', display: 'inline-block', marginTop: '10px' }}>{article.publisher}</span><span style={{ float: 'right', marginTop: '10px' }}>{moment(`${article.publish_date}`).fromNow()}</span></span>}
                                            rows={3}
                                            classes={{
                                                root: classes.otherTopArticleSecondaryRoot,
                                                subtitle: classes.otherTopArticleSecondarySubtitle,
                                            }}
                                        />


                                        <GridListTileBar
                                            style={this.props.newsFeedRowColor}
                                            className={classes.voteBar}
                                            titlePosition="bottom"
                                            title={
                                                <div style={{ width: '100%' }}>
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

export default withWidth()(withStyles(styles)(NewsFeedRowOld))

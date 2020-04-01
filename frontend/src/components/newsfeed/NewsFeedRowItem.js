// REACT LIBRARIES
import React, { Component } from 'react';

// OTHER LIBRARIES
import moment from 'moment';

// INTERNAL REACT COMPONENTS
import ArticleVote from './ArticleVote';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import withWidth from '@material-ui/core/withWidth';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Hidden from '@material-ui/core/Hidden';
import { FacebookShareButton, FacebookIcon } from "react-share";
import ShareIcon from '@material-ui/icons/Share';
import Button from '@material-ui/core/Button'

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/newsfeed/NewsFeedRowItem.js';

class NewsFeedRowItem extends Component {

    render() {
        const { classes, article } = this.props;
        var score = Math.round(((article.sentiment_score + 1) * 100 / 2));

        return (
            <Grid item xs={12} sm={6} md={4}>
                <Paper className={classes.paper} style={{ background: `-webkit-linear-gradient(${this.props.itemColor}, rgba(0, 0, 0, 0.3))`, backgroundSize: '100% 100%' }} square={true}>
                    <Link href={article.url}>
                        <Typography variant='subtitle1' className={classes.title} >
                            {article.title}
                        </Typography>
                    </Link>

                    <span>
                        <Typography className={classes.subtitleLeft}>
                            {article.publisher}
                        </Typography>
                        <Typography className={classes.subtitleRight}>
                            {moment(`${article.publish_date}`).fromNow()}
                        </Typography>
                    </span>
                    <span className={classes.alignLeft} >
                        <ArticleVote articleId={article.id} />
                    </span>

                    <span className={classes.alignLeft} >
                        <p className={classes.positivity} style={{ color: score > 70 ? 'green' : score > 50 ? 'orange' : 'red' }}>
                            {score}%
                            <Hidden smDown>
                                {" Positive"}
                            </Hidden>
                        </p>

                        <FacebookShareButton url={article.url} quote={article.title} className="share">
                            <Button style={{ color: 'white', padding: '-4px' }}>
                                Share <ShareIcon />
                            </Button>
                        </FacebookShareButton>
                    </span>
                    
                </Paper>
            </Grid>

        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedRowItem))
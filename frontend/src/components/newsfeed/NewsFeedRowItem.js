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
import { FacebookShareButton, FacebookShareCount } from "react-share";
import ShareIcon from '@material-ui/icons/Share';
import Button from '@material-ui/core/Button'
import FacebookIcon from '@material-ui/icons/Facebook';

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
                            {(article.publisher).substring(0, 20)}
                        </Typography>
                        <Typography className={classes.subtitleRight}>
                            {moment(`${article.publish_date}`).fromNow()}
                        </Typography>
                    </span>
                    <span className={classes.alignLeft} >
                        <ArticleVote articleId={article.id} />
                    </span>
                    <p className={classes.positivity} style={{ display: 'inline-block', width: '50%', color: score > 70 ? 'green' : score > 50 ? 'orange' : 'red' }}>
                        {score}%
                            <Hidden lgDown>
                            {" Positive"}
                        </Hidden>
                    </p>

                    <div style={{ display: 'inline-block', width: '30%', 'height': '8px' }}>
                        <FacebookShareButton url={article.url} quote={article.title} className="share">
                            <Button style={{ border: '1px solid blue', height: '35px', marginTop: '0px', backgroundColor: 'rgba(255,255,255,1)' }}>
                                Share <FacebookIcon style={{ height: '20px' }} />
                            </Button>
                        </FacebookShareButton>
                    </div>
                    
                </Paper>
            </Grid>

        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedRowItem))
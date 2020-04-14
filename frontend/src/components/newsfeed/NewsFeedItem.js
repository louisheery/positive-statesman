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
import { FacebookShareButton } from "react-share";
import Button from '@material-ui/core/Button'
import FacebookIcon from '@material-ui/icons/Facebook';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/newsfeed/NewsFeedItem.js';

class NewsFeedItem extends Component {

    render() {
        const { classes, article } = this.props;
        var score = Math.round(((article.sentiment_score + 1) * 100 / 2));

        var headerItemStyle = { background: `-webkit-linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("${article.image_url}")`, backgroundSize: '100% 100%' };
        var rowItemStyle = { background: `-webkit-linear-gradient(${this.props.itemColor}, rgba(0, 0, 0, 0.3))`, backgroundSize: '100% 100%' }

        return (
            <Grid item xs={12} sm={6} md={4}>
                <Paper className={classes.paper} style={this.props.isHeaderItem ? headerItemStyle : rowItemStyle} square={true}>
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

                    
                        <p className={classes.positivity} style={{ display: 'inline-block', width: '40%', color: score > 70 ? 'green' : score > 50 ? 'orange' : 'red' }}>
                            {score}%
                            <Hidden mdDown>
                                {" Positive"}
                            </Hidden>
                        </p>

                    <div  style={{ display: 'inline-block', width: '30%', 'height': '8px'}}>
                        <FacebookShareButton url={article.url} quote={article.title} className="share">
                            <Button style={{ border: '1px solid blue', height: '35px', marginTop: '0px', backgroundColor: 'rgba(255,255,255,1)'}}>
                        Share <FacebookIcon style={{height: '20px'}} />
                        </Button>
                        </FacebookShareButton>
                    </div>

                </Paper>
            </Grid>

        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedItem))
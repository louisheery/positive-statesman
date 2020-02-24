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

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/newsfeed/NewsFeedHeaderItem.js';

class NewsFeedHeaderItem extends Component {

    render() {

        var itemWidth;
        switch (this.props.width) {
            case 'xs':
                itemWidth = 12;
                break
            case 'sm':
            case 'md':
                itemWidth = 6;
                break
            default:
                itemWidth = 4;
                break;
        }

        const { classes, article } = this.props;

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
            <Grid item xs={itemWidth}>
                <Paper className={classes.paper} style={{ background: `-webkit-linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("${article.image_url}")`, backgroundSize: '100% 100%' }} square={true}>
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
                        <p className={classes.positivity} style={positivityTextStyle}>
                            {positivityScorePcnt}%
                            <Hidden smDown>
                                {" Positive"}
                            </Hidden>
                        </p>
                    </span>
                </Paper>
            </Grid>

        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedHeaderItem))
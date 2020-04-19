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

import { publisherDictionary } from '../Settings'

class NewsFeedItem extends Component {

    //state = { src: null };

    constructor(props) {
        super(props)
        this.state = {
            src: null
        }
    }

    componentDidMount() {

        const imageLoader = new Image();
        imageLoader.src = this.props.article.image_url;

        imageLoader.onload = () => {
            this.setState({ src: imageLoader.src });
        };
    }


    vlookup(matrix, origin, destination, publisher) {
        for (var key in matrix) {
            if (matrix[key][origin] == publisher) {
                return matrix[key][destination];
            }
        }
        return '';
    }


    render() {
        const { classes, article } = this.props;
        var score = Math.round(((article.sentiment_score + 1) * 100 / 2));

        var headerItemStyle = { backgroundImage: `-webkit-linear-gradient(rgba(50,50,50, 0.5), rgba(0,0,0,0.5)), url("${this.state.src || ''}")`, backgroundSize: '100% 100%'};
        //var headerItemStyle = { background: `-webkit-linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.3)), url("${article.image_url}")`, backgroundSize: '100% 100%' };
        var rowItemStyle = { backgroundImage: `-webkit-linear-gradient(${this.props.itemColor}, rgba(0, 0, 0, 0.3)), url("${this.state.src || ''}")`, backgroundSize: '100% 100%' };


        return (
            <Grid item xs={12} sm={6} md={4}>
                <Paper className={classes.paper} style={this.props.isHeaderItem ? headerItemStyle : rowItemStyle} square={true}>
                    <Link href={article.url}>
                        <Typography variant='subtitle1' className={classes.title} >
                            {article.title}
                        </Typography>
                    </Link>

                    <span>
                        <Link href={`/publishers/${this.vlookup(publisherDictionary, 1, 0, article.publisher)}`}>
                            <Typography className={classes.subtitleLeft}>
                                {(article.publisher).substring(0, 18)}
                            </Typography>
                        </Link>



                        <Typography className={classes.subtitleRight}>
                            {moment(`${article.publish_date}`).format('DD/MM/YY')}
                        </Typography>
                    </span>
                    <span className={classes.alignLeft} >
                        <ArticleVote articleId={article.id} />
                    </span>


                    <div className={classes.buttonDiv}>
                        <Button disabled={true} className={classes.shareButton} style={{ backgroundColor: 'white', borderColor: score > 70 ? 'green' : score > 50 ? 'orange' : 'red', color: score > 70 ? 'green' : score > 50 ? 'orange' : 'red' }}>
                            {score}%
                            <Hidden lgDown>
                                {" Positive"}
                            </Hidden>
                        </Button>
                    </div>

                    <div className={classes.buttonDiv}>
                        <FacebookShareButton url={article.url} quote={article.title} className="share">
                            <Button className={classes.shareButton}>
                                Share <FacebookIcon className={classes.fbShareIcon} />
                            </Button>
                        </FacebookShareButton>
                    </div>


                </Paper>
            </Grid>

        )
    }
}

export default withWidth()(withStyles(styles)(NewsFeedItem))
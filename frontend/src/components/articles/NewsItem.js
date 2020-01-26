import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles'
import moment from 'moment';

import styles from '../../../src/assets/styles/components/articles/NewsItem.js';

class NewsItem extends Component {

    handleClickPlaceholder(e) {
        // do nothing
        e.preventDefault();

        // Call API to register vote here
    }

    render() {

        const { classes } = this.props;

        const { Article } = this.props; // like this.props.ArticlArticleeData

        var positivityTextStyle

        var positivityScorePcnt = Math.round(((Article.sentiment_score + 1) * 100 / 2));

        if (positivityScorePcnt > 70) {
            positivityTextStyle = { color: 'green' };
        }
        else if (positivityScorePcnt > 50) {
            positivityTextStyle = { color: 'orange' };
        }
        else {
            positivityTextStyle = { color: 'red' };
        }


        var maxTitleLength = 60;

        return (
            <div>
                <Card className={classes.NewsFeedCard}>
                    <CardActionArea href={Article.url}>
                        <CardMedia
                            component="img"
                            alt=""
                            height="60"
                            image={Article.image_url}
                            title={Article.title}
                        />
                        <CardContent>
                            <Typography className={classes.title}>{(Article.title).substring(0, maxTitleLength)}</Typography>
                            <Typography className={classes.subtitle}>{Article.publisher}<span style={{float:'right'}}>{moment(`${Article.publish_date}`).format('DD/MM/YY')}</span></Typography>
                            <center>
                                <Button className={classes.voteButton} color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="happy">😀</span>
                                </Button>

                                <Button className={classes.voteButton} color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="neural">😐</span>
                                </Button>

                                <Button className={classes.voteButton} color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="sad">🙁</span>
                                </Button>

                                <br />
                                <Button className={classes.positivityScore} variant="outlined" color="primary" disableElevation disabled>
                                    <span role="img" style={positivityTextStyle}>{positivityScorePcnt}% Positivity</span>
                                </Button>
                            </center>
                        </CardContent>
                    </CardActionArea>
                </Card>

            </div>

        )
    }
}

export default withStyles(styles)(NewsItem)
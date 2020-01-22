import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { Button } from '@material-ui/core';
import { withStyles } from '@material-ui/core/styles'

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

        if (Article.ArticlePositivity > 70) {
            positivityTextStyle = { color: 'green' };
        }
        else if (Article.ArticlePositivity > 50) {
            positivityTextStyle = { color: 'orange' };
        }
        else {
            positivityTextStyle = { color: 'red' };
        }




        return (
            <div>
                <Card className={classes.NewsFeedCard}>
                    <CardActionArea href={Article.ArticleURL}>
                        <CardMedia
                            component="img"
                            alt=""
                            height="50"
                            image={'https://uc57443d2e8d1a8c5cc8e6785206.previews.dropboxusercontent.com/p/thumb/AAp872jbqNtHmM0MGe5uVCb8ee1PTgRVN3e5k7nrvikbc4LrLZZ1rsnVfcujL1zBcFTPdSZLB7Gqar_e2j9MfmAlj8WoEsyhrGxI-Y7td6gjD_9ZMs33uPU-LrYhNyU1UfADd231gtIl7PPGccjbH7Dv66ksJKK1_eLadu_hAVCbvVwBG7ne7lF0JqJ9Pwrf76EVZUHbOHi_G5FFydEvG13bRn_ZwENJ0Dp6kSPgvKlM_0QGi1X0BnxImuwuU5GK8G-B76yktt6jyNjH0Mhn1Vj1Guy7LoCOobYjB92U4RMv3dPfcFztQ6ckIRn0g3fY_A3GlHypnKrqtlONaisoxTfIGJYtmdP6qc0HAgES3JU8v4-hWFdYPWYazQYv9f8IF9FaqSNwXHSAFaQ9qNKO0ppjkqAKo6KIwg45QB_nfrO4DreTj12xgVcIw0Bc3czUaiPwbUbBQToFnJWAJGIVI6Y0/p.png?size=1024x768&size_mode=3'} // {/* image={Article.ArticleImageURL} */}
                            title={Article.ArticleTitle}
                        />
                        <CardContent>
                            <Typography className={classes.title} color="textPrimary" component="p">{Article.ArticleTitle}</Typography>
                            <Typography className={classes.title} color="textSecondary" component="p">{Article.ArticlePublisher}{"  "}{Article.ArticleDate}</Typography>
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
                                    <span role="img" style={positivityTextStyle}>{Article.ArticlePositivity}% Positivity</span>
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
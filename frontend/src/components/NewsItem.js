import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { Button } from '@material-ui/core';

class NewsItem extends Component {

    handleClickPlaceholder(e) {
        // do nothing
        e.preventDefault();

        // Call API to register vote here
    }
    
    render() {

        const { Article } = this.props; // like this.props.ArticlArticleeData

        var positivityTextStyle

        if (Article.ArticlePositivity > 70) {
            positivityTextStyle = { color: 'green'};
        }
        else if (Article.ArticlePositivity > 50) {
            positivityTextStyle = { color: 'orange'};
        }
        else {
            positivityTextStyle = { color: 'red'};
        }

        


        return (
            <div key={this.props.i} className="NewsItem">
                <Card className="NewsFeedCard">
                    <CardActionArea href={Article.ArticleURL}>
                        <CardMedia
                            component="img"
                            alt=""
                            height="150"
                            image={Article.ArticleImageURL}
                            title={Article.ArticleTitle}
                        />
                        <CardContent>
                            <Typography variant="title1" color="textPrimary" component="p">{Article.ArticleTitle}</Typography>
                            <Typography variant="body1" color="textSecondary" component="p">{Article.ArticlePublisher}</Typography>
                            <Typography variant="body1" color="textSecondary" component="p">{Article.ArticleDate}</Typography>
                            <br />
                            <Typography>
                                <center>
                                    <Button variant="outlined" color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                        <Button variant="uncontained" color="primary" disableElevation>
                                            <span role="img" aria-label="sheep">😀</span>
                                        </Button>

                                        <Button variant="uncontained" color="primary" onClick={this.handleClickPlaceholder}  disableElevation>
                                            <span role="img" aria-label="sheep">😐</span>
                                        </Button>

                                        <Button variant="uncontained" color="primary" onClick={this.handleClickPlaceholder}  disableElevation>
                                            <span role="img" aria-label="sheep">🙁</span>
                                        </Button>
                                    </Button>
                                
                                <br />
                                <br />
                                <Button className="NewsFeedCardPositivity" variant="outlined" color="primary" disableElevation disabled>
                                    <span role="img" style={positivityTextStyle}>{Article.ArticlePositivity}% Positivity</span>
                                </Button>
                                </center>
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                </Card>
            </div>

        )
    }
}

export default NewsItem
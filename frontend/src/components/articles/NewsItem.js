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
            <div>
                <Card className="NewsFeedCard">
                    <CardActionArea href={Article.ArticleURL}>
                        <CardMedia
                            component="img"
                            alt=""
                            height="50"
                            image={Article.ArticleImageURL}
                            title={Article.ArticleTitle}
                        />
                        <CardContent>
                            <Typography style={{fontSize: '10pt'}} color="textPrimary" component="p">{Article.ArticleTitle}</Typography>
                            <Typography style={{ fontSize: '10pt' }} color="textSecondary" component="p">{Article.ArticlePublisher}{"  "}{Article.ArticleDate}</Typography>
                            <center>
                                <Button style={{ padding: '0px', marginBottom: "5px", flexGrow: '0' }} variant="uncontained" color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="happy">😀</span>
                                </Button>

                                <Button style={{ padding: '0px', marginBottom: "5px", flexGrow: '0' }} variant="uncontained" color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="neural">😐</span>
                                </Button>

                                <Button style={{ padding: '0px', marginBottom: "5px", flexGrow: '0' }} variant="uncontained" color="primary" onClick={this.handleClickPlaceholder} disableElevation>
                                    <span role="img" aria-label="sad">🙁</span>
                                </Button>
                            
                                <br />
                                <Button className="NewsFeedCardPositivity" variant="outlined" color="primary" disableElevation disabled>
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

export default NewsItem
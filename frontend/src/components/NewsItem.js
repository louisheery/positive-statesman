import React, { Component } from 'react';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';

class NewsItem extends Component {
    render() {

        const { Article } = this.props; // like this.props.ArticlArticleeData
        return (
            <div key={this.props.i} className="NewsItem">
                <Card>
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
                        </CardContent>
                    </CardActionArea>
                </Card>
            </div>

        )
    }
}

export default NewsItem
import React, { Component } from 'react';
import NewsItem from './NewsItem';
import articles from '../data/articles';
import Grid from '@material-ui/core/Grid';

class NewsFeed extends Component {

    render() {

        var numberOfColumns;

        if (window.innerWidth < 700) {
            numberOfColumns = 12;
        }
        else if (window.innerWidth < 1400) {
            numberOfColumns = 6;
        }
        else {
            numberOfColumns = 3;
        }

        return (
        // NewsFeed = ClassName
            <div className="NewsFeedGrid">
                <Grid container spacing={3}>
                    {
                        articles.Articles.map((article, i) => {
                            return (
                                <Grid item xs={12} sm={numberOfColumns}>
                                    <NewsItem key={i} Article={article} />
                                </Grid>
                            );
                        })
                    }
                </Grid>
            </div>


        )
    }
}

export default NewsFeed
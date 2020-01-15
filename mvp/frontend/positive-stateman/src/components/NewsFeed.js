import React, { Component } from 'react';
import NewsItem from './NewsItem';
import articles from '../data/articles'

class NewsFeed extends Component {
    render() {
        return (
            <div className="NewsFeed">
                {
                    articles.Top100Articles.map((article, i) => {
                        return (
                            <NewsItem key={i} Article={article} />
                        );
                    })
                }
            </div>


        )
    }
}

export default NewsFeed
import React, { Component } from 'react';
import NewsItem from './NewsItem';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { fetchArticles } from '../../apiIntegration';
import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/articles/NewsFeedRow.js';

class NewsFeedRow extends Component {

    constructor(props) {
        super(props)

        this.state = {
            rowArticles: [],  // articles to be displayed in row

        }
    }

    async componentDidMount() {
        // 1. Call API
        // 2. Receive JSON from API of article list
        // 3. Update State to reflect JSON data
        /*
                fetch(PROXYURL + API + "/" + this.props.newsFeedRow, { mode: 'cors' })
                    .then(response => response.json())
                    .then(rowArticles => this.setState({ rowArticles }));
        
        */

        var fetchedArticles = await fetchArticles(this.props.newsFeedRow)
        this.setState({ rowArticles: fetchedArticles })


    }

    render() {

        const { classes } = this.props;

        return (
            <div className={classes.container}>
                <Typography variant="h5">{this.props.newsFeedRowTitle}</Typography>

                <div>
                    <GridList cols={5} style={{ flexWrap: 'nowrap', transform: 'translateZ(0)' }}>
                        {
                            this.state.rowArticles.map((article, i) => {
                                return (

                                    <GridListTile style={{ height: '220px', width: '250px', padding: '10px' }} key={Math.random()}>

                                        <NewsItem key={this.props.i} Article={article} />

                                    </GridListTile>
                                )
                            }).sort((a, b) => (a.sentiment_score > b.sentiment_score) ? 1 : -1)
                        }
                    </GridList>
                </div>
            </div>


        )
    }
}

export default withStyles(styles)(NewsFeedRow)

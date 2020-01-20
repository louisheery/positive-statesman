import React, { Component } from 'react';
import NewsItem from './NewsItem';
import articles from '../../data/articles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import Typography from '@material-ui/core/Typography';
import { fetchArticles } from '../apiIntegration';

const API = 'http://positive-statesman-api.azurewebsites.net'
const PROXYURL = "https://cors-anywhere.herokuapp.com/";

class NewsFeed extends Component {

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
        console.log("HI-->", this.state.rowArticles)

        return (
            // NewsFeed = ClassName
            <div style={{ display: 'fixed', flexWrap: 'nowrap',  overflow: 'show', backgroundColor: 'white' }}>
                <Typography variant="h5">{this.props.newsFeedRowTitle}</Typography>
                
                <div>
                    <GridList cols={5} style={{ flexWrap: 'nowrap', transform: 'translateZ(0)' }}>
                        {
                            this.state.rowArticles.map((article, i) => {
                                return (
                                    
                                    <GridListTile style={{height: '220px', width: '250px', margin: '10px'}} key={Math.random()}>

                                        <NewsItem key={this.props.i} Article={article} />

                                    </GridListTile>
                                )
                            })
                        }
                    </GridList>
                </div>
            </div>


        )
    }
}

export default NewsFeed
// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import CircularProgress from '@material-ui/core/CircularProgress'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Search.js'

// INTERNAL REACT COMPONENTS
import NewsFeedItem from '../newsfeed/NewsFeedItem'

// API
import { searchArticle } from '../../apiIntegration.js'

// QUERY STRING
import queryString from "query-string"
import { wait } from '@testing-library/react'

// searchArticle(this.state.input).then((response) => { this.props.history.push({ pathname: "/search/", state: { searchResults: response } }) })


class Search extends Component {

    constructor(props) {
        super(props)
        this.state = {
            searchQuery: "",
            searchResults: [],
            finishedLoading: false,

        }
    }

    componentDidMount = () => {
        this.executeSearch()
    }

    componentDidUpdate = (prevProps) => {
        if (this.props.location.search !== prevProps.location.search) {
            this.setState({ finishedLoading: false })
            this.executeSearch()
        }
    }

    executeSearch = () => {
        const searchQuery = queryString.parse(this.props.location.search).q
        if (searchQuery)
            searchArticle(searchQuery).then((response) => { this.setState({ searchResults: response !== null ? response : [], finishedLoading: true, searchQuery: searchQuery }) })
        else
            this.setState({ searchResults: [], finishedLoading: true, searchQuery: "" })
    }

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    Search Results
                </Typography>
                <Grid container>
                    {this.state.finishedLoading ? this.state.searchResults.length === 0 ?
                        <Grid className={classes.loadingIcon} container item justify="center" alignItems="center" xs={12}>
                            <Typography>{"Sorry, we couldn't find articles in our database relating to \"" + this.state.searchQuery + "\"."} </Typography></Grid> :
                        this.state.searchResults.map((article, i) => {
                            return <NewsFeedItem key={i} article={article} isHeaderItem={false} />
                        })

                        :
                        <Grid className={classes.loadingIcon} container item justify="center" alignItems="center" xs={12}>
                            <CircularProgress />
                        </Grid>
                    }
                </Grid>

            </div>
        )
    }
}

export default withRouter(withStyles(styles)(Search))
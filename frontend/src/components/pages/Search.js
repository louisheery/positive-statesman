// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Search.js'

// INTERNAL REACT COMPONENTS
import NewsFeedRowItem from '../newsfeed/NewsFeedRowItem';




class Search extends Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    Search Results
                </Typography>
                <Grid container>
                    {this.props.location.state.searchResults.map((article, i) => {
                        return <NewsFeedRowItem key={i} article={article} />
                    })
                    }
                </Grid>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(Search))
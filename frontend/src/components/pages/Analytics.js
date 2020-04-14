// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Analytics.js'
import Hidden from '@material-ui/core/Hidden'

// COMPONENTS
import TimeSeries from '../analytics/TimeSeries'
import Map from '../analytics/Map'


class Analytics extends Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    Analytics
                </Typography>
                <Grid container justify="center">
                    <Map />
                </Grid>
                <Hidden xsDown>
                    <Grid container justify="center">
                        <TimeSeries param="categories" title="Category Positivity" description="This graph shows the development of the average news coverage positivity per category over the past 7 days." />
                        <TimeSeries param="locations" title="Region Positivity" description="This graph shows the development of the average news coverage positivity per continent over the past 7 days." />
                    </Grid>
                </Hidden>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(Analytics))
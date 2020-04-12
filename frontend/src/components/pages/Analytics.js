// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Analytics.js'

// COMPONENTS
import TimeSeries from '../analytics/TimeSeries'
import Map from '../analytics/Map'

// API
import { getTimeSeriesData } from "../../apiIntegration"


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
                <Grid container justify="center">
                    <TimeSeries param="categories" />
                    <TimeSeries param="locations" />
                </Grid>
                */}
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(Analytics))
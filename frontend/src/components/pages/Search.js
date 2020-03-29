// REACT LIBRARIES
import React, { Component } from 'react'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import withWidth from '@material-ui/core/withWidth'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/Search.js';




class Search extends Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    Search Results
                </Typography>
            </div>
        )
    }
}

export default withWidth()(withStyles(styles)(Search))
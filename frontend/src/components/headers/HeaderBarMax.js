// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

// MATERIAL UI
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Hidden from '@material-ui/core/Hidden'
import MenuIcon from '@material-ui/icons/Menu'
import IconButton from '@material-ui/core/IconButton'
import Typography from '@material-ui/core/Typography'

// COMPONENTS
import CategoryBar from './CategoryBar'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/headers/HeaderBarMax.js';


class HeaderBarMax extends Component {

    render() {
        const { classes } = this.props
        return (
            <div>
                <AppBar className={classes.appBar} position="fixed">
                    <Toolbar>
                        <Typography variant="h5">
                            The Positive Statesman
                        </Typography>
                        <Hidden smUp>
                            <IconButton color="inherit">
                                <MenuIcon />
                            </IconButton>
                        </Hidden>
                    </Toolbar>
                    <CategoryBar />
                </AppBar>
            </div>
        )
    }
}

export default withStyles(styles)(HeaderBarMax)



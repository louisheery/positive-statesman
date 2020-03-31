// REACT LIBRARIES
import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom'

// MATERIAL UI
import Tab from '@material-ui/core/Tab'
import Tabs from '@material-ui/core/Tabs'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../assets/styles/components/headers/CategoryBar.js';


class CategoryBar extends Component {

    otherTabs = ['/login', '/signup', '/profile']

    render() {
        const { classes } = this.props
        return (
            <div>
                <Tabs
                    className={classes.tabs}
                    value={this.otherTabs.includes(this.props.location.pathname) ? '/' : this.props.location.pathname}
                    defaultValue={"/"}
                    variant="scrollable"
                >
                    <Tab className={classes.tab} component={Link} to="/" value={"/"} label="Home" />
                    <Tab className={classes.tab} component={Link} to={'/business'} value="/business" label="Business" />
                    <Tab className={classes.tab} component={Link} to={'/politics'} value="/politics" label="Politics" />
                    <Tab className={classes.tab} component={Link} to={'/sport'} value="/sport" label="Sport" />
                    <Tab className={classes.tab} component={Link} to={'/arts'} value="/arts" label="Arts" />
                    <Tab className={classes.tab} component={Link} to={'/science'} value="/science" label="Science" />
                </Tabs>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(CategoryBar))
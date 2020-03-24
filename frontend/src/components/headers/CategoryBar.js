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

    render() {
        const { classes } = this.props
        return (
            <div>
                <Tabs
                    className={classes.tabs}
                    value={this.props.location.pathname}
                    variant="scrollable"
                >
                    <Tab className={classes.tab} component={Link} to="/" value={"/"} label="Home" />
                    <Tab className={classes.tab} component={Link} to={'/categories/business'} value="/categories/business" label="Business" />
                    <Tab className={classes.tab} component={Link} to={'/categories/politics'} value="/categories/politics" label="Politics" />
                    <Tab className={classes.tab} component={Link} to={'/categories/sport'} value="/categories/sport" label="Sport" />
                    <Tab className={classes.tab} component={Link} to={'/categories/arts'} value="/categories/arts" label="Arts" />
                    <Tab className={classes.tab} component={Link} to={'/categories/science'} value="/categories/science" label="Science" />
                </Tabs>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(CategoryBar))
// REACT LIBRARIES
import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom'

// MATERIAL UI
import Tab from '@material-ui/core/Tab'
import Tabs from '@material-ui/core/Tabs'

import {categoryBarTabs} from '../Settings'

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
                    value={this.props.location.pathname.slice(0, 12) === "/categories/" || this.props.location.pathname.length === 1 ? this.props.location.pathname : false}
                    variant="scrollable"
                >
                    <Tab className={classes.tab} component={Link} to="/" value={"/"} label="Home" />

                    {categoryBarTabs.map((cat, i) => {
                        return <Tab className={classes.tab} component={Link} to={`/categories/${cat}`} value={`/categories/${cat}`} label={cat.replace(/^\w/, c => c.toUpperCase())} key={i} />
                    })}

                </Tabs>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(CategoryBar))
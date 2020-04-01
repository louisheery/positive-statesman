// REACT LIBRARIES
import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom'

// MATERIAL UI
import Tab from '@material-ui/core/Tab'
import Tabs from '@material-ui/core/Tabs'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../assets/styles/components/headers/CategoryBar.js';

const CATEGORIES = ["business",
                    "politics",
                    "sport",
                    "arts",
                    "science",
                    "technology",
                    "travel"]

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

                    {CATEGORIES.map((cat, i) => {
                        return <Tab className={classes.tab} component={Link} to={`/categories/${cat}`} value={`/categories/${cat}`} label={cat.replace(/^\w/, c => c.toUpperCase())} key={i}/>
                    })}
                    
                </Tabs>
            </div>
        )
    }
}

export default withRouter(withStyles(styles)(CategoryBar))
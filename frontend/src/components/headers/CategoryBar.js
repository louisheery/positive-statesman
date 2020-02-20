// REACT LIBRARIES
import React, { Component } from 'react';
import { Link } from 'react-router-dom'

// MATERIAL UI
import Tab from '@material-ui/core/Tab'
import Tabs from '@material-ui/core/Tabs'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../assets/styles/components/headers/CategoryBar.js';


class CategoryBar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            tabValue: "top"
        }
    }

    handleChangeTabs = (event, newValue) => {
        this.setState({tabValue: newValue})
    }

    render() {
        const { classes } = this.props
        return (
            <div>
                <Tabs 
                    className={classes.tabs} 
                    onChange={this.handleChangeTabs}
                    value={this.state.tabValue}
                    variant="fullWidth"
                >
                    <Tab component={Link} to="/" value={"top"} label="Top Stories"  />
                    <Tab component={Link} to={'/business'} value="/business" label="Business" />
                    <Tab component={Link} to={'/politics'} value="/politics" label="Politics" />
                    <Tab component={Link} to={'/sport'} value="/sport" label="Sport" />
                    <Tab component={Link} to={'/arts'} value="/arts" label="Arts" />
                </Tabs>
            </div>
        )
    }
}

export default withStyles(styles)(CategoryBar)
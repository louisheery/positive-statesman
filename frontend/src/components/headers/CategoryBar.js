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
                    <Tab label="Top Stories" component={Link} value={"top"} to="/" />
                    <Tab label="Business" component={Link} value={"business"} to="/business" />
                    <Tab label="Politics" component={Link} value={"politics"} to="/politics" />
                    <Tab label="Sports" component={Link} value={"sports"} to="/sports" />
                    <Tab label="Culture" component={Link} value={"culture"} to="/culture" />
                </Tabs>
            </div>
        )
    }
}

export default withStyles(styles)(CategoryBar)
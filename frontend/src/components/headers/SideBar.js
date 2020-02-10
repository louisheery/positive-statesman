import React, { Component } from 'react';
import Drawer from '@material-ui/core/Drawer';
import Button from '@material-ui/core/Button';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';


import { withStyles } from '@material-ui/core/styles'

import styles from '../../../src/assets/styles/components/headers/SideBar.js';


function a11yProps(index) {
    return {
        id: `scrollable-auto-tab-${index}`,
        'aria-controls': `scrollable-auto-tabpanel-${index}`,
    };
}


class SideBar extends Component {

    constructor(props) {
        super(props);
        this.state = {
        };
    }



    render() {

        const { classes } = this.props;


        return (
            
            <Drawer open={true}>
                
            </Drawer>
            
        )
    }
}

export default withStyles(styles)(SideBar)
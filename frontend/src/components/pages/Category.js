import React, { Component } from 'react';


import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/pages/Category.js';


class Category extends Component {


    render() {

        const { classes } = this.props;
        
        return (
            <div>
                Category Page
            </div>
        )
    }
}

export default withStyles(styles)(Category)

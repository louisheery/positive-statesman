import React, { Component } from 'react';
import Ticker from 'react-ticker'
import Typography from '@material-ui/core/Typography'
import { withStyles } from '@material-ui/core/styles'

import styles from '../../../src/assets/styles/components/headers/NewsTickerBar.js';

class NewsTickerBar extends Component {

    render() {

        const { classes } = this.props;


        return (
            <div className={classes.grid}>
                <Ticker>
                    {({ index }) => (
                        <div style={{ backgroundColor: '#e3f3f4', marginTop: '10px', marginBottom: '10px' }}>
                            <Typography variant="body1" style={{ textDecoration: "None", backgroundColor: '#e3f3f4', paddingTop: '10px', paddingBottom: '10px' }}>Business  60%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Politics  30%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sport  70%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Culture  80%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Typography>
                        </div>
                    )}
                </Ticker>
            </div>
        )
    }
}

export default withStyles(styles)(NewsTickerBar)

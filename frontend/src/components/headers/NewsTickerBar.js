// REACT LIBRARIES
import React, { Component } from 'react';
import Ticker from 'react-ticker'

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/headers/NewsTickerBar.js';

class NewsTickerBar extends Component {

    render() {

        const { classes } = this.props;


        return (
            <div className={classes.grid}>
                <Ticker>
                    {/* Currently only 1 div component, but index could map to 1 div per article type */}
                    {({ index }) => (
                        <div className={classes.tickerDiv}>
                            <Typography variant="body1" className={classes.tickerText}>Business  60%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Politics  30%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sport  70%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Culture  80%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Typography>
                        </div>
                    )}
                </Ticker>
            </div>
        )
    }
}

export default withStyles(styles)(NewsTickerBar)

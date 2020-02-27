// REACT LIBRARIES
import React, { Component } from 'react';

// NON-REACT LIBRARIES & COMPONENTS
import Fab from '@material-ui/core/Fab';
import FeedbackIcon from '@material-ui/icons/Feedback';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/popups/FeedbackButton.js';

class FeedbackButton extends Component {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.fabDiv}>
                <Fab variant="extended" href="https://forms.gle/EfVfZNP7Zp8Pe3jd8" target="_blank" color="secondary" aria-label="add" className={classes.fabButton}>
                    <FeedbackIcon className={classes.fabIcon} />
                    Give Feedback!
            </Fab>
            </div>
        )
    }
}

export default withStyles(styles)(FeedbackButton)
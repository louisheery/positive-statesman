// REACT LIBRARIES
import React, { Component } from 'react';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import CloseIcon from '@material-ui/icons/Close';
import Alert from '@material-ui/lab';
import MuiAlert from '@material-ui/lab/Alert';
import Typography from '@material-ui/core/Typography';
import Popover from '@material-ui/core/Popover';
import moment from 'moment';

// STYLES
import { withStyles } from '@material-ui/core/styles';

// API
import { userFeedback } from '../../apiIntegration.js'

import styles from '../../assets/styles/components/newsfeed/ArticleVote.js';



class ArticleVote extends Component {

    constructor(props) {
        super(props)

        this.state = {
            open: false,
        }
    }

    render() {

        const { classes } = this.props;

        return (
            <div>
                <Popover
                    id={1}
                    open={this.state.open}
                    anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'center',
                    }}
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'center',
                    }}
                    onClose={() => this.setState({ open: false })}
                >
                    <Typography style={{ padding: '10px' }}>Vote Submitted!</Typography>
                </Popover>


                <IconButton className={classes.voteIcon} aria-label="positiveVote" onClick={() => { userFeedback(this.props.articleId, "positive"); this.setState({ open: true }); }}>
                    <span role="img" aria-label="happy">😀</span>
                </IconButton>
                <IconButton className={classes.voteIcon} aria-label="neutralVote" onClick={() => { userFeedback(this.props.articleId, "neutral"); this.setState({ open: true }); }}>
                    <span role="img" aria-label="neural">😐</span>
                </IconButton>
                <IconButton className={classes.voteIcon} aria-label="negativeVote" onClick={() => { userFeedback(this.props.articleId, "negative"); this.setState({ open: true }); }}>
                    <span role="img" aria-label="sad">🙁</span>
                </IconButton>
            </div>
        )
    }
}

export default withStyles(styles)(ArticleVote)
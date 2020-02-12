import React, { Component } from 'react';
import IconButton from '@material-ui/core/IconButton';

import { withStyles } from '@material-ui/core/styles';

import styles from '../../assets/styles/components/articles/ArticleVote.js';

class ArticleVote extends Component {

    render() {

        const { classes } = this.props;

        return (
            <div>
                <IconButton className={classes.voteIcon}>
                    <span role="img" aria-label="happy">😀</span>
                </IconButton>
                <IconButton className={classes.voteIcon}>
                    <span role="img" aria-label="neural">😐</span>
                </IconButton>
                <IconButton className={classes.voteIcon}>
                    <span role="img" aria-label="sad">🙁</span>
                </IconButton>
            </div>
        )
    }
}

export default withStyles(styles)(ArticleVote)
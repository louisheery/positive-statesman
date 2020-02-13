// REACT LIBRARIES
import React, { Component } from 'react';

// EXTERNAL REACT LIBRARIES & COMPONENTS
import IconButton from '@material-ui/core/IconButton';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import { userFeedback } from '../../apiIntegration.js'

import styles from '../../assets/styles/components/newsfeed/ArticleVote.js';

class ArticleVote extends Component {

    render() {

        const { classes } = this.props;

        return (
            <div>
                <IconButton className={classes.voteIcon} onClick={() => userFeedback(this.props.articleId, "positive")}>
                    <span role="img" aria-label="happy">😀</span>
                </IconButton>
                <IconButton className={classes.voteIcon} onClick={() => userFeedback(this.props.articleId, "neutral")}>
                    <span role="img" aria-label="neural">😐</span>
                </IconButton>
                <IconButton className={classes.voteIcon} onClick={() => userFeedback(this.props.articleId, "negative")}>
                    <span role="img" aria-label="sad">🙁</span>
                </IconButton>
            </div>
        )
    }
}

export default withStyles(styles)(ArticleVote)
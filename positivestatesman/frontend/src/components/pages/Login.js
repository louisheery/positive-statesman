import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import GoogleButton from 'react-google-button';
import HeaderBar from '../headers/HeaderBar';


import { withStyles } from '@material-ui/core/styles';

import styles from '../../../src/assets/styles/components/pages/Login.js';

class Login extends React.Component {

    render() {

        const { classes } = this.props;
        
        return (
            <div>
                <Container className={classes.container} maxWidth="lg" align="center" >
                    <Typography className={classes.header} variant="h5" align="center" component="div">
                        Login to The Positive Statesman
        
                <div className={classes.GoogleButton} align="center">
                            <GoogleButton onClick={() => alert('API magic happens now')} />
                        </div>
                    </Typography>
                </Container>
            </div>
        )
    }
}

export default withStyles(styles)(Login)

// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import GoogleButton from 'react-google-button';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/pages/Logout.js';

class Logout extends React.Component {

    componentDidMount() {
        ReactGA.pageview(`loginpage`);
    }

    render() {

        const { classes } = this.props;

        return (
            <div>
                <Container className={classes.container} maxWidth="lg" align="center" >
                    <Typography className={classes.header} variant="h5" align="center" component="div">
                        Login to The Positive Statesman

                        {/* Google Button should Interface with Google Login API */}
                        <div className={classes.GoogleButton} align="center">
                            <GoogleButton onClick={() => alert('API magic happens now')} />
                        </div>
                    </Typography>
                </Container>
            </div>
        )
    }
}

export default withStyles(styles)(Logout)

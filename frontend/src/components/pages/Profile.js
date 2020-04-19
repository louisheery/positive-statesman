// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';


// REDUX LIBRARIES
import { connect } from 'react-redux';
import { Redirect } from "react-router-dom";
import ProfileTable from '../profile/ProfileTable';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Profile.js';

class Profile extends React.Component {

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
    }

    render() {

        const { classes } = this.props;

        if (this.props.isLoggedIn == false) {
            return <Redirect to="/" />;
        }


        return (
            <div>

                <Container className={classes.container} maxWidth="lg" align="center" >


                    <Typography className={classes.title} variant="h5" align="center" component="div">
                        Profile
                    </Typography>

                    <div>
                        <ProfileTable tableType={"category"} />

                    </div>


                    <div>
                        <ProfileTable tableType={"publisher"} />

                    </div>


                </Container>
            </div>


        )
    }
}

const mapStateToProps = state => {
    return {
        isLoggedIn: state.reducer.isLoggedIn,
    };
};

export default connect(mapStateToProps, {})(withStyles(styles)(Profile))
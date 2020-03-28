// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

// REDUX
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { logIn } from '../../store/actions/actions'; 

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Login.js';
import { Link } from '@material-ui/core';

class Login extends React.Component {

    state = {
        username: '',
        password: '',
    }

    static propTypes = {
        logIn: PropTypes.func.isRequired,
        isLoggedIn: PropTypes.bool,
    }

    componentDidMount() {
        ReactGA.pageview(`loginpage`);
    }

    onSubmit = (e) => {
        e.preventDefault();
        console.log('login clicked');
        this.props.logIn( this.state.username, this.state.password );
    }

    onChange = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }

    render() {

        const { username, password } = this.state;

        const { classes } = this.props;

        if (this.props.isLoggedIn == true) {
            return <Redirect to="/" />;
        }

        return (
            <div>
                <Container className={classes.container} maxWidth="lg" align="center" >
                    <Link href="/signup" to={"/signup"}>
                        <Typography>Not Registered? Signup Here</Typography>
                    </Link>

                    <Typography className={classes.header} variant="h5" align="center" component="div">
                        Login to The Positive Statesman

                        <form onSubmit={this.onSubmit}>
                            <div>
                                <label>Username</label>
                                <input
                                    type="text"
                                    name="username"
                                    onChange={this.onChange}
                                    value={username}
                                />
                            </div>

                            <div>
                                <label>Password</label>
                                <input
                                    type="text"
                                    name="password"
                                    onChange={this.onChange}
                                    value={password}
                                />
                            </div>

                            <div>
                                <button type="submit">Login</button>
                            </div>

                        </form>
                    </Typography>
                </Container>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        isLoggedIn: state.isLoggedIn
    };
};

export default connect(mapStateToProps, { logIn })(withStyles(styles)(Login))

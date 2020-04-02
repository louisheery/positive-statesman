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
import { signupUser } from '../../store/actions/actions'; 

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../assets/styles/components/pages/Signup.js';
import { Link } from '@material-ui/core';

class Signup extends React.Component {

    state = {
        username: '',
        email: '',
        password: '',
    }

    static propTypes = {
        signupUser: PropTypes.func.isRequired,
        isLoggedIn: PropTypes.bool,
    }

    componentDidMount() {
        ReactGA.pageview(`signuppage`);
    }

    onSubmit = (e) => {
        e.preventDefault();
        this.props.signupUser(this.state.username, this.state.email, this.state.password);
    }

    onChange = (e) => {
        this.setState( { [e.target.name]: e.target.value })
    }

    render() {

        const { username, email, password } = this.state;

        const { classes } = this.props;

        if (this.props.isLoggedIn) {
            return <Redirect to="/" />;
        }

        return (
            <div>
                <Container className={classes.container} maxWidth="lg" align="center" >
                    <Link href="/login" to={"/login"}>
                        <Typography>Login?</Typography>
                    </Link>

                    <Typography className={classes.header} variant="h5" align="center" component="div">
                        Signup to The Positive Statesman

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
                                <label>Email</label>
                                <input
                                    type="text"
                                    name="email"
                                    onChange={this.onChange}
                                    value={email}
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
                                <button type="submit">Signup</button>
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
        isLoggedIn: state.reducer.isLoggedIn
    };
};

export default connect(mapStateToProps, { signupUser })(withStyles(styles)(Signup))


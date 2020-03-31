// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
import { checkLoggedIn } from '../store/actions/actions';

// REDUX LIBRARIES
import reducer from '../store/reducers/reducer';
import { connect, Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import store from "../store/store";
import { userData } from '../store/actions/actions';

// REACT COMPONENTS
//import HeaderBar from './headers/backup/HeaderBar'
import HeaderBar from './headers/HeaderBar'
import Home from './pages/Home'
import Category from './pages/Category'
import Login from './pages/Login'
import Logout from './pages/Logout'
import Signup from './pages/Signup'
import Profile from './pages/Profile'
import FeedbackButton from './popups/FeedbackButton';


// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../src/assets/styles/components/Root.js';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

// MATERIAL UI THEME
const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#003249'
        },
        secondary: {
            main: '#e3f3f4'
        }
    }
},
)

const categoryDictionary = {
    ART: ['/arts', 'Art, Culture & Entertainment', 'iab-qagIAB1'],
    BUSINESS: ['/business', 'Business', 'iab-qagIAB3'],
    POLITICS: ['/politics', 'Law, Government & Politics', 'iab-qagIAB11'],
    SCIENCE: ['/science', 'Science', 'iab-qagIAB15'],
    SPORT: ['/sport', 'Sport', 'iab-qagIAB17'],
    TECH: ['/tech', 'Technology', 'iab-qagIAB19'],
    TRAVEL: ['/travel', 'Travel', 'iab-qagIAB20'],
}

class Root extends Component {

    componentDidMount() {

        this.props.checkLoggedIn();

        if (this.props.isLoggedIn) {
            store.dispatch(userData());
        }

    }

    render() {
        const { classes } = this.props
        return (
            
            <Router>
                <MuiThemeProvider theme={theme}>
                    <HeaderBar location={this.props.location} />
                    <div className={classes.appBarSpacer} />

                    <Switch>
                        {
                            Object.keys(categoryDictionary).map(function (key, i) {
                                return (
                                    <Route
                                        key={i}
                                        exact path={categoryDictionary[key][0]}
                                        render={props => (
                                            <div>
                                                <Category
                                                    key={Math.random() + i}
                                                    categoryName={categoryDictionary[key][1]}
                                                    categoryId={categoryDictionary[key][2]}
                                                    {...props}
                                                />
                                            </div>
                                        )}
                                    />
                                )
                            })}
                        <Route
                            exact path="/"
                            render={props => (
                                <div>
                                    <Home
                                        key={Math.random()}
                                        categoryName={"Top Stories"}
                                        categoryId={""}
                                        {...props}
                                    />
                                </div>
                            )}
                        />

                        <Route exact path="/login" component={Login} />
                        <Route exact path="/profile" component={Profile} />
                        <Route exact path="/signup" component={Signup} />
                        <Route exact path="/logout" component={Logout} />
                        <Redirect to="/" />
                    </Switch>
                    <FeedbackButton />
                </MuiThemeProvider>
            </Router>
        )
    }
}


const mapStateToProps = state => {
    return {
        isLoggedIn: state.reducer.isLoggedIn
    };
};


const mapDispatchToProps = dispatch => {
    return {
        checkLoggedIn: () => dispatch(checkLoggedIn()),
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(withStyles(styles)(Root))
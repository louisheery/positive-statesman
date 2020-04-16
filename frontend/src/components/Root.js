// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
import { checkLoggedIn } from '../store/actions/actions';

// REDUX LIBRARIES
import { connect } from 'react-redux';

// REACT COMPONENTS
//import HeaderBar from './headers/backup/HeaderBar'
import HeaderBar from './headers/HeaderBar'
import Articles from './pages/Articles'
import Login from './pages/Login'
import Logout from './pages/Logout'
import Signup from './pages/Signup'
import Profile from './pages/Profile'
import FeedbackButton from './popups/FeedbackButton'
import Search from './pages/Search'
import Analytics from './pages/Analytics'
import List from './pages/List'
import { categoryDictionary } from './Settings';
import { publisherDictionary } from './Settings';


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



class Root extends Component {

    componentDidMount() {
        this.props.checkLoggedIn();
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
                                        exact path={`/categories/${categoryDictionary[key][0]}`}
                                        render={props => (
                                            <div>
                                                <Articles
                                                    key={Math.random() + i}
                                                    pageName={categoryDictionary[key][1]}
                                                    categoryId={categoryDictionary[key][2]}
                                                    {...props}
                                                />
                                            </div>
                                        )}
                                    />
                                )
                            })}
                         
                        {
                            Object.keys(publisherDictionary).map(function (key, i) {
                                return (
                                    <Route
                                        key={i}
                                        exact path={`/publishers/${publisherDictionary[key][0]}`}
                                        render={props => (
                                            <div>
                                                <Articles
                                                    key={Math.random() + i}
                                                    pageName={publisherDictionary[key][1]}
                                                    publisherId={publisherDictionary[key][2]}
                                                    {...props}
                                                />
                                            </div>
                                        )}
                                    />
                                )
                            })}
                        <Route path="/search/" render={props => <div><Search /></div>} />
                        <Route path="/analytics/" render={props => <div><Analytics /></div>} />
                        <Route
                            exact path="/"
                            render={props => (
                                <div>
                                    <Articles
                                        key={Math.random()}
                                        pageName={"Top Stories"}
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
                        <Route exact path="/publishers" component={List} />
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
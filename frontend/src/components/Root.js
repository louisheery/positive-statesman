// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
import { checkLoggedIn } from '../store/actions/actions';

// REDUX LIBRARIES
import reducer from '../store/reducers/reducer';
import { connect, Provider } from 'react-redux';
import store from "../store/store";
import { userFetchData } from '../store/actions/actions';

// REACT COMPONENTS
//import HeaderBar from './headers/backup/HeaderBar'
import HeaderBar from './headers/HeaderBar'
import Home from './pages/Home'
import Category from './pages/Category'
import Login from './pages/Login'
import Logout from './pages/Logout'
import Signup from './pages/Signup'
import Profile from './pages/Profile'
import FeedbackButton from './popups/FeedbackButton'
import Search from './pages/Search'
import Analytics from './pages/Analytics'


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
    ART: ['arts', 'Art, Culture & Entertainment', 'iab-qagIAB1'],
    BUSINESS: ['business', 'Business', 'iab-qagIAB3'],
    POLITICS: ['politics', 'Law, Government & Politics', 'iab-qagIAB11'],
    SCIENCE: ['science', 'Science', 'iab-qagIAB15'],
    SPORT: ['sport', 'Sport', 'iab-qagIAB17'],
    TECH: ['tech', 'Technology', 'iab-qagIAB19'],
    TRAVEL: ['travel', 'Travel', 'iab-qagIAB20'],
}

const publisherDictionary = {
    GUARDIAN: ['theguardian', 'The Guardian', ''],
    NYTIMES: ['nytimes', 'New York Times', ''],
    FTIMES: ['ft', 'Financial Times', ''],
    BLOOMBERG: ['bloomberg', 'Bloomberg', ''],
    REUTERS: ['reuters', 'Reuters', ''],
    AP: ['ap', 'Associated Press', ''],
    TIMES: ['thetimes', 'The Times', ''],
    WAPOST: ['washingtonpost', 'Washington Post', ''],
    TIMEMAG: ['time', 'Time', ''],
    WSJ: ['wsj', 'Wall Street Journal', ''],
    BBCNEWS: ['bbcnews', 'BBC News', ''],
    HUFFPOST: ['huffingtonpost', 'Huffington Post', ''],
    ATLANTIC: ['theatlantic', 'The Atlantic', ''],
    VOX: ['vox', 'Vox', ''],
}

class Root extends Component {

    componentDidMount() {

        this.props.checkLoggedIn();

        if (this.props.isLoggedIn) {
            store.dispatch(userFetchData());
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
                                        exact path={`/categories/${categoryDictionary[key][0]}`}
                                        render={props => (
                                            <div>
                                                <Category
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
                                                <Category
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
                                    <Home
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
// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
import ReactGA from "react-ga";

// REACT COMPONENTS
//import HeaderBar from './headers/backup/HeaderBar'
import HeaderBar from './headers/HeaderBar'
import Home from './pages/Home'
import Category from './pages/Category'
import Login from './pages/Login'
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
    ART: ['/arts', 'Art, Culture & Entertainment', 'iab-qaglIAB1'],
    BUSINESS: ['/business', 'Business', 'iab-qagllIAB3'],
    POLITICS: ['/politics', 'Law, Government & Politics', 'iab-qaglIAB11'],
    SCIENCE: ['/science', 'Science', 'iab-qaglIAB15'],
    SPORT: ['/sport', 'Sport', 'iab-qaglIAB17'],
    TECH: ['/tech', 'Technology', 'iab-qaglIAB19'],
    TRAVEL: ['/travel', 'Travel', 'iab-qaglIAB20'],
}

class Root extends Component {

    componentDidMount() {
        ReactGA.initialize('replace-your-trackingID-here');
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
                                        path={categoryDictionary[key][0]}
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
                        <Redirect to="/" />
                    </Switch>
                    <FeedbackButton />
                </MuiThemeProvider>
            </Router>
        )
    }
}

export default withStyles(styles)(Root)
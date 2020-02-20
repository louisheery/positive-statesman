// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

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
    ART: ['/arts', 'Art, Culture & Entertainment', 'iptc-qagIAB1'],
    BUSINESS: ['/business', 'Business', 'iptc-qagIAB3'],
    POLITICS: ['/politics', 'Law, Government & Politics', 'iab-qagIAB11'],
    SCIENCE: ['/science', 'Science', 'iptc-qagIAB15'],
    SPORT: ['/sport', 'Sport', 'iab-qagIAB17'],
    TECH: ['/tech', 'Technology', 'iptc-qagIAB19'],
    TRAVEL: ['/travel', 'Travel', 'iptc-qagIAB20'],
}

class Root extends Component {

    render() {
        const { classes } = this.props
        return (
            <Router>
                <MuiThemeProvider theme={theme}>
                    <HeaderBar location={this.props.location} />
                    <div className={classes.appBarSpacer}/>
                    <FeedbackButton />
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
                        <Route exact path="/" component={Home} />
                        <Route exact path="/login" component={Login} />
                        <Redirect to="/" />
                    </Switch>
                </MuiThemeProvider>
            </Router>
        )
    }
}

export default withStyles(styles)(Root)
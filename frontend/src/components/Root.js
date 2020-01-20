// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

// COMPONENTS
import HeaderBar from './headers/HeaderBar'
import Home from './pages/Home'
import Category from './pages/Category'

// STYLE
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

// Custom Theme
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

    constructor(props) {
        super(props);
        this.handleArticlePopupOpening = this.handleArticlePopupOpening.bind(this);
        this.state = {
            addArticlePopupIsOpen: false,
            userIsLoggedIn: false,
            loginPageDisplayed: false,
        };
    }

    handleArticlePopupOpening() {
        this.setState({ addArticlePopupIsOpen: !this.state.addArticlePopupIsOpen })
    }

    render() {
        return (
            <Router>
                <MuiThemeProvider theme={theme}>
                    <HeaderBar userIsLoggedIn={this.state.userIsLoggedIn} addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
                    <Switch>
                        {/* HeaderBar component needs to be placed here*/}
                        <Route path="/business" component={Category} />
                        <Route path="/politics" component={Category} />
                        <Route path="/sport" component={Category} />
                        <Route path="/science" component={Category} />
                        <Route path="/health" component={Category} />
                        <Route path="/gaming" component={Category} />
                        <Route path="/culture" component={Category} />
                        <Route exact path="/" component={Home} />
                        <Redirect to="/" />
                    </Switch >
                </MuiThemeProvider>
            </Router >
        )
    }
}

export default Root

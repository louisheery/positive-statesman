// REACT LIBRARIES
import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

// REACT COMPONENTS
import HeaderBar from './headers/HeaderBar'
import Home from './pages/Home'
import Category from './pages/Category'
import Login from './pages/Login'
import FeedbackButton from './popups/FeedbackButton';

// STYLES
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

    render() {
        return (
            <Router>
                <MuiThemeProvider theme={theme}>
                    <HeaderBar location={this.props.location} />
                    <FeedbackButton />
                    <Switch>
                        <Route path="/business" component={Category} />
                        <Route path="/politics" component={Category} />
                        <Route path="/sport" component={Category} />
                        <Route path="/science" component={Category} />
                        <Route path="/health" component={Category} />
                        <Route path="/gaming" component={Category} />
                        <Route path="/culture" component={Category} />
                        <Route exact path="/" component={Home} />
                        <Route exact path="/login" component={Login} />
                        <Redirect to="/" />
                    </Switch>
                </MuiThemeProvider>
            </Router>
        )
    }
}

export default Root
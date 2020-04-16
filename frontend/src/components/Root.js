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
    TECH: ['technology', 'Technology', 'iab-qagIAB19'],
    TRAVEL: ['travel', 'Travel', 'iab-qagIAB20'],
}

const publisherDictionary = {
    GUARDIAN: ['guardian', 'The Guardian', 'The%20Guardian'],
    NYTIMES: ['nytimes', 'NYTimes', 'New%20York%20Times'],
    FT: ['ft', 'FT', 'Financial%20Times'],
    BLOOMBERG: ['bloomberg', 'Bloomberg', 'Bloomberg'],
    REUTERS: ['reuters', 'Reuters', 'Reuters'],
    AP: ['ap', 'AP', 'Associated%20Press'],
    THETIMES: ['thetimes', 'The Times', 'The%20Times'],
    WASHINGTONPOST: ['washingtonpost', 'Washington Post', 'Washington%20Post'],
    AFP: ['afp', 'AFP', 'AFP'],
    ABCNEWS: ['abcnews', 'ABC News', 'ABC%20News'],
    TIME: ['time', 'Time', 'Time'],
    WSJ: ['wsj', 'Wall Street Journal', 'Wall%20Street%20Journal'],
    ECONOMIST: ['economist', 'Economist', 'The%20Economist'],
    POLITICO: ['politico', 'Politico', 'Politico'],
    BBC: ['bbc', 'BBC News', 'BBC'],
    PBS: ['pbs', 'PBS', 'PBS'],
    THEHILL: ['the hill', 'The Hill', 'The%20Hill'],
    USATODAY: ['usatoday', 'USA Today', 'USA%20Today'],
    NPR: ['npr', 'NPR', 'NPR'],
    CBSNEWS: ['cbsnews', 'CBS News', 'CBS%20News'],
    AXIOS: ['axios', 'Axios', 'Axios'],
    HUFFINGTONPOST: ['huffingtonpost', 'Huffington Post', 'Huffington%20Post'],
    NEWYORKER: ['newyorker', 'The New Yorker', 'The%20New%20Yorker'],
    NATIONALREVIEW: ['nationalreview', 'National Review', 'National%20Review'],
    SLATE: ['slate', 'Slate', 'Slate'],
    THEATLANTIC: ['theatlantic', 'The Atlantic', 'The%20Atlantic'],
    THEWEEK: ['theweek', 'The Week', 'The%20Week'],
    VANITYFAIR: ['vanityfair', 'Vanity Fair', 'Vanity%20Fair'],
    MSNBC: ['msnbc', 'MSNBC', 'MSNBC'],
    CNN: ['cnn', 'CNN', 'CNN'],
    AMERICANCONSERVATIVE: ['americanconservative', 'The American Conservative', 'The%20American%20Conservative'],
    VOX: ['vox', 'Vox', 'Vox'],
    MIC: ['mic', 'Mic', 'Mic'],
    INDEPENDENT: ['independent', 'Independent', 'Independent'],
    THESUN: ['thesun', 'The Sun', 'The%20Sun'],
    THEMETRO: ['themetro', 'The Metro', 'The%20Metro'],
    DAILYMAIL: ['dailymail', 'Daily Mail', 'Daily%20Mail'],
    TELEGRAPH: ['telegraph', 'The Telegraph', 'The%20Telegraph'],
    LATIMES: ['latimes', 'LA Times', 'Los%20Angeles%20Times'],
    CNET: ['cnet', 'CNET', 'CNET'],
    ENGADGET: ['engadget', 'Engadget', 'Engadget'],
    THEVERGE: ['theverge', 'The Verge', 'The%20Verge'],
    VICE: ['vice', 'Vice', 'Vice'],
    HOLLYWOODREPORTER: ['hollywoodreporter', 'The Hollywood Reporter', 'The%20Hollywood%20Reporter'],
    NEWSWEEK: ['newsweek', 'Newsweek', 'Newsweek'],
    FORBES: ['forbes', 'Forbes', 'Forbes'],
    SCIENCEMAG: ['sciencemag', 'Science Magazine', 'Science%20Magazine'],
    RTE: ['rte', 'RTE', 'RTE'],
    NATGEO: ['natgeo', 'National Geographic', 'National%20Geographics'],
    WANDERLUST: ['wanderlust', 'Wanderlust', 'Wanderlust'],
    SKYSPORTSNEWS: ['skysportsnews', 'Sky Sports News', 'Sky%20Sports%20News'],
    ESPN: ['espn', 'ESPN', 'ESPN'],
    THEATHLETIC: ['theathletic', 'The Athletic', 'The%20Athletic'],
    PHYSORG: ['phys.org', 'Phys.org', 'Phys.org'],
    PHYSICSWORLD: ['physicsworld', 'physicsworld.com', 'Physics%20World'],
    SKYNEWS: ['skynews', 'Sky News', 'Sky%20News'],
    TECHRADAR: ['techradar', 'TechRadar', 'TechRadar'],
    ENTERTAINMENTDAILY: ['entertainmentdaily', 'Entertainment Daily', 'Entertainment%20Daily'],
    DIGITALSPY: ['digitalspy', 'Digital Spy', 'Digital%20Spy'],
    INEWS: ['inews', 'i News', 'i%20News'],
    IGN: ['ign', 'IGN', 'IGN'],
    FRANCE24: ['france24', 'France24', 'France24'],
    DW: ['dw', 'Deutsche Welle', 'Deutsche%20Welle'],
    EURONEWS: ['euronews', 'Euro News', 'Euro%20News'],
    THELOCALITALY: ['thelocalitaly', 'The Local Italy', 'The%20Local'],
    ELPAIS: ['elpais', 'El Pais', 'El%20Pais'],
    CBC: ['cbc', 'CBC', 'CBC'],
    GLOBALNEWS: ['globalnews', 'Global News', 'Global%20News'],
    NATIONALPOST: ['nationalpost', 'National Post', 'National%20Post'],
    MSN: ['msn', 'MSN', 'MSN'],
    NBCNEWS: ['nbcnews', 'NBC News', 'NBC%20News'],
    ABCNEWSAU: ['abcnews', 'ABC News', 'ABC%20News%20au'],
    SCMP: ['scmp', 'SCMP', 'SCMP'],
    SEATTLETIMES: ['seattletimes', 'Seattle Times', 'Seattle%20Times'],
    INDEPENDENTIE: ['independentie', 'Independent IE', 'Independent%20ie'],
    EVENINGSTANDARD: ['eveningstandard', 'Evening Standard', 'Evening%20Standard'],
    WIRED: ['wired', 'Wired', 'Wired'],
    FORTUNE: ['fortune', 'Fortune', 'Fortune'],
    TECHCRUNCH: ['techcrunch', 'Techcrunch', 'Techcrunch'],
    USNEWS: ['usnews', 'US News', 'US%20News'],
}

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
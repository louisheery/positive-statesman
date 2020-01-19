import React from 'react';
import HeaderBar from './components/HeaderBar';
import NewsFeed from './components/NewsFeed';
import NewsTickerBar from './components/NewsTickerBar'
import './App.css';
import AddArticlePopup from './components/AddArticlePopup';
import { fetchArticles } from './apiIntegration';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import GoogleButton from 'react-google-button';

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

class App extends React.Component {

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
    this.setState({addArticlePopupIsOpen: !this.state.addArticlePopupIsOpen})
  }

  render() {
    return (
      <div>
        <MuiThemeProvider theme={theme}>
        <HeaderBar userIsLoggedIn={this.state.userIsLoggedIn} addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
        {(this.state.loginPageDisplayed) ? (
          <div>
              <Container maxWidth="lg" align="center" style={{marginTop: '150px'}}>
                <Typography variant="h5" align="center" component="div" style={{ backgroundColor: '#FFF', height: '100vh'}}>
                Login to The Positive Statesman
                       
                  <div align="center" style={{marginTop: '50px'}}>
                    <GoogleButton onClick={() => alert('API magic happens now')} />
                  </div>
                </Typography>
              </Container>
          </div>
          ) : ( 
            <div>
              <NewsTickerBar />
              <NewsFeed addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />
              <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
            </div>
        )}
        
        </MuiThemeProvider>
     </div>
    )
  }
}

export default App;
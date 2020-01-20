import React from 'react';
import './App.css';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import HomePage from './containers/HomePage'
//import LoginPage from './containers/LoginPage'

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

  render() {
    return (
      <div>
        <MuiThemeProvider theme={theme}>
        <HomePage />
        </MuiThemeProvider>
     </div>
    )
  }
}

export default App;
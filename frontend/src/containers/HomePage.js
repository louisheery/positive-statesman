import React from 'react';
import NewsFeed from '../components/NewsFeed';
import NewsTickerBar from '../components/NewsTickerBar'
import '../App.css';
import AddArticlePopup from '../components/AddArticlePopup';
import HeaderBar from '../components/HeaderBar';

class HomePage extends React.Component {

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
            <div>
                <HeaderBar userIsLoggedIn={this.state.userIsLoggedIn} addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
                <NewsTickerBar />
                <NewsFeed addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} />
                <AddArticlePopup addArticlePopupIsOpen={this.state.addArticlePopupIsOpen} handleArticlePopupOpening={this.handleArticlePopupOpening} />
            </div>
        )
    }
}

export default HomePage;
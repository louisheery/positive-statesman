import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import CircularProgress from '@material-ui/core/CircularProgress';
import fetchedArticle from '../data/fetchedArticle';
import NewsItem from './NewsItem';

class AddArticlePopup extends Component {

    constructor(props){
        super(props);

        this.state = {
            currentArticleURL: "",
            isEnterURLDisplayed: true,
            isLoadingDisplayed: false,
            isFailedDisplayed: false,
            isSuccessDisplayed: false,
        }
    }

    waitTimer(ms) {
        var start = new Date().getTime();
        var end = start;
        while (end < start + ms) {
            end = new Date().getTime();
        }
    }

    handleClickAddArticle = () => {
        


            //show loading
            this.setState({ isEnterURLDisplayed: false})
            // wait 2 seconds
            

        if (this.state.currentArticleURL === "found") {
            this.setState({isLoadingDisplayed: true })
            // Send article URL to backend
            // I.e. Send this.state.currentArticleURL
            // WAIT FOR API CALL TO HAPPEN
            this.setState({ isLoadingDisplayed: false, isSuccessDisplayed: true})

        } else {
            this.setState({ isLoadingDisplayed: true })
            // Send article URL to backend
            // I.e. Send this.state.currentArticleURL
            // WAIT FOR API CALL TO HAPPEN
            this.setState({ isLoadingDisplayed: false, isFailedDisplayed: true })
        }

        // Close Popup
    }

    handleClickCloseBox = () => {
        
        // Close Popup
        this.setState({ isEnterURLDisplayed: true, isLoadingDisplayed: false, isSuccessDisplayed: false, isFailedDisplayed: false })
        this.props.handleArticlePopupOpening()
        
    }

    render() {

        let dialogContent;

        if (this.state.isEnterURLDisplayed) {

            dialogContent = (
                <div>
                <DialogTitle id="form-dialog-title">Add Article</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            Enter the URL of the News Article you would like to add:
                            </DialogContentText>

                        <TextField fullWidth placeholder="e.g. http://www.bbc.co.uk/108791 -OR- [TRY: 'found']" onChange={e => this.setState({ currentArticleURL: e.target.value })} />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleClickAddArticle}>Add Article</Button>
                        <Button onClick={this.handleClickCloseBox}>Cancel</Button>
                    </DialogActions>
                </div>
            )
        }

        if (this.state.isLoadingDisplayed) {

            dialogContent = (
                <div>
                    <DialogContent fullWidth="true" maxWidth='lg'>
                        <DialogTitle id="form-dialog-title">Add Article</DialogTitle>
                        <center>
                        <DialogContentText>
                            Loading
                        </DialogContentText>
                        <CircularProgress />
                        </center>
                    </DialogContent>
                
                <DialogActions>
                    <Button onClick={this.handleClickCloseBox}>Close</Button>
                </DialogActions>
                </div>
            )
        }

        if (this.state.isFailedDisplayed) {
            dialogContent = (
                <div>
                    <DialogTitle id="form-dialog-title">Add Article</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            Article Could Not Be Found. Please Try Again or Cancel.
                            </DialogContentText>

                        <TextField fullWidth placeholder="e.g. http://www.bbc.co.uk/108791" onChange={e => this.setState({ currentArticleURL: e.target.value })} />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={this.handleClickAddArticle}>Add Article</Button>
                        <Button onClick={this.handleClickCloseBox}>Cancel</Button>
                    </DialogActions>
                </div>
            )
        }

        if (this.state.isSuccessDisplayed) {
            dialogContent = (
                <div>
                <div style={{ marginLeft: '50px', marginRight: '50px'}}>
                    {
                    fetchedArticle.Articles.map((article, i) => {
                            return (<NewsItem key={i} Article={article} />);
                        })
                    }
                    
                </div>
                <DialogActions>
                    <center>
                    <Button onClick={this.handleClickCloseBox}>Close</Button>
                    </center>
                </DialogActions>
                </div>
            )
        }


        return (

            <div>
                <Dialog open={this.props.addArticlePopupIsOpen}>
                    {dialogContent}
                </Dialog>
            </div>

            
        )
    }
}

export default AddArticlePopup
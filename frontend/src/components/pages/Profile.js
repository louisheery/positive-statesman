// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button'
import Autocomplete from '@material-ui/lab/Autocomplete';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Toolbar from '@material-ui/core/Toolbar';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Switch from '@material-ui/core/Switch';
import DeleteIcon from '@material-ui/icons/Delete';
import AddIcon from '@material-ui/icons/Add';
import FilterListIcon from '@material-ui/icons/FilterList';

// REDUX LIBRARIES
import reducer from '../store/reducers/reducer';
import { connect, Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import store from "../store/store";
import { userData, avaliableData } from '../../store/actions/actions';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Profile.js';
import { Link } from '@material-ui/core';

class Profile extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            //userCategories: [[0, 'Business'], [1, 'Politics']],
            //userPublishers: [[0, 'BBC'], [1, 'NYT'], [10, 'Bloomberg']],
            //allCategories: [[0, 'Business'], [1, 'Politics'], [4, 'Art'], [7, 'Sport']],
            //allPublishers: [[0, 'BBC'], [1, 'NYT'], [4, 'Guardian'], [7, 'FT'], [10, 'Bloomberg']],
            dialogOpen: false,
            dialogContent: 'category',
        }
    }

    static propTypes = {
        userData: PropTypes.func.isRequired,
        avaliableData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
        store.dispatch(avaliableData());
    }

    onRequestAdd(type) {
        // FETCH LIST OF PUBLISHERS OR CATEGORIES
        // onSubmitGet(type);

        // DISPLAY POPUP

        // id = [what user selects]

        // THEN CALL onSubmitAdd(type, id) of which publisher/category to add
        // this.props.userData('POST', type, id, null);

        // SHOULD THEN APPEAR IN TABLES
    }

    onSubmitGet(type) {
        // this.props.userData('GET', type, null);
    }

    onSubmitAdd(type, id) {
        // this.props.userData('POST', type, id);
        userData = (requestType, dataType, dataId = null)
    }

    onSubmitDelete(type, id) {
        // this.props.userData('DELETE', type, id);
    }

    handleClose() {
        this.setState( { dialogOpen: false })
    }



    render() {

        //const { username, password } = this.state;

        const { classes } = this.props;

        if (this.props.isLoggedIn == false) {
            return <Redirect to="/" />;
        }

        var popupCategoriesTable = (
            <div>
                <Typography className={classes.title} variant="subtitle1" align="center" component="div">
                    Select a Category
                    </Typography>

                <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Category</TableCell>
                                <TableCell align="right" padding="checkbox"></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {this.state.allCategories.map((row) => (
                                <TableRow key={Math.random()}>
                                    <TableCell align="left">{row[1]}</TableCell>
                                    <TableCell align="right" padding="checkbox">
                                        <IconButton onClick={this.onSubmitAdd('category', row[0])} aria-label="delete">
                                            <AddIcon />
                                        </IconButton>
                                    </TableCell>

                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        )

        var popupPublishersTable = (
            <div>
                <Typography className={classes.title} variant="subtitle1" align="center" component="div">
                    Select a Publisher
                    </Typography>

                <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>Publisher</TableCell>
                                <TableCell align="right" padding="checkbox"></TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {this.state.allPublishers.map((row) => (
                                <TableRow key={Math.random()}>
                                    <TableCell align="left">{row[1]}</TableCell>
                                    <TableCell align="right" padding="checkbox">
                                        <IconButton onClick={this.onSubmitAdd('publisher', row[0])} aria-label="delete">
                                            <AddIcon />
                                        </IconButton>
                                    </TableCell>

                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </div>
        )



        return (
            <div>

                <Dialog open={this.state.dialogOpen} onClose={handleClose} aria-labelledby="form-dialog-title">
                    <DialogTitle id="form-dialog-title">Subscribe</DialogTitle>
                    <DialogContent>
                        <DialogContentText>
                            To subscribe to this website, please enter your email address here. We will send updates
                            occasionally.
          </DialogContentText>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            label="Email Address"
                            type="email"
                            fullWidth
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose} color="primary">
                            Cancel
          </Button>
                        <Button onClick={handleClose} color="primary">
                            Subscribe
          </Button>
                    </DialogActions>
                </Dialog>

                <Container className={classes.container} maxWidth="lg" align="center" >


                    <Typography className={classes.title} variant="h5" align="center" component="div">
                        Profile
                    </Typography>

                    <div>
                        <Typography className={classes.title} variant="subtitle1" align="center" component="div">
                            Categories
                    </Typography>


                        <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                            <Table aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Category</TableCell>
                                        <TableCell align="right" padding="checkbox">
                                            <Button onClick={this.onRequestAdd('category')} aria-label="add">
                                                Add <AddIcon />
                                            </Button>
                                        </TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.userPublishers.map((row) => (
                                        <TableRow key={Math.random()}>
                                            <TableCell align="left">{row[1]}</TableCell>
                                            <TableCell align="right" padding="checkbox">
                                                <IconButton onClick={this.onSubmitDelete('category', row[0])} aria-label="delete">
                                                    <DeleteIcon />
                                                </IconButton>
                                            </TableCell>

                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </TableContainer>

                    </div>





                    <div>
                        <Typography className={classes.title} variant="subtitle1" align="center" component="div">
                            Publishers
                    </Typography>


                        <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                            <Table aria-label="simple table" >
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Publisher</TableCell>
                                        <TableCell align="right" padding="checkbox">
                                            <Button onClick={this.onRequestAdd('category')} aria-label="add">
                                                Add <AddIcon />
                                            </Button>
                                        </TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.publishers.map((row) => (
                                        <TableRow key={Math.random()}>
                                            <TableCell align="left">{row[1]}</TableCell>
                                            <TableCell align="right" padding="checkbox">
                                                <IconButton onClick={this.onSubmitDelete('category', row[0])} aria-label="delete">
                                                    <DeleteIcon />
                                                </IconButton>
                                            </TableCell>

                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </div>



                </Container>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        isLoggedIn: state.reducer.isLoggedIn
    };
};

export default connect(mapStateToProps, { userData, avaliableData })(withStyles(styles)(Profile))

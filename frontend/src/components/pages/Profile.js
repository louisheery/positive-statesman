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
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Popover from '@material-ui/core/Popover';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';


// REDUX LIBRARIES
import reducer from '../../store/reducers/reducer';
import { connect, Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import store from "../../store/store";
import { userData, avaliableData } from '../../store/actions/actions';
import AutocompleteCustom from './profile/AutocompleteCustom';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Profile.js';
import { Link } from '@material-ui/core';

class Profile extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            AuserCategories: [[0, 'Business'], [1, 'Politics']],
            AuserPublishers: [[0, 'BBC'], [1, 'NYT'], [10, 'Bloomberg']],
            AallCategories: [[0, 'Business'], [1, 'Politics'], [4, 'Art'], [7, 'Sport']],
            AallPublishers: [[0, 'BBC'], [1, 'NYT'], [4, 'Guardian'], [7, 'FT'], [10, 'Bloomberg']],
            openMenuCategory: false,
            openMenuPublisher: false,
            anchorElCategory: undefined,
            anchorElPublisher: undefined,
            
        }
    }

    static propTypes = {
        userData: PropTypes.func.isRequired,
        avaliableData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
        //store.dispatch(avaliableData());
    }

    onSubmitAdd(type, id) {
        // this.props.userData('POST', type, id);
        store.dispatch(userData());

        // THIS SHOULD THEN REFRESH THE TABLE
    }

    onSubmitDelete(type, id) {
        // this.props.userData('DELETE', type, id);
        store.dispatch(userData());

        // THIS SHOULD THEN REFRESH THE TABLE
    }

    handleClickCategory = event => {
        this.setState({ openMenuCategory: true, anchorElCategory: event.currentTarget });
    };

    handleClickPublisher = event => {
        this.setState({ openMenuPublisher: true, anchorElPublisher: event.currentTarget });
    };

    handleRequestClose = () => {
        this.setState({ openMenuCategory: false, anchorElCategory: null });
    };

    handleRequestClose = () => {
        this.setState({ openMenuPublisher: false, anchorElPublisher: null });
    };



    render() {

        //const { username, password } = this.state;

        const { classes } = this.props;

        if (this.props.isLoggedIn == false) {
            return <Redirect to="/" />;
        }

        return (
            <div>

                <Container className={classes.container} maxWidth="lg" align="center" >


                    <Typography className={classes.title} variant="h5" align="center" component="div">
                        Profile
                    </Typography>

                    <div>

                        

                        <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                            <Table aria-label="simple table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Category</TableCell>
                                        <TableCell align="right" padding="checkbox">
                                            <Button onClick={this.handleClickCategory} aria-label="add">
                                                Add <AddIcon />
                                            </Button>
                                            <Menu
                                                id="simple-menu"
                                                anchorEl={this.state.anchorElCategory}
                                                open={this.state.openMenuCategory}
                                                keepMounted
                                                onClose={() => this.setState({ openMenuCategory: false })}
                                            >
                                                <TableContainer component={Paper} style={{ minWidth: 200, maxWidth: 800 }}>
                                                    <Table aria-label="simple table">
                                                        <TableBody>
                                                            {this.state.AallCategories.map((row) => (
                                                                <TableRow key={Math.random()}>
                                                                    <TableCell align="left">{row[1]}</TableCell>
                                                                    <TableCell align="right" padding="checkbox">
                                                                        <IconButton onClick={() => {this.onSubmitAdd('category', row[0]); this.setState( { openMenuCategory: false })}} aria-label="add">
                                                                            <AddIcon />
                                                                        </IconButton>
                                                                    </TableCell>

                                                                </TableRow>
                                                            ))}
                                                        </TableBody>
                                                    </Table>
                                                </TableContainer>
                                            </Menu>
                                        </TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.AuserCategories.map((row) => (
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


                        <TableContainer component={Paper} style={{ marginTop: '50px', maxWidth: 800 }}>
                            <Table aria-label="simple table" >
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Publisher</TableCell>
                                        <TableCell align="right" padding="checkbox">
                                            <Button onClick={this.handleClickPublisher} aria-label="add">
                                                Add <AddIcon />
                                            </Button>
                                            <Menu
                                                id="simple-menu"
                                                anchorEl={this.state.anchorElPublisher}
                                                open={this.state.openMenuPublisher}
                                                keepMounted
                                                onClose={() => this.setState({ openMenuPublisher: false })}
                                            >
                                                <TableContainer component={Paper} style={{ minWidth: 200, maxWidth: 800 }}>
                                                    <Table aria-label="simple table">
                                                        <TableBody>
                                                            {this.state.AallPublishers.map((row) => (
                                                                <TableRow key={Math.random()}>
                                                                    <TableCell align="left">{row[1]}</TableCell>
                                                                    <TableCell align="right" padding="checkbox">
                                                                        <IconButton onClick={() => { this.onSubmitAdd('publisher', row[0]); this.setState({ openMenuPublisher: false }) }} aria-label="add">
                                                                            <AddIcon />
                                                                        </IconButton>
                                                                    </TableCell>

                                                                </TableRow>
                                                            ))}
                                                        </TableBody>
                                                    </Table>
                                                </TableContainer>
                                            </Menu>
                                        </TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {this.state.AuserPublishers.map((row) => (
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

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

// REDUX
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { getUserData, addUserData, delUserData } from '../../store/actions/actions';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Profile.js';
import { Link } from '@material-ui/core';

class Profile extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            categories: [[0, 'Business'], [1, 'Politics']],
            publishers: [[0, 'BBC'], [1, 'NYT'], [10, 'Bloomberg']],
            allCategories: [[0, 'Business'], [1, 'Politics'], [4, 'Art'], [7, 'Sport']],
            allPublishers: [[0, 'BBC'], [1, 'NYT'], [4, 'Guardian'], [7, 'FT'], [10, 'Bloomberg']],
        }
    }

    static propTypes = {
        getUserData: PropTypes.func.isRequired,
        addUserData: PropTypes.func.isRequired,
        delUserData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
    }
    /*
        onSubmit = (e) => {
            e.preventDefault();
            console.log('login clicked');
            this.props.logIn(this.state.username, this.state.password);
        }
    
        onChange = (e) => {
            this.setState({ [e.target.name]: e.target.value })
        }
    */

    onRequestAdd(type) {
        // FETCH LIST OF PUBLISHERS OR CATEGORIES
        //this.props.getExternalData(type);

        // DISPLAY POPUP

        // THEN CALL onSubmitAdd(type, id) of which publisher/category to add

        // SHOULD THEN APPEAR IN TABLES
    }

    onSubmitAdd(type, id) {
        //this.props.addUserData(type, id);
    }

    onSubmitDelete(type, id) {
        //this.props.delUserData(type, id);
    }



    render() {

        var popupTable = (
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
                                    {this.state.categories.map((row) => (
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


                        <TableContainer component={Paper} style={{ maxWidth: 800}}>
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
        isLoggedIn: state.isLoggedIn
    };
};

export default connect(mapStateToProps, { getUserData, addUserData, delUserData })(withStyles(styles)(Profile))

// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import IconButton from '@material-ui/core/IconButton';
import DeleteIcon from '@material-ui/icons/Delete';
import AddIcon from '@material-ui/icons/Add';
import Menu from '@material-ui/core/Menu';


// REDUX LIBRARIES
import { connect } from 'react-redux';
import { Redirect } from "react-router-dom";
import PropTypes from "prop-types";
import { userEditData, userFetchData, avaliableData } from '../../store/actions/actions';

// STYLES
import { withStyles } from '@material-ui/core/styles';
import styles from '../../../src/assets/styles/components/pages/Profile.js';

class Profile extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            allCategories: [['/arts', 'Art, Culture & Entertainment', 'iab-qagIAB1'], ['/business', 'Business', 'iab-qagIAB3'], ['/politics', 'Law, Government & Politics', 'iab-qagIAB11'], ['/science', 'Science', 'iab-qagIAB15'], ['/sport', 'Sport', 'iab-qagIAB17'], ['/tech', 'Technology', 'iab-qagIAB19'], ['/travel', 'Travel', 'iab-qagIAB20'],],
            allPublishers: [['/theguardian', 'The Guardian', ''], ['/nytimes', 'New York Times', ''], ['/ft', 'Financial Times', ''], ['/bloomberg', 'Bloomberg', ''], ['/reuters', 'Reuters', ''], ['/ap', 'Associated Press', ''], ['/thetimes', 'The Times', ''], ['/washingtonpost', 'Washington Post', ''], ['/time', 'Time', ''], ['/wsj', 'Wall Street Journal', ''], ['/bbcnews', 'BBC News', ''], ['/huffingtonpost', 'Huffington Post', ''], ['/theatlantic', 'The Atlantic', ''], ['/vox', 'Vox', '']],
            openMenuCategory: false,
            openMenuPublisher: false,
            anchorElCategory: undefined,
            anchorElPublisher: undefined,

        }
    }
    /*
    [['iab-qagIAB1','Arts & Entertainment'],
    ['iab-qagIAB2','Automotive'],
    ['iab-qagIAB3','Business'],
    ['iab-qagIAB4','Careers'],
    ['iab-qagIAB5','Education'],
    ['iab-qagIAB6','Family & Parenting'],
    ['iab-qagIAB7','Health & Fitness'],
    ['iab-qagIAB8','Food & Drink'],
    ['iab-qagIAB9','Hobbies & Interests'],
    ['iab-qagIAB10','Home & Garden'],
    ['iab-qagIAB11','Law, Gov’t & Politics'],
    ['iab-qagIAB12','News'],
    ['iab-qagIAB13','Personal Finance'],
    ['iab-qagIAB14','Society'],
    ['iab-qagIAB15','Science'],
    ['iab-qagIAB16','Pets'],
    ['iab-qagIAB17','Sports'],
    ['iab-qagIAB18','Style & Fashion'],
    ['iab-qagIAB19','Technology & Computing'],
    ['iab-qagIAB20','Travel'],
    ['iab-qagIAB21','Real Estate'],
    ['iab-qagIAB22','Shopping'],
    ['iab-qagIAB23','Religion & Spirituality'],
    ['iab-qagIAB24','Uncategorized'],
    ['iab-qagIAB25','Non,Standard Content'],
    ['iab-qagIAB26','Illegal Content']]
    */

    static propTypes = {
        userEditData: PropTypes.func.isRequired,
        userFetchData: PropTypes.func.isRequired,
        avaliableData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
        //store.dispatch(avaliableData());
        this.props.userFetchData('GET', 'category');
        this.props.userFetchData('GET', 'publisher');
    }

    onSubmitAdd(type, id) {
        this.props.userEditData('POST', type, id);
        this.props.userFetchData('GET', type);
        this.handleSubmit;
    }

    onSubmitDelete(type, id) {
        this.props.userEditData('DELETE', type, id);
        this.props.userFetchData('GET', type);
    }

    handleClickCategory = event => {
        this.setState({ openMenuCategory: !this.state.openMenuCategory, anchorElCategory: event.currentTarget });
    };

    handleClickPublisher = event => {
        this.setState({ openMenuPublisher: !this.state.openMenuPublisher, anchorElPublisher: event.currentTarget })};

    handleRequestClose = () => {
        this.setState({ openMenuCategory: !this.state.openMenuCategory, anchorElCategory: null });
    };

    handleRequestClose = () => {
        this.setState({ openMenuPublisher: !this.state.openMenuPublisher, anchorElPublisher: null });
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



                        <TableContainer component={Paper} style={{ maxWidth: 800, marginBottom: '30px' }}>
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
                                                onClose={(e) => this.setState({ openMenuCategory: !this.state.openMenuCategory })}
                                            >
                                                <TableContainer component={Paper} style={{ minWidth: 200, maxWidth: 800 }}>
                                                    <Table aria-label="simple table">
                                                        <TableBody>
                                                            {this.state.allCategories.map((row) => (
                                                                <TableRow key={Math.random()}>
                                                                    <TableCell align="left">{row[1]}</TableCell>
                                                                    <TableCell align="right" padding="checkbox">
                                                                        <IconButton onClick={() => { this.onSubmitAdd('category', row[2]) }} aria-label="add">
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

                                    {(this.props.userCategories != undefined) &&
                                    this.props.userCategories.map((row) => (
                                        <TableRow key={Math.random()}>
                                            <TableCell align="left">{row[1]}</TableCell>
                                            <TableCell align="right" padding="checkbox">
                                                <IconButton onClick={() => { this.onSubmitDelete('category', row[2]); this.forceUpdate();}} aria-label="delete">
                                                    <DeleteIcon />
                                                </IconButton>
                                            </TableCell>

                                        </TableRow>
                                    ))
                                        }
                                </TableBody>
                            </Table>
                        </TableContainer>

                    </div>


                    <div>



                        <TableContainer component={Paper} style={{ maxWidth: 800 }}>
                            <Table aria-label="simple table">
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
                                                onClose={(e) => this.setState({ openMenuPublisher: !this.state.openMenuPublisher })}
                                            >
                                                <TableContainer component={Paper} style={{ minWidth: 200, maxWidth: 800 }}>
                                                    <Table aria-label="simple table">
                                                        <TableBody>
                                                            {this.state.allPublishers.map((row) => (
                                                                <TableRow key={Math.random()}>
                                                                    <TableCell align="left">{row[1]}</TableCell>
                                                                    <TableCell align="right" padding="checkbox">
                                                                        <IconButton onClick={() => { this.onSubmitAdd('publisher', row[2]) }} aria-label="add">
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

                                    {(this.props.userPublisers != undefined) &&
                                        this.props.userPublisers.map((row) => (
                                            <TableRow key={Math.random()}>
                                                <TableCell align="left">{row[0]}</TableCell>
                                                <TableCell align="right" padding="checkbox">
                                                    <IconButton onClick={() => { this.onSubmitDelete('publisher', row[1]); this.forceUpdate(); }} aria-label="delete">
                                                        <DeleteIcon />
                                                    </IconButton>
                                                </TableCell>

                                            </TableRow>
                                        ))
                                    }
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
        isLoggedIn: state.reducer.isLoggedIn,
        userCategories: state.reducer.userCategories,
        userPublisers: state.reducer.userPublishers,
    };
};

export default connect(mapStateToProps, { userEditData, userFetchData, avaliableData })(withStyles(styles)(Profile))
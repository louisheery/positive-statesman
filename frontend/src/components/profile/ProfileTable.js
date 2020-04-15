// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

// EXTERNAL REACT LIBRARIES & COMPONENTS
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
import PropTypes from "prop-types";
import { userEditData, userFetchData, avaliableData } from '../../store/actions/actions';

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../assets/styles/components/profile/ProfileTable.js'


class ProfileTable extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            allCategories: [['/arts', 'Art, Culture & Entertainment', 'iab-qagIAB1'], ['/business', 'Business', 'iab-qagIAB3'], ['/politics', 'Law, Government & Politics', 'iab-qagIAB11'], ['/science', 'Science', 'iab-qagIAB15'], ['/sport', 'Sport', 'iab-qagIAB17'], ['/tech', 'Technology', 'iab-qagIAB19'], ['/travel', 'Travel', 'iab-qagIAB20'],],
            allPublishers: [['/theguardian', 'The Guardian', ''], ['/nytimes', 'New York Times', ''], ['/ft', 'Financial Times', ''], ['/bloomberg', 'Bloomberg', ''], ['/reuters', 'Reuters', ''], ['/ap', 'Associated Press', ''], ['/thetimes', 'The Times', ''], ['/washingtonpost', 'Washington Post', ''], ['/time', 'Time', ''], ['/wsj', 'Wall Street Journal', ''], ['/bbcnews', 'BBC News', ''], ['/huffingtonpost', 'Huffington Post', ''], ['/theatlantic', 'The Atlantic', ''], ['/vox', 'Vox', '']],
            openMenu: false,
            anchorEl: undefined,

        }
    }

    static propTypes = {
        userEditData: PropTypes.func.isRequired,
        userFetchData: PropTypes.func.isRequired,
        avaliableData: PropTypes.func.isRequired,
    }

    componentDidMount() {
        ReactGA.pageview(`profilepage`);
        //store.dispatch(avaliableData());
        this.props.userFetchData('GET', this.props.tableType);
    }

    onSubmitAdd(id) {
        this.props.userEditData('POST', this.props.tableType, id);
        this.props.userFetchData('GET', this.props.tableType);
        this.props.userFetchData('GET', this.props.tableType);
    }

    onSubmitDelete(id) {
        this.props.userEditData('DELETE', this.props.tableType, id);
        this.props.userFetchData('GET', this.props.tableType);
        this.props.userFetchData('GET', this.props.tableType);
    }

    handleClick = event => {
        this.setState({ openMenu: !this.state.openMenu, anchorEl: event.currentTarget });    
    };

    handleRequestClose = () => {
        this.setState({ openMenu: !this.state.openMenu, anchorEl: null });
        
    };


    render() {
        const { classes, tableType } = this.props;

        var userData = tableType == 'category' ? this.props.userCategories : this.props.userPublishers
        var allData = tableType == 'category' ? this.state.allCategories : this.state.allPublishers

        return (
            <div>
                <TableContainer component={Paper} style={{ maxWidth: 800, marginBottom: '30px' }}>
                    <Table aria-label="simple table">
                        <TableHead>
                            <TableRow>
                                <TableCell>{this.props.tableType == 'category' ? ('Category') : ('Publisher')}</TableCell>
                                <TableCell align="right" padding="checkbox">
                                    <Button onClick={this.handleClick} aria-label="add">
                                        Add <AddIcon />
                                    </Button>
                                    <Menu
                                        id="simple-menu"
                                        anchorEl={this.state.anchorEl}
                                        open={this.state.openMenu}
                                        keepMounted
                                        onClose={(e) => this.setState({ openMenu: !this.state.openMenu })}
                                    >
                                        <TableContainer component={Paper} style={{ minWidth: 200, maxWidth: 800 }}>
                                            <Table aria-label="simple table">
                                                <TableBody>
                                                    {allData.map((row) => (
                                                        <TableRow key={Math.random()}>
                                                            <TableCell align="left">{row[1]}</TableCell>
                                                            <TableCell align="right" padding="checkbox">
                                                                <IconButton onClick={() => { this.onSubmitAdd(row[2]) }} aria-label="add">
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

                            {(userData != undefined) &&
                                userData.map((row) => (
                                    <TableRow key={Math.random()}>
                                        <TableCell align="left">{row[1]}</TableCell>
                                        <TableCell align="right" padding="checkbox">
                                            <IconButton onClick={() => { this.onSubmitDelete(row[2]); this.forceUpdate(); }} aria-label="delete">
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

export default connect(mapStateToProps, { userEditData, userFetchData, avaliableData })(withStyles(styles)(ProfileTable))


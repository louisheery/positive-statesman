// REACT LIBRARIES
import React, { Component } from 'react';
import { withRouter, Link } from 'react-router-dom'

// REDUX
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { logOut } from '../../store/actions/actions';

// MATERIAL UI
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button'
import SvgIcon from '@material-ui/core/SvgIcon'
import InputBase from '@material-ui/core/InputBase'
import Paper from '@material-ui/core/Paper'
import Hidden from '@material-ui/core/Hidden'
import Popover from '@material-ui/core/Popover';
import IconButton from '@material-ui/core/IconButton';
import AccountCircle from '@material-ui/icons/AccountCircle';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';
import AddCircleOutlineIcon from '@material-ui/icons/AddCircleOutline'
import SearchIcon from '@material-ui/icons/Search'
import ClickAwayListener from '@material-ui/core/ClickAwayListener'
import AssessmentIcon from '@material-ui/icons/Assessment'

// COMPONENTS
import CategoryBar from './CategoryBar'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../assets/styles/components/headers/HeaderBar.js';

// API
import { addArticle } from '../../apiIntegration.js'


class HeaderBar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            input: "",
            addArticle: false,
            searchArticle: false,
            open: false,
            openMenu: false,
            anchorEl: undefined,
        }
    }

    static propTypes = {
        logOut: PropTypes.func.isRequired,
        isLoggedIn: PropTypes.bool,
    }

    handleChangeInput = (event) => {
        this.setState({ input: event.target.value })
    }

    handleClickSubmit = () => {
        if (this.state.addArticle) {
            addArticle(this.state.input)
            this.setState({ open: true })
        }
        if (this.state.searchArticle) {
            this.props.history.push({ pathname: "/search/", search: "?q=" + this.state.input })
        }
        this.setState({ input: "", addArticle: false, searchArticle: false })
    }

    handleClickAdd = () => {
        this.setState({ addArticle: true })
    }

    handleClickSearch = () => {
        this.setState({ searchArticle: true })
    }

    handleKeyDown = (event) => {
        if (event.keyCode == 13) {
            this.handleClickSubmit()
        }
    }


    handleClick = event => {
        this.setState({ openMenu: true, anchorEl: event.currentTarget });
    };

    handleRequestClose = () => {
        this.setState({ openMenu: false, anchorEl: null });
    };

    handleClickAway = () => {
        this.setState({ input: "", addArticle: false, searchArticle: false })
    }

    handleClickAnalytics = () => {
        this.props.history.push({ pathname: "/analytics/" })
    }


    render() {

        const { classes } = this.props;
        return (
            <div>
                <Popover
                    id={1}
                    anchorEl={null}
                    open={this.state.open}
                    anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'center',
                    }}
                    transformOrigin={{
                        vertical: 'top',
                        horizontal: 'center',
                    }}
                    onClose={() => this.setState({ open: false })}
                >
                    <Typography style={{ padding: '10px' }}>Article Submitted!</Typography>
                </Popover>

                <AppBar position="fixed">

                    {/* MAIN HEADER BAR */}
                    <Toolbar className={classes.toolbar}>

                        {/* LOGO */}
                        <Button className={classes.logo} component={Link} to={'/'} disableElevation aria-label="logo"
                            variant="contained"
                            color="primary"
                            startIcon={<SvgIcon><path d="M21 7a.78.78 0 0 0 0-.21.64.64 0 0 0-.05-.17 1.1 1.1 0 0 0-.09-.14.75.75 0 0 0-.14-.17l-.12-.07a.69.69 0 0 0-.19-.1h-.2A.7.7 0 0 0 20 6h-5a1 1 0 0 0 0 2h2.83l-4 4.71-4.32-2.57a1 1 0 0 0-1.28.22l-5 6a1 1 0 0 0 .13 1.41A1 1 0 0 0 4 18a1 1 0 0 0 .77-.36l4.45-5.34 4.27 2.56a1 1 0 0 0 1.27-.21L19 9.7V12a1 1 0 0 0 2 0V7z" /></SvgIcon>}
                        >
                            <Hidden xsDown>
                                <Typography variant="h5">
                                    The Positive Statesman
                                </Typography>
                            </Hidden>
                        </Button>

                        {/* SEARCH AND ADD STORY SECTION */}
                        {this.state.searchArticle ?
                            <ClickAwayListener onClickAway={this.handleClickAway}>
                                <Paper className={classes.addStoryPaper} >
                                    <InputBase placeholder="Search" onChange={this.handleChangeInput} onKeyDown={this.handleKeyDown} />
                                    <IconButton className={classes.iconButton} color="secondary" onClick={this.handleClickSubmit}>
                                        <SearchIcon />
                                    </IconButton>
                                </Paper>
                            </ClickAwayListener>
                            : this.state.addArticle ?
                                <ClickAwayListener onClickAway={this.handleClickAway}>
                                    <Paper className={classes.addStoryPaper} >
                                        <InputBase placeholder="URL of Article" onChange={this.handleChangeInput} onKeyDown={this.handleKeyDown} />
                                        <IconButton className={classes.iconButton} color="secondary" onClick={this.handleClickSubmit}>
                                            <AddCircleOutlineIcon />
                                        </IconButton>
                                    </Paper>
                                </ClickAwayListener>
                                :
                                <div>
                                    <IconButton color="secondary" onClick={this.handleClickSearch}>
                                        <SearchIcon />
                                    </IconButton>
                                    <IconButton color="secondary" onClick={this.handleClickAdd}>
                                        <AddCircleOutlineIcon />
                                    </IconButton>
                                    <IconButton color="secondary" onClick={this.handleClickAnalytics}>
                                        <AssessmentIcon />
                                    </IconButton>
                                </div>
                        }

                        {this.props.isLoggedIn ? (
                            <div>
                                <IconButton
                                    aria-label="account of current user"
                                    aria-controls="menu-appbar"
                                    aria-haspopup="true"
                                    onClick={this.handleClick}
                                    color="inherit"
                                >
                                    <AccountCircle />
                                </IconButton>
                                <Menu

                                    id="menu-appbar"
                                    anchorEl={this.state.anchorEl}
                                    open={this.state.openMenu}
                                    onClose={this.handleRequestClose}

                                >
                                    <MenuItem component={Link} to={'/profile'}>Profile</MenuItem>
                                    <MenuItem onClick={this.props.logOut}>Logout</MenuItem>
                                </Menu>
                            </div>
                        ) : (
                                <Button color="inherit" component={Link} to={'/login'}>Login</Button>
                            )}

                    </Toolbar>

                    {/* CATEGORY HEADER BAR */}
                    <CategoryBar />

                </AppBar>
            </div>
        )
    }
}

const mapStateToProps = state => ({
    isLoggedIn: state.reducer.isLoggedIn
});

export default withRouter(connect(mapStateToProps, { logOut })(withStyles(styles)(HeaderBar)))

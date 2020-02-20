// This is Louis overcomplicated version of the header bar. I we can use it as
// inspiration for our new simple header barr and add the features once we
// actually need them.



// REACT LIBRARIES
import React, { Component } from 'react';
import { Link } from 'react-router-dom';

// INTERNAL REACT COMPONENTS

// EXTERNAL REACT LIBRARIES & COMPONENTS
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import SvgIcon from '@material-ui/core/SvgIcon';
import Hidden from '@material-ui/core/Hidden';
import InputBase from '@material-ui/core/InputBase';
import SearchIcon from '@material-ui/icons/Search';
import AccountCircle from '@material-ui/icons/AccountCircle';

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../assets/styles/components/headers/HeaderBar.js';


function a11yProps(index) {
    return {
        id: `scrollable-auto-tab-${index}`,
        'aria-controls': `scrollable-auto-tabpanel-${index}`,
    };
}


class HeaderBar extends Component {

    constructor(props) {
        super(props);
        this.state = {
            open: false,
            searchBarMobileOpen: false,
        };
    }


    handleOpenLoginMenu = () => {
        // Close Popup
        this.setState({ open: !this.state.open })
    }

    handleOpenSearchMenu = () => {
        this.setState({ searchBarMobileOpen: true })
    }

    handleCloseSearchMenu = () => {
        this.setState({ searchBarMobileOpen: false })
    }

    render() {

        const { classes } = this.props;

        var positiveStatesmanLogo = (
            <div>
                <Hidden only={['xs', 'sm']}>
                    <Button className={classes.psButton} component={Link} to={'/'} disableElevation
                        variant="contained"
                        color="primary"
                        startIcon={<SvgIcon>
                            <path d="M21 7a.78.78 0 0 0 0-.21.64.64 0 0 0-.05-.17 1.1 1.1 0 0 0-.09-.14.75.75 0 0 0-.14-.17l-.12-.07a.69.69 0 0 0-.19-.1h-.2A.7.7 0 0 0 20 6h-5a1 1 0 0 0 0 2h2.83l-4 4.71-4.32-2.57a1 1 0 0 0-1.28.22l-5 6a1 1 0 0 0 .13 1.41A1 1 0 0 0 4 18a1 1 0 0 0 .77-.36l4.45-5.34 4.27 2.56a1 1 0 0 0 1.27-.21L19 9.7V12a1 1 0 0 0 2 0V7z" />
                        </SvgIcon>}
                    ><Typography variant="h5">The Positive Statesman</Typography>
                    </Button>
                </Hidden>

                <Hidden only={['xs', 'md', 'lg', 'xl']}>
                    <Button className={classes.psButton} component={Link} to={'/'} disableElevation
                        variant="contained"
                        color="primary"
                    ><Typography variant="h5">The Positive Statesman</Typography>
                    </Button>
                </Hidden>


                <Hidden only={['sm', 'md', 'lg', 'xl']}>
                    <Link className={classes.psButtonSmall} href="/" to={"/"} onClick={(event) => event.preventDefault()}>
                        <p className={classes.psButtonSmallText}>
                            Positive Statesman
                                    </p>
                    </Link>

                </Hidden>
            </div>
        )

        var mobileSearchBar = (
            <Toolbar className={classes.toolbar} >

                <div className={classes.searchBarMobile}>
                    <div className={classes.searchBarIcon}>
                        <SearchIcon />
                    </div>
                    <InputBase
                        placeholder="Search"
                        classes={{
                            root: classes.searchBox,
                            input: classes.searchBoxText,
                        }}
                        inputProps={{ 'aria-label': 'search' }}
                    />
                </div>

                <Button color="inherit" onClick={this.handleCloseSearchMenu}>Close</Button>

            </Toolbar>
        )

        var desktopSearchBar = (
            <div>
                <Hidden only={['xs', 'sm']}>
                    <div className={classes.flexDiv}>
                        <center>
                            <div className={classes.searchBar}>
                                <div className={classes.searchBarIcon}>
                                    <SearchIcon />
                                </div>
                                <InputBase
                                    placeholder="Search"
                                    classes={{
                                        root: classes.searchBox,
                                        input: classes.searchBoxText,
                                    }}
                                    inputProps={{ 'aria-label': 'search' }}
                                />
                            </div>
                        </center>
                    </div>
                </Hidden>

                <Hidden only={['md', 'lg', 'xl']}>
                    <div className={classes.flexDiv}>
                    </div>
                </Hidden>
            </div>
        )

        var userAccountLoginSection = (
            <div>
                <Hidden only={['md', 'lg', 'xl']}>
                    <IconButton onClick={this.handleOpenSearchMenu} color="inherit">
                        <SearchIcon />
                    </IconButton>
                </Hidden>

                {!this.props.userIsLoggedIn && <Button component={Link} to={'/login'} color="inherit">{this.props.userIsLoggedIn ? "Log Out" : "Log In"}</Button>}
                {
                    !this.props.userIsLoggedIn &&
                    <div>
                        <IconButton onClick={this.handleOpenLoginMenu} color="inherit">
                            <AccountCircle />
                        </IconButton>
                    </div>
                }
            </div>
        )


        return (


            <AppBar>
                {/* CONDITIONAL ON WHETHER TO SHOW MOBILE SEARCH BAR */}
                {this.state.searchBarMobileOpen ?
                    (
                        { mobileSearchBar }

                    ) : (

                        <Toolbar className={classes.toolbar}>
                            <IconButton edge="start" color="inherit" aria-label="menu">
                                <MenuIcon />
                            </IconButton>

                            {positiveStatesmanLogo}

                            <div className={classes.flexDiv}></div>
                            {/* { desktopSearchBar } */}

                            <div className={classes.addButton} >
                                <Hidden only={['xs', 'sm']}>
                                    <Button className={classes.addStoryButton} display={{ xs: 'none', md: 'block' }} variant="contained" color="secondary" disableElevation onClick={this.props.handleArticlePopupOpening}>
                                        Add Story
                                    </Button>
                                </Hidden>
                            </div>
                            {/* { userAccountLoginSection }  */}
                        </Toolbar>

                    )}

                {/* Second Row of Header Bar i.e. Navigation Panels */}
                <Tabs className={classes.tabBar}
                    value={"/"} // FIX THIS -- this.props.location.pathname
                    onChange={this.handleChange}
                    indicatorColor="secondary"
                    variant="scrollable"
                    aria-label="scrollable auto tabs example"
                >

                    <Tab className={classes.headerTab} component={Link} to={'/'} value="/" label={<span color="#FFF" role="img" aria-label="home">Home</span>} {...a11yProps(0)} />

                    <Tab className={classes.headerTab} component={Link} to={'/business'} value="/business" label="Business" {...a11yProps(1)} />

                    <Tab className={classes.headerTab} component={Link} to={'/politics'} value="/politics" label="Politics" {...a11yProps(2)} />

                    <Tab className={classes.headerTab} component={Link} to={'/sport'} value="/sport" label="Sport" {...a11yProps(3)} />

                    <Tab className={classes.headerTab} component={Link} to={'/science'} value="/science" label="Science" {...a11yProps(4)} />

                    <Tab className={classes.headerTab} component={Link} to={'/health'} value="/health" label="Health" {...a11yProps(5)} />

                    <Tab className={classes.headerTab} component={Link} to={'/gaming'} value="/gaming" label="Gaming" {...a11yProps(6)} />

                    <Tab className={classes.headerTab} component={Link} to={'/culture'} value="/culture" label="Culture" {...a11yProps(7)} />

                </Tabs>
            </AppBar>
        )
    }
}

export default withStyles(styles)(HeaderBar)
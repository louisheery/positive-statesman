import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import SvgIcon from '@material-ui/core/SvgIcon';
import { Link } from 'react-router-dom';
import { withRouter } from 'react-router-dom';


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
        };
    }


    handleOpenLoginMenu = () => {
        // Close Popup
        this.setState({ open: !this.state.open })
    }

    render() {

        return (

            <AppBar>
                <Toolbar style={{ marginLeft: '65px', marginRight: '65px' }}>
                    <IconButton edge="start" color="inherit" aria-label="menu">
                        <MenuIcon />
                    </IconButton>

                    <Button component={Link} to={'/'} style={{ textTransform: 'none', marginLeft: '20px' }} disableElevation
                        variant="contained"
                        color="primary"
                        startIcon={<SvgIcon>
                            <path d="M21 7a.78.78 0 0 0 0-.21.64.64 0 0 0-.05-.17 1.1 1.1 0 0 0-.09-.14.75.75 0 0 0-.14-.17l-.12-.07a.69.69 0 0 0-.19-.1h-.2A.7.7 0 0 0 20 6h-5a1 1 0 0 0 0 2h2.83l-4 4.71-4.32-2.57a1 1 0 0 0-1.28.22l-5 6a1 1 0 0 0 .13 1.41A1 1 0 0 0 4 18a1 1 0 0 0 .77-.36l4.45-5.34 4.27 2.56a1 1 0 0 0 1.27-.21L19 9.7V12a1 1 0 0 0 2 0V7z" />
                        </SvgIcon>}
                    ><Typography variant="h5">The Positive Statesman</Typography>
                    </Button>


                    {/* ADD SEARCH BAR HERE */}

                    <div className="HeaderBarFlexGrow" />
                    <div className="HeaderBarAddButton">
                        <Button variant="contained" color="secondary" disableElevation onClick={this.props.handleArticlePopupOpening}>
                            Add Story
                        </Button>
                    </div>
                    {!this.props.userIsLoggedIn && <Button component={Link} to={'/login'} color="inherit">{this.props.userIsLoggedIn ? "Log Out" : "Log In"}</Button>}
                    {!this.props.userIsLoggedIn &&
                        <div>
                            <IconButton onClick={this.handleOpenLoginMenu} color="inherit">
                                <AccountCircle />
                            </IconButton>
                        </div>
                    }
                </Toolbar>

                <Tabs style={{ background: '#007ea7', paddingLeft: "5%", paddingRight: "5%" }}
                    value={this.props.location.pathname}
                    onChange={this.handleChange}
                    indicatorColor="secondary"
                    variant="scrollable"
                    aria-label="scrollable auto tabs example"
                >

                    <Tab component={Link} to={'/'} value="/" style={{ flexGrow: "1" }} label={<span color="#FFF" role="img" aria-label="home">Home</span>} {...a11yProps(0)} />


                    <Tab component={Link} to={'/business'} value="/business" style={{ flexGrow: "1" }} label="Business" {...a11yProps(1)} />

                    <Tab component={Link} to={'/politics'} value="/politics" style={{ flexGrow: "1" }} label="Politics" {...a11yProps(2)} />

                    <Tab component={Link} to={'/sport'} value="/sport" style={{ flexGrow: "1" }} label="Sport" {...a11yProps(3)} />

                    <Tab component={Link} to={'/science'} value="/science" style={{ flexGrow: "1" }} label="Science" {...a11yProps(4)} />

                    <Tab component={Link} to={'/health'} value="/health" style={{ flexGrow: "1" }} label="Health" {...a11yProps(5)} />

                    <Tab component={Link} to={'/gaming'} value="/gaming" style={{ flexGrow: "1" }} label="Gaming" {...a11yProps(6)} />

                    <Tab component={Link} to={'/culture'} value="/culture" style={{ flexGrow: "1" }} label="Culture" {...a11yProps(7)} />

                </Tabs>


            </AppBar>
        )
    }
}

export default withRouter(HeaderBar)

import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

class HeaderBar extends Component {

    render() {
        return (

            <AppBar position="fixed">
                <Toolbar>
                    <IconButton edge="start" color="inherit" aria-label="menu">
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" style={{ marginLeft: "50px" }}>
                        The Positive Statesman
                    </Typography>
                    <div className="HeaderBarFlexGrow" />
                    <div className="HeaderBarAddButton">
                        <Button variant="contained" color="secondary" disableElevation onClick={this.props.handleArticlePopupOpening}>
                            Add Story
                        </Button>
                    </div>
                </Toolbar>
            </AppBar>
        )
    }
}

export default HeaderBar
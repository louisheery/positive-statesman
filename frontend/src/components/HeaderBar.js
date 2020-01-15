import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

class HeaderBar extends Component {
    render() {
        return (

            <AppBar position="fixed">
                <Toolbar>
                    <Typography variant="h6" style={{ marginLeft: "50px" }}>
                        The Positive Statesman
                    </Typography>
                </Toolbar>
            </AppBar>
        )
    }
}

export default HeaderBar
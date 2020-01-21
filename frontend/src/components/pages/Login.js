import React from 'react';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import GoogleButton from 'react-google-button';
import HeaderBar from '../headers/HeaderBar';


class Login extends React.Component {

    render() {
        return (
            <div>
                <Container maxWidth="lg" align="center" style={{ marginTop: '150px' }}>
                    <Typography variant="h5" align="center" component="div" style={{ backgroundColor: '#FFF', height: '100vh' }}>
                        Login to The Positive Statesman
        
                <div align="center" style={{ marginTop: '50px' }}>
                            <GoogleButton onClick={() => alert('API magic happens now')} />
                        </div>
                    </Typography>
                </Container>
            </div>
        )
    }
}

export default Login;

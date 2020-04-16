// REACT LIBRARIES
import React from 'react';
import ReactGA from "react-ga";

class Logout extends React.Component {

    componentDidMount() {
        ReactGA.pageview(`logoutpage`);
    }

    render() {

        return (
            <div>
                <p>Logout Page</p>
            </div>
        )
    }
}

export default Logout
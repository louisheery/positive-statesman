import React, { Component } from 'react';
import Ticker from 'react-ticker'

class NewsTickerBar extends Component {

    render() {
        return (
            <div className="NewsTickerGrid">
            <Ticker>
                {({ index }) => (
                        <div style={{ backgroundColor: '#e3f3f4'}}>
                            <h3 style={{ backgroundColor: '#e3f3f4', paddingTop: '10px', paddingBottom: '10px'}}>Business  60%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Politics  30%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sport  70%↑ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Culture  80%↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h3>
                    </div>
                )}
            </Ticker>
            </div>
        )
    }
}

export default NewsTickerBar
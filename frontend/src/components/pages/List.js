// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'
import ReactGA from 'react-ga'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import Link from '@material-ui/core/Link';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';

import { publisherDictionary } from '../Settings';

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/List.js'

console.log(publisherDictionary)

class ListPage extends Component {

    componentDidMount() {
        ReactGA.pageview(`publisherspage`);
    }



    render() {
        const { classes } = this.props;
        return (
            <div className={classes.container}>
                <Typography variant="h4">
                    Publishers
                </Typography>
                <Grid container justify="center">
                    {
                        Object.keys(publisherDictionary).map(function (key, i) {
                            return (
                                <div key={i}>
                    <Link href={`/publishers/${publisherDictionary[key][0]}`}>
                    <Card className={classes.cardRoot}>
                        <CardActionArea>
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="h2">
                                    {publisherDictionary[key][1]}
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>

                                    </Link>
                                </div>
                            )
                        })}
      
                </Grid>

            </div>
        )
    }
}

export default withRouter(withStyles(styles)(ListPage))
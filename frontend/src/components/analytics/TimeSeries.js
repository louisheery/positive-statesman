// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import Card from '@material-ui/core/Card'
import CardHeader from '@material-ui/core/CardHeader'

// CHARTS
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Label } from "recharts"

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/analytics/TimeSeries.js'

// API
import { getTimeSeriesData } from "../../apiIntegration"

/*
var data = [
    {
        "date": '2020-03-20', // Date of the average. Needs to be called name!
        "business": 0.3, // Average for business category
        "economics": 0.5, // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-21', // Date of the average. Needs to be called name!
        "business": 0.1, // Average for business category
        "economics": 0.7 // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-22', // Date of the average. Needs to be called name!
        "business": 0.4, // Average for business category
        "economics": 0.4 // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-23', // Date of the average. Needs to be called name!
        "business": 0.3, // Average for business category
        "economics": 0.5 // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-24', // Date of the average. Needs to be called name!
        "business": 0.7, // Average for business category
        "economics": 0.7 // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-25', // Date of the average. Needs to be called name!
        "business": 0.8, // Average for business category
        "economics": 0.2 // Average for politics
        // Averages for all remaining categories
    },
    {
        "date": '2020-03-26', // Date of the average. Needs to be called name!
        "business": 0.5, // Average for business category
        "economics": 0.1 // Average for politics
        // Averages for all remaining categories
    },
]*/
const colors = ["#58C1B2", "#6B62CC", "#BF4466", "#F8CE4C", "#5096DD", "#CC6BD5", "#949A9B", "#79C867", "#EE8E53", "#CB4B45"]

class Analytics extends Component {

    constructor(props) {
        super(props)
        var today = this.getDate()
        this.state = {
            data: [{}],
            begin: '2020-03-24',
            end: '2020-04-02'
        }
    }

    componentDidMount = () => {
        this.getData()
    }

    getDate = () => {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0')
        var mm = String(today.getMonth() + 1).padStart(2, '0')
        var yyyy = today.getFullYear()

        return yyyy + "-" + mm + '-' + dd
    }

    getData = () => {
        getTimeSeriesData(this.props.param, this.state.begin, this.state.end).then((data) => {
            for (let i = 0; i < data.length; i++) {
                for (let key in data[i]) {
                    if (key !== "date") {
                        data[i][key] = (data[i][key] * 100).toFixed(0)
                    }
                }
            }

            this.setState({ data: data !== null ? data : [{}] })
        })
    }


    render() {
        const { classes } = this.props;
        return (
            <Grid className={classes.cardOutside} container item xs={12} lg={8} justify="center">
                <Card className={classes.card} >
                    <CardHeader className={classes.cardHeader} title={this.props.param} align="center" titleTypographyProps={{ variant: "subtitle1" }} />
                    <ResponsiveContainer width="100%" height={300}>
                        <LineChart data={this.state.data} margin={{ top: 10, right: 10, left: 10, bottom: 20 }}>
                            <CartesianGrid strokeDasharray="3 3" />
                            <XAxis dataKey="date" style={{ fontSize: 12 }}>
                                <Label value="Time" offset={-10} position="insideBottom" className={classes.axisLabel} />
                            </XAxis>
                            <YAxis type="number" domain={[0, 100]} style={{ fontSize: 12 }}>
                                <Label value="Avg. Sentiment Score in %" angle={-90} position="insideLeft" className={classes.axisLabel} />
                            </YAxis>
                            <Tooltip />
                            <Legend verticalAlign="top" />
                            {this.state.data.length !== 0 ? Object.keys(this.state.data[0]).map((dataKey, i) => {
                                return dataKey !== "date" ? <Line key={i} type="monotone" dataKey={dataKey} stroke={colors[i]} />
                                    : null
                            })
                                : null
                            }
                        </LineChart>
                    </ResponsiveContainer>
                </Card>
            </Grid >
        )
    }
}

export default withRouter(withStyles(styles)(Analytics))
// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'

// MATERIAL UI
import Grid from '@material-ui/core/Grid'
import Card from '@material-ui/core/Card'
import CardHeader from '@material-ui/core/CardHeader'
import Typography from '@material-ui/core/Typography'

// CHARTS
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line, Label } from "recharts"

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/analytics/TimeSeries.js'

// API
import { getTimeSeriesData } from "../../apiIntegration"

const colors = ["#58C1B2", "#6B62CC", "#BF4466", "#F8CE4C", "#5096DD", "#CC6BD5", "#949A9B", "#79C867", "#EE8E53", "#CB4B45"]

class TimeSeries extends Component {

    constructor(props) {
        super(props)
        this.state = {
            data: [{}],
            begin: this.getDate(-6),
            end: this.getDate(0)
        }
    }

    componentDidMount = () => {
        this.getData()
    }

    getDate = (differenceFromToday = 0) => {
        var date = new Date();
        date.setDate(date.getDate() + differenceFromToday)
        var dd = String(date.getDate()).padStart(2, '0')
        var mm = String(date.getMonth() + 1).padStart(2, '0')
        var yyyy = date.getFullYear()
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
                    <CardHeader className={classes.cardHeader} title={this.props.title} align="center" titleTypographyProps={{ variant: "subtitle1" }} />
                    <Grid container justify="center">
                        <Grid className={classes.typo} item xs={12}>
                            <Typography variant="caption">
                                {this.props.description}
                            </Typography>
                        </Grid>
                    </Grid>
                    <ResponsiveContainer width="99%" height={300}>
                        <LineChart data={this.state.data} margin={{ top: 20, right: 40, left: 10, bottom: 20 }}>
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
                                return dataKey !== "date" ? <Line key={i} type="monotone" dataKey={dataKey} stroke={colors[i]} /> : null
                            }) : null
                            }
                        </LineChart>
                    </ResponsiveContainer>
                </Card>
            </Grid >
        )
    }
}

export default withRouter(withStyles(styles)(TimeSeries))
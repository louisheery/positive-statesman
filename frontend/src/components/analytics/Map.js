// REACT LIBRARIES
import React, { Component } from 'react'

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/analytics/Map.js'
import Grid from '@material-ui/core/Grid'
import Card from '@material-ui/core/Card'
import CardHeader from '@material-ui/core/CardHeader'
import Typography from '@material-ui/core/Typography'

// MAP
import { ComposableMap, Geographies, Geography } from "react-simple-maps";

// API
import { getTimeSeriesData } from "../../apiIntegration"

// Retrieved from https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json
import geoUrl from "./Map.json"

const DEFAULT_COLOR = "grey"

class Map extends Component {
    constructor(props) {
        super(props)
        this.state = {
            data: [{}],
            date: this.getDate(0)
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
        getTimeSeriesData("countries", this.state.date, this.getDate(0)).then((data) => {
            for (let i = 0; i < data.length; i++) {
                for (let key in data[i]) {
                    if (key !== "date") {
                        data[i][key] = (data[i][key] * 100).toFixed(0)
                    }
                }
            }
            this.setState({ data: data !== null ? data : [{}] })
            console.log(this.state.data)
        })
    }

    colorScale = (percentage) => {
        let red, green, blue = 0
        if (percentage < 50) {
            red = 255
            green = Math.round(5.1 * percentage)
        }
        else {
            green = 255
            red = Math.round(510 - 5.1 * percentage);
        }
        var hex = red * 0x10000 + green * 0x100 + blue * 0x1;
        return '#' + ('000000' + hex.toString(16)).slice(-6);
    }

    render() {
        const { classes } = this.props;
        return (
            <Grid className={classes.cardOutside} container item xs={12} lg={8} justify="center">
                <Card className={classes.card} >
                    <CardHeader className={classes.cardHeader} title={"Map"} align="center" titleTypographyProps={{ variant: "subtitle1" }} />
                    <Grid container justify="center">
                        <Grid className={classes.typo} item xs={12}>
                            <Typography variant="caption">
                                This map shows the average news coverage positivity for each country on {String(this.state.date)}.
                            </Typography>
                        </Grid>
                    </Grid>
                    <ComposableMap
                        projectionConfig={{ center: [18, 7] }}
                        height={420}
                    >
                        <Geographies geography={geoUrl} >
                            {({ geographies }) =>
                                geographies.map(geo => {
                                    let value = this.state.data[0][geo.properties.NAME];
                                    return (
                                        <Geography key={geo.rsmKey} geography={geo} fill={value && value != 0 ? this.colorScale(value) : DEFAULT_COLOR} />
                                    )
                                })
                            }
                        </Geographies>
                    </ComposableMap>
                </Card>
            </Grid>
        )
    }
}

export default withStyles(styles)(Map)

/*
[
  "Afghanistan",
  "Angola",
  "Albania",
  "United Arab Emirates",
  "Argentina",
  "Armenia",
  "Antarctica",
  "Fr. S. Antarctic Lands",
  "Australia",
  "Austria",
  "Azerbaijan",
  "Burundi",
  "Belgium",
  "Benin",
  "Burkina Faso",
  "Bangladesh",
  "Bulgaria",
  "Bahamas",
  "Bosnia and Herz.",
  "Belarus",
  "Belize",
  "Bolivia",
  "Brazil",
  "Brunei",
  "Bhutan",
  "Botswana",
  "Central African Rep.",
  "Canada",
  "Switzerland",
  "Chile",
  "China",
  "Côte d'Ivoire",
  "Cameroon",
  "Dem. Rep. Congo",
  "Congo",
  "Colombia",
  "Costa Rica",
  "Cuba",
  "N. Cyprus",
  "Cyprus",
  "Czechia",
  "Germany",
  "Djibouti",
  "Denmark",
  "Dominican Rep.",
  "Algeria",
  "Ecuador",
  "Egypt",
  "Eritrea",
  "Spain",
  "Estonia",
  "Ethiopia",
  "Finland",
  "Fiji",
  "Falkland Is.",
  "France",
  "Gabon",
  "United Kingdom",
  "Georgia",
  "Ghana",
  "Guinea",
  "Gambia",
  "Guinea-Bissau",
  "Eq. Guinea",
  "Greece",
  "Greenland",
  "Guatemala",
  "Guyana",
  "Honduras",
  "Croatia",
  "Haiti",
  "Hungary",
  "Indonesia",
  "India",
  "Ireland",
  "Iran",
  "Iraq",
  "Iceland",
  "Israel",
  "Italy",
  "Jamaica",
  "Jordan",
  "Japan",
  "Kazakhstan",
  "Kenya",
  "Kyrgyzstan",
  "Cambodia",
  "South Korea",
  "Kosovo",
  "Kuwait",
  "Laos",
  "Lebanon",
  "Liberia",
  "Libya",
  "Sri Lanka",
  "Lesotho",
  "Lithuania",
  "Luxembourg",
  "Latvia",
  "Morocco",
  "Moldova",
  "Madagascar",
  "Mexico",
  "Macedonia",
  "Mali",
  "Myanmar",
  "Montenegro",
  "Mongolia",
  "Mozambique",
  "Mauritania",
  "Malawi",
  "Malaysia",
  "Namibia",
  "New Caledonia",
  "Niger",
  "Nigeria",
  "Nicaragua",
  "Netherlands",
  "Norway",
  "Nepal",
  "New Zealand",
  "Oman",
  "Pakistan",
  "Panama",
  "Peru",
  "Philippines",
  "Papua New Guinea",
  "Poland",
  "Puerto Rico",
  "North Korea",
  "Portugal",
  "Paraguay",
  "Palestine",
  "Qatar",
  "Romania",
  "Russia",
  "Rwanda",
  "W. Sahara",
  "Saudi Arabia",
  "Sudan",
  "S. Sudan",
  "Senegal",
  "Solomon Is.",
  "Sierra Leone",
  "El Salvador",
  "Somaliland",
  "Somalia",
  "Serbia",
  "Suriname",
  "Slovakia",
  "Slovenia",
  "Sweden",
  "Swaziland",
  "Syria",
  "Chad",
  "Togo",
  "Thailand",
  "Tajikistan",
  "Turkmenistan",
  "Timor-Leste",
  "Trinidad and Tobago",
  "Tunisia",
  "Turkey",
  "Taiwan",
  "Tanzania",
  "Uganda",
  "Ukraine",
  "Uruguay",
  "United States of America",
  "Uzbekistan",
  "Venezuela",
  "Vietnam",
  "Vanuatu",
  "Yemen",
  "South Africa",
  "Zambia",
  "Zimbabwe"
]
*/
// REACT LIBRARIES
import React, { Component } from 'react'
import { withRouter } from 'react-router-dom'
import ReactGA from 'react-ga'

// MATERIAL UI
import Typography from '@material-ui/core/Typography'
import Grid from '@material-ui/core/Grid'
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Divider from '@material-ui/core/Divider';
import InboxIcon from '@material-ui/icons/Inbox';
import DraftsIcon from '@material-ui/icons/Drafts';

// STYLES
import { withStyles } from '@material-ui/core/styles'
import styles from '../../../src/assets/styles/components/pages/List.js'

const publisherDictionary = {
    GUARDIAN: ['guardian', 'The Guardian', 'The%20Guardian'],
    NYTIMES: ['nytimes', 'NYTimes', 'New%20York%20Times'],
    FT: ['ft', 'FT', 'Financial%20Times'],
    BLOOMBERG: ['bloomberg', 'Bloomberg', 'Bloomberg'],
    REUTERS: ['reuters', 'Reuters', 'Reuters'],
    AP: ['ap', 'AP', 'Associated%20Press'],
    THETIMES: ['thetimes', 'The Times', 'The%20Times'],
    WASHINGTONPOST: ['washingtonpost', 'Washington Post', 'Washington%20Post'],
    AFP: ['afp', 'AFP', 'AFP'],
    ABCNEWS: ['abcnews', 'ABC News', 'ABC%20News'],
    TIME: ['time', 'Time', 'Time'],
    WSJ: ['wsj', 'Wall Street Journal', 'Wall%20Street%20Journal'],
    ECONOMIST: ['economist', 'Economist', 'The%20Economist'],
    POLITICO: ['politico', 'Politico', 'Politico'],
    BBC: ['bbc', 'BBC News', 'BBC'],
    PBS: ['pbs', 'PBS', 'PBS'],
    THEHILL: ['the hill', 'The Hill', 'The%20Hill'],
    USATODAY: ['usatoday', 'USA Today', 'USA%20Today'],
    NPR: ['npr', 'NPR', 'NPR'],
    CBSNEWS: ['cbsnews', 'CBS News', 'CBS%20News'],
    AXIOS: ['axios', 'Axios', 'Axios'],
    HUFFINGTONPOST: ['huffingtonpost', 'Huffington Post', 'Huffington%20Post'],
    NEWYORKER: ['newyorker', 'The New Yorker', 'The%20New%20Yorker'],
    NATIONALREVIEW: ['nationalreview', 'National Review', 'National%20Review'],
    SLATE: ['slate', 'Slate', 'Slate'],
    THEATLANTIC: ['theatlantic', 'The Atlantic', 'The%20Atlantic'],
    THEWEEK: ['theweek', 'The Week', 'The%20Week'],
    VANITYFAIR: ['vanityfair', 'Vanity Fair', 'Vanity%20Fair'],
    MSNBC: ['msnbc', 'MSNBC', 'MSNBC'],
    CNN: ['cnn', 'CNN', 'CNN'],
    AMERICANCONSERVATIVE: ['americanconservative', 'The American Conservative', 'The%20American%20Conservative'],
    VOX: ['vox', 'Vox', 'Vox'],
    MIC: ['mic', 'Mic', 'Mic'],
    INDEPENDENT: ['independent', 'Independent', 'Independent'],
    THESUN: ['thesun', 'The Sun', 'The%20Sun'],
    THEMETRO: ['themetro', 'The Metro', 'The%20Metro'],
    DAILYMAIL: ['dailymail', 'Daily Mail', 'Daily%20Mail'],
    TELEGRAPH: ['telegraph', 'The Telegraph', 'The%20Telegraph'],
    LATIMES: ['latimes', 'LA Times', 'Los%20Angeles%20Times'],
    CNET: ['cnet', 'CNET', 'CNET'],
    ENGADGET: ['engadget', 'Engadget', 'Engadget'],
    THEVERGE: ['theverge', 'The Verge', 'The%20Verge'],
    VICE: ['vice', 'Vice', 'Vice'],
    HOLLYWOODREPORTER: ['hollywoodreporter', 'The Hollywood Reporter', 'The%20Hollywood%20Reporter'],
    NEWSWEEK: ['newsweek', 'Newsweek', 'Newsweek'],
    FORBES: ['forbes', 'Forbes', 'Forbes'],
    SCIENCEMAG: ['sciencemag', 'Science Magazine', 'Science%20Magazine'],
    RTE: ['rte', 'RTE', 'RTE'],
    NATGEO: ['natgeo', 'National Geographic', 'National%20Geographics'],
    WANDERLUST: ['wanderlust', 'Wanderlust', 'Wanderlust'],
    SKYSPORTSNEWS: ['skysportsnews', 'Sky Sports News', 'Sky%20Sports%20News'],
    ESPN: ['espn', 'ESPN', 'ESPN'],
    THEATHLETIC: ['theathletic', 'The Athletic', 'The%20Athletic'],
    PHYSORG: ['phys.org', 'Phys.org', 'Phys.org'],
    PHYSICSWORLD: ['physicsworld', 'physicsworld.com', 'Physics%20World'],
    SKYNEWS: ['skynews', 'Sky News', 'Sky%20News'],
    TECHRADAR: ['techradar', 'TechRadar', 'TechRadar'],
    ENTERTAINMENTDAILY: ['entertainmentdaily', 'Entertainment Daily', 'Entertainment%20Daily'],
    DIGITALSPY: ['digitalspy', 'Digital Spy', 'Digital%20Spy'],
    INEWS: ['inews', 'i News', 'i%20News'],
    IGN: ['ign', 'IGN', 'IGN'],
    FRANCE24: ['france24', 'France24', 'France24'],
    DW: ['dw', 'Deutsche Welle', 'Deutsche%20Welle'],
    EURONEWS: ['euronews', 'Euro News', 'Euro%20News'],
    THELOCALITALY: ['thelocalitaly', 'The Local Italy', 'The%20Local'],
    ELPAIS: ['elpais', 'El Pais', 'El%20Pais'],
    CBC: ['cbc', 'CBC', 'CBC'],
    GLOBALNEWS: ['globalnews', 'Global News', 'Global%20News'],
    NATIONALPOST: ['nationalpost', 'National Post', 'National%20Post'],
    MSN: ['msn', 'MSN', 'MSN'],
    NBCNEWS: ['nbcnews', 'NBC News', 'NBC%20News'],
    ABCNEWSAU: ['abcnews', 'ABC News', 'ABC%20News%20au'],
    SCMP: ['scmp', 'SCMP', 'SCMP'],
    SEATTLETIMES: ['seattletimes', 'Seattle Times', 'Seattle%20Times'],
    INDEPENDENTIE: ['independentie', 'Independent IE', 'Independent%20ie'],
    EVENINGSTANDARD: ['eveningstandard', 'Evening Standard', 'Evening%20Standard'],
    WIRED: ['wired', 'Wired', 'Wired'],
    FORTUNE: ['fortune', 'Fortune', 'Fortune'],
    TECHCRUNCH: ['techcrunch', 'Techcrunch', 'Techcrunch'],
    USNEWS: ['usnews', 'US News', 'US%20News'],
}

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
                    <div className={classes.root}>
                        <List component="nav" aria-label="main mailbox folders">
                            {
                                Object.keys(publisherDictionary).map(function (key, i) {
                                    return (
                                        <div key={i}>
                                            <ListItem button>
                                                <ListItemIcon>
                                                    <InboxIcon />
                                                </ListItemIcon>
                                                <ListItemText primary={publisherDictionary[key][1]} />
                                            </ListItem>
                                        </div>
                                    )
                                })}

                            


                        </List>
                    </div>
                    
                </Grid>

            </div>
        )
    }
}

export default withRouter(withStyles(styles)(ListPage))
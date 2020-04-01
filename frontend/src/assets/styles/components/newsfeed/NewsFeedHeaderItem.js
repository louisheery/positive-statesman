const styles = {

    paper: {
        padding: '10px',
        margin: '10px',
        textAlign: 'center',
        backgroundColor: 'grey',
        height: '160px',
    },

    paperSmall: {
        padding: '10px',
        textAlign: 'center',
        backgroundColor: 'white',
        height: '160px',
    },

    title: {
        color: 'white',
        fontSize: '1.8vh',
        textAlign: 'left',
        fontWeight: 'bold',
        lineHeight: '1em',
        textOverflow: 'ellipsis',
        overflow: 'hidden',
        whiteSpace: 'normal',
        minHeight: '3em',
        maxHeight: '3em',
        paddingTop: '10px',
        paddingBottom: '5px',
        "&:hover": {
            textDecoration: "underline"
        },
    },

    subtitleLeft: {
        color: 'white', fontSize: '1.6vh', float: 'left', display: 'inline-block', lineHeight: '1em', maxHeight: '1em',
    },

    subtitleRight: {
        color: 'white', fontSize: '1.6vh', float: 'right', display: 'inline-block', lineHeight: '1em', maxHeight: '1em',
    },

    alignLeft: {
        float: 'left', display: 'inline-block', width: '100%'
    },

    positivity: {
        fontFamily: 'helvetica', borderRadius: '5px', border: '1px solid green', backgroundColor: 'white', marginLeft: '10%', marginRight: '10%', margin: '5px'
    }



}

export default styles;
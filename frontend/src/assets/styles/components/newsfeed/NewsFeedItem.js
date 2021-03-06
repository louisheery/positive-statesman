const styles = {

    paper: {
        padding: '10px',
        margin: '10px',
        paddingBottom: '20px',
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
        fontSize: '10pt + 1.8vw',
        textAlign: 'left',
        fontWeight: 'bold',
        lineHeight: '14pt',
        textOverflow: 'ellipsis',
        overflow: 'hidden',
        whiteSpace: 'normal',
        minHeight: '38pt',
        maxHeight: '38pt',
        paddingTop: '10px',
        paddingBottom: '5px',
        "&:hover": {
            textDecoration: "underline"
        },
    },

    subtitleLeft: {
        color: 'white', fontSize: '1.6vh', float: 'left', display: 'inline-block', lineHeight: '1em', maxHeight: '1em',
        "&:hover": {
            textDecoration: "underline"
        },
    },

    subtitleRight: {
        color: 'white', fontSize: '1.6vh', float: 'right', display: 'inline-block', lineHeight: '1em', maxHeight: '1em',
    },

    alignLeft: {
        float: 'left', display: 'inline-block', width: '100%'
    },

    positivity: {
        fontFamily: 'helvetica', fontSize: '12px', paddingTop: '10px', paddingBottom: '10px', borderRadius: '5px', border: '2px solid green', backgroundColor: 'white', margin: '5px', marginTop: '5px',
    },

    positivityButton: {
        border: '1px solid blue',  height: '35px', marginTop: '0px', backgroundColor: 'rgba(255,255,255,1)', margin: '5px',

    },

    shareButton: {
        fontFamily: 'helvetica', fontSize: '12px', borderRadius: '5px', border: '2px solid blue', backgroundColor: 'white', margin: '5px', marginTop: '5px', paddingTop: '6px', paddingBottom: '8px',
        "&:hover": {
            backgroundColor: 'lightgrey'
        },
    },

    fbShareIcon: {
        height: '20px'
    },

    buttonDiv: {
        display: 'inline-block', width: '30%', 'height': '8px'
    }




}

export default styles;

const styles = {

  container: {
        flexWrap: 'nowrap',
        overflow: 'hidden',
        backgroundColor: 'white',
  },

  subContainer: {
        display: 'flex',
        overflow: 'hidden',
        flexWrap: 'nowrap',
        padding: 0,
        height: '300',
  },

  gridList: {
        display: 'flex',
        overflow: 'hidden',
        flexWrap: 'wrap',
        padding: 0,
        height: '300',
  },

      topArticleRoot: {
            position: 'absolute',
            left: 0,
            right: 0,
            height: 160,
            background: 'rgba(0, 0, 0, 0.5)',
            display: 'flex',
            alignItems: 'center',
      },

topArticleTitle: {
      fontSize: '20pt',
      textAlign: 'left',
      fontWeight: 'bold',
      lineHeight: '1em',
      textOverflow: 'ellipsis',
      overflow: 'hidden',
      whiteSpace: 'normal',
      maxHeight: '3em',
      paddingTop: '20px',
      "&:hover": {
            textDecoration: "underline"
      },
      },

topArticleSubtitle: {
      fontSize: '10pt',
      fontWeight: 'medium',
      textAlign: 'left',
      lineHeight: '1.2em',
      textOverflow: 'ellipsis',
      overflow: 'hidden',
      whiteSpace: 'normal',
      maxHeight: '3.6em',
      paddingTop: '5px',
},

      topArticleSecondaryRoot: {
            position: 'absolute',
            left: 0,
            right: 0,
            top: 160,
            height: 30,
            background: 'rgba(0, 0, 0, 0.5)',
            display: 'flex',
            alignItems: 'center',
            paddingBottom: '72px'
      },

      topArticleSecondarySubtitle: {
            fontSize: '12pt',
            textOverflow: 'ellipsis',
            overflow: 'hidden',
            whiteSpace: 'normal',
            paddingBottom: '15px',
      },

      otherTopArticleRoot: {
            position: 'absolute',
            left: 0,
            right: 0,
            height: 50,
            background: 'rgba(0, 0, 0, 0.5)',
            display: 'flex',
            alignItems: 'center',
      },

      otherTopArticleTitle: {
            fontSize: 'calc(10pt + 0.3vw)',
            textAlign: 'left',
            fontWeight: 'bold',
            lineHeight: '1em',
            textOverflow: 'ellipsis',
            overflow: 'hidden',
            whiteSpace: 'normal',
            maxHeight: '2em',
            paddingTop: '10px',
            "&:hover": {
                  textDecoration: "underline"
            },
      },

      otherTopArticleSecondaryRoot: {
            position: 'absolute',
            left: 0,
            right: 0,
            top: 50,
            height: 40,
            paddingBottom: 12,
            background: 'rgba(0, 0, 0, 0.5)',
            display: 'flex',
            alignItems: 'center',
      },

      otherTopArticleSecondarySubtitle: {
            fontSize: '12pt',
            textOverflow: 'ellipsis',
            overflow: 'hidden',
            whiteSpace: 'normal',
            paddingBottom: '15px',
      },

  gridRoot: {
        display: 'inline-block',
        flexWrap: 'wrap',
        paddingTop: '10px',
        justifyContent: 'space-around',
        overflow: 'hidden',
  },

  voteBar: {
        paddingTop: '5px',
        paddingBottom: '5px',

  },
  
  voteIcon: {
        "&:hover": {
              backgroundColor: 'grey',
        },
        borderRadius: '100%',
        color: 'white',
        margin: '1px',
        paddingTop: '12',
        paddingBottom: '12',
        paddingLeft: '2pt',
        paddingRight: '2pt',

  },

positivityScore: {
      marginTop: '12px',
      marginBottom: '12px',
      border: '1px',
      backgroundColor: 'white',
},

}

export default styles;
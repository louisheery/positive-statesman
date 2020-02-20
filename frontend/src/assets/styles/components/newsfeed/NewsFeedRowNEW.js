const styles = {

      container: {
            flexWrap: 'nowrap',
            overflow: 'hidden',
            paddingTop: '20px',
      },

      subContainer: {
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-around',
            overflow: 'hidden',

      },

      gridList: {
            flexWrap: 'nowrap',
            // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
            transform: 'translateZ(0)',
            paddingTop: '5px',

      },

      sectionTitle: {
            "&:hover": {
                  fontWeight: "bold"
            },
      },

      otherTopArticleRoot: {
            borderTop: '1px solid black',
            position: 'absolute',
            left: 0,
            right: 0,
            height: 49,
            display: 'flex',
            alignItems: 'center',

      },

      otherTopArticleTitle: {
            color: 'black',
            fontSize: '12pt',
            textAlign: 'left',
            fontWeight: 'light',
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
            height: 29,
            paddingBottom: 12,
            display: 'flex',
            alignItems: 'center',

      },

      otherTopArticleSecondarySubtitle: {
            color: 'black',
            fontSize: '10pt',
            textOverflow: 'ellipsis',
            overflow: 'hidden',
            whiteSpace: 'normal',
            paddingBottom: '15px',

      },

      gridRoot: {
            display: 'inline-block',
            flexWrap: 'wrap',
            justifyContent: 'space-around',
            overflow: 'hidden',

      },

      voteBar: {
            paddingTop: '5px',
            paddingBottom: '5px',
            borderBottom: '1px solid black',


      },

      positivityScore: {
            marginTop: '12px',
            marginBottom: '12px',
            border: '1px',
            backgroundColor: 'white',
      },

      otherArticleTileVoteDiv: {
            width: '100%'
      },

      rowTitle: {
            textDecoration: 'none',
            color: 'unset'
      },



}

export default styles;
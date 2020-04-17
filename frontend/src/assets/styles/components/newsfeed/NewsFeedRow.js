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
            overflowX: 'hidden',
            paddingTop: '5px',
            
      },

      hyperlinkTitle: {
            textDecoration: 'none',
            color: 'unset',
            '&:hover': {
                  fontWeight: 'bold',
            },
      },

      nonHyperlinkTitle: {
            textDecoration: 'none',
            color: 'unset',
      },

      

}

export default styles;
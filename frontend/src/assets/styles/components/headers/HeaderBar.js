import { fade } from '@material-ui/core/styles';

const styles = {

  toolbar: {
    marginLeft: '80px',
    marginRight: '65px',
  },

  psButton: {
    marginLeft: '20px',
    textTransform: 'none',
  },

  psButtonSmall: {
    color: 'white',
    textDecoration: 'none',
  },

  psButtonSmallText: {
    fontFamily: 'roboto',
    fontSize: '3vw',
  },

  addStoryButton: {
    width: '120px',
  },

  searchBar: {
    position: 'relative',
    borderRadius: '5px',
    backgroundColor: fade('#000', 0.15),
    '&:hover': {
      backgroundColor: fade('#000', 0.25),
    },
    marginLeft: '20px',
    marginRight: '20px',
    width: 'auto',
    maxWidth: '500px',
  },

  searchBarMobile: {
    position: 'relative',
    borderRadius: '5px',
    backgroundColor: fade('#000', 0.15),
    '&:hover': {
      backgroundColor: fade('#000', 0.25),
    },
    marginLeft: '20px',
    marginRight: '20px',
    width: '100%',
    marginTop: '13.5px',
    marginBottom: '13.5px',
  },

  searchBarIcon: {
    paddingLeft: '5px',
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },

  searchBox: {
    color: 'inherit',
    width: '100%'
  },

  searchBoxText: {
    paddingLeft: '30px',
    paddingTop: '10px',
    paddingBottom: '10px',
    width: '100%',
  },

  headerTab: {
    flexGrow: '1',
  },

  flexDiv: {
    flexGrow: '1',
    alignItems: 'center',
    justifyContent: 'center',
  },

  addButton: {
    marginRight: '65px',
  },

  tabBar: {
    backgroundColor: '#007ea7',
    paddingLeft: '5%',
    paddingRight: '5%',
  },

}

export default styles;




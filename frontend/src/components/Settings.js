var categoryBarTabs = ["business",
    "politics",
    "sport",
    "arts",
    "science",
    "technology",
    "travel"]

var defaultCategoryNames = ['Art, Culture & Entertainment', 'Business', 'Law, Government & Politics', 'Science', 'Sport', 'Technology', 'Travel']

var categoryNames = ['Art, Culture & Entertainment', 'Business', 'Law, Government & Politics', 'Science', 'Sport', 'Technology', 'Travel', 'Careers', 'Education', 'Family & Parenting', 'Health & Fitness', 'Food', 'Hobbies & Interests', 'Home & Garden', 'General News', 'Personal Finance', 'Society', 'Pets', 'Style & Fashion', 'Real Estate',]

var publisherNames = ['The Guardian', 'NYTimes', 'FT', 'Reuters', 'The Times', 'Washington Post', 'AFP', 'Time', 'Wall Street Journal', 'Economist', 'Politico', 'BBC News', 'The Hill', 'USA Today', 'NPR', 'CBS News', 'Axios', 'The New Yorker', 'National Review', 'Slate', 'The Atlantic', 'The Week', 'Vanity Fair', 'MSNBC', 'CNN', 'CNN Money', 'Vox', 'Mic', 'Independent', 'The Sun', 'Metro', 'Daily Mail', 'The Telegraph', 'LA Times', 'CNET', 'Engadget', 'The Verge', 'Vice', 'Newsweek', 'Forbes', 'Science Magazine', 'Sky Sports News', 'ESPN', 'Phys.org', 'Sky News', 'TechRadar', 'Digital Spy', 'i News', 'IGN', 'France24', 'Deutsche Welle', 'Euro News', 'CBC', 'Global News', 'National Post', 'MSN', 'NBC News', 'ABC News', 'SCMP', 'Seattle Times', 'Independent IE', 'Evening Standard', 'Wired', 'Fortune', 'Techcrunch', 'US News']

var remainingCategories = ['careers', 'education', 'familyparenting', 'healthfitness', 'food', 'hobbies', 'homegarden', 'personalfinance', 'society', 'pets', 'stylefashion', 'Style & Fashion', 'realestate']

var categoryDictionary = {
    ART: ['arts', 'Art, Culture & Entertainment', 'iab-qagIAB1'],
    BUSINESS: ['business', 'Business', 'iab-qagIAB3'],
    POLITICS: ['politics', 'Law, Government & Politics', 'iab-qagIAB11'],
    SCIENCE: ['science', 'Science', 'iab-qagIAB15'],
    SPORT: ['sport', 'Sport', 'iab-qagIAB17'],
    TECH: ['technology', 'Technology', 'iab-qagIAB19'],
    TRAVEL: ['travel', 'Travel', 'iab-qagIAB20'],
    CAREER: ['careers', 'Careers', 'iab-qagIAB4'],
    EDU: ['education', 'Education', 'iab-qagIAB5'],
    FAMILY: ['familyparenting', 'Family & Parenting', 'iab-qagIAB6'],
    HEALTH: ['healthfitness', 'Health & Fitness', 'iab-qagIAB7'],
    FOOD: ['food', 'Food', 'iab-qagIAB8'],
    HOBBIES: ['hobbies', 'Hobbies & Interests', 'iab-qagIAB9'],
    HOMEGARDEN: ['homegarden', 'Home & Garden', 'iab-qagIAB10'],
    PFINANCE: ['personalfinance', 'Personal Finance', 'iab-qagIAB13'],
    SOCIETY: ['society', 'Society', 'iab-qagIAB14'],
    PETS: ['pets', 'Pets', 'iab-qagIAB16'],
    STYLEFASHION: ['stylefashion', 'Style & Fashion', 'iab-qagIAB18'],
    REALESTATE: ['realestate', 'Real Estate', 'iab-qagIAB21'],
};

var publisherDictionary = {
    GUARDIAN: ['guardian', 'The Guardian', 'The%20Guardian'],
    NYTIMES: ['nytimes', 'NYTimes', 'The%20New%20York%20Times'],
    FT: ['ft', 'FT', 'FT.com%20-%20Mergermarket'],
    REUTERS: ['reuters', 'Reuters', 'Reuters'],
    THETIMES: ['thetimes', 'The Times', 'Sunday%20Times,%20The%20(Ireland)'],
    WASHINGTONPOST: ['washingtonpost', 'Washington Post', 'The%20Washington%20Post'],
    AFP: ['afp', 'AFP', 'AFP%20World%20News'],
    TIME: ['time', 'Time', 'Time'],
    WSJ: ['wsj', 'Wall Street Journal', 'Wall%20Street%20Journal'],
    ECONOMIST: ['economist', 'Economist', 'The%20Economist'],
    POLITICO: ['politico', 'Politico', 'Politico'],
    BBC: ['bbc', 'BBC News', 'BBC.com'],
    THEHILL: ['the hill', 'The Hill', 'The%20Hill'],
    USATODAY: ['usatoday', 'USA Today', 'USA%20Today'],
    NPR: ['npr', 'NPR', 'National%20Public%20Radio'],
    CBSNEWS: ['cbsnews', 'CBS News', 'CBS%20News'],
    AXIOS: ['axios', 'Axios', 'Axios'],
    NEWYORKER: ['newyorker', 'The New Yorker', 'The%20New%20Yorker'],
    NATIONALREVIEW: ['nationalreview', 'National Review', 'National%20Review'],
    SLATE: ['slate', 'Slate', 'Slate'],
    THEATLANTIC: ['theatlantic', 'The Atlantic', 'The%20Atlantic'],
    THEWEEK: ['theweek', 'The Week', 'The%20Week'],
    VANITYFAIR: ['vanityfair', 'Vanity Fair', 'Vanity%20Fair'],
    MSNBC: ['msnbc', 'MSNBC', 'MSNBC'],
    CNN: ['cnn', 'CNN', 'CNN'],
    CNNMONEY: ['cnnmoney', 'CNN Money', 'Money'],
    VOX: ['vox', 'Vox', 'Vox'],
    MIC: ['mic', 'Mic', 'Mic'],
    INDEPENDENT: ['independent', 'Independent', 'The%20Independent%20-%20UK'],
    THESUN: ['thesun', 'The Sun', 'The%20Sun%20-%20UK'],
    METRO: ['metro', 'Metro', 'Metro'],
    DAILYMAIL: ['dailymail', 'Daily Mail', 'Daily%20Mail%20UK'],
    TELEGRAPH: ['telegraph', 'The Telegraph', 'The%20Telegraph'],
    LATIMES: ['latimes', 'LA Times', 'The%20Los%20Angeles%20Times'],
    CNET: ['cnet', 'CNET', 'CNET'],
    ENGADGET: ['engadget', 'Engadget', 'Engadget'],
    THEVERGE: ['theverge', 'The Verge', 'The%20Verge'],
    VICE: ['vice', 'Vice', 'Vice'],
    NEWSWEEK: ['newsweek', 'Newsweek', 'Newsweek'],
    FORBES: ['forbes', 'Forbes', 'Forbes'],
    SCIENCEMAG: ['sciencemag', 'Science Magazine', 'Science'],
    SKYSPORTSNEWS: ['skysportsnews', 'Sky Sports News', 'Sky%20Sports'],
    ESPN: ['espn', 'ESPN', 'ESPN%20US'],
    PHYSORG: ['phys.org', 'Phys.org', 'Phys.org'],
    SKYNEWS: ['skynews', 'Sky News', 'Sky%20News'],
    TECHRADAR: ['techradar', 'TechRadar', 'TechRadar'],
    DIGITALSPY: ['digitalspy', 'Digital Spy', 'Digital%20Spy%20(UK)'],
    INEWS: ['inews', 'i News', 'i%20News'],
    IGN: ['ign', 'IGN', 'IGN'],
    FRANCE24: ['france24', 'France24', 'France%2024%20-%20English'],
    DW: ['dw', 'Deutsche Welle', 'Deutsche%20Welle'],
    EURONEWS: ['euronews', 'Euro News', 'Euro%20News%20-%20English'],
    CBC: ['cbc', 'CBC', 'CBC'],
    GLOBALNEWS: ['globalnews', 'Global News', 'Global%20News'],
    NATIONALPOST: ['nationalpost', 'National Post', 'National%20Post%20-%20Canada'],
    MSN: ['msn', 'MSN', 'MSN%20Money'],
    NBCNEWS: ['nbcnews', 'NBC News', 'NBC%20News'],
    ABCNEWSAU: ['abcnews', 'ABC News', 'ABC%20News%20Australia'],
    SCMP: ['scmp', 'SCMP', 'South%20China%20Morning%20Post'],
    SEATTLETIMES: ['seattletimes', 'Seattle Times', 'The%20Seattle%20Times'],
    INDEPENDENTIE: ['independentie', 'Independent IE', 'Irish%20Independent'],
    EVENINGSTANDARD: ['eveningstandard', 'Evening Standard', 'Evening%20Standard'],
    WIRED: ['wired', 'Wired', 'Wired%20UK'],
    FORTUNE: ['fortune', 'Fortune', 'Fortune'],
    TECHCRUNCH: ['techcrunch', 'Techcrunch', 'TechCrunch'],
    USNEWS: ['usnews', 'US News', 'U.S.%20News'],
};

export { categoryBarTabs, defaultCategoryNames, remainingCategories, categoryNames, publisherNames, categoryDictionary, publisherDictionary }
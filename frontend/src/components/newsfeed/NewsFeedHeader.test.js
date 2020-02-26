import React from 'react'
import { render, fireEvent, waitForElement } from '@testing-library/react'
import { BrowserRouter, Redirect } from 'react-router-dom'
import { FetchMock, fetchMock } from '@react-mock/fetch'
import NewsFeedHeader from './NewsFeedHeader'

describe('User sees correct number of articles in top section', () => {
    test('on phone view two articles are displayed', async () => {
        const { findAllByText } = render(
            <BrowserRouter>
                <FetchMock matcher={"*"} method='POST' response={JSON.stringify(sampleArticles)}>
                    <NewsFeedHeader width='xs' />
                </FetchMock>
            </BrowserRouter>
        )
        const titles = await waitForElement(() => findAllByText(/title/i))
        expect(titles.length).toEqual(2)
    })
    test('on tablet view four articles are displayed', async () => {
        const { findAllByText } = render(
            <BrowserRouter>
                <FetchMock matcher={"*"} method='POST' response={JSON.stringify(sampleArticles)}>
                    <NewsFeedHeader width='sm' />
                </FetchMock>
            </BrowserRouter>
        )
        const titles = await waitForElement(() => findAllByText(/title/i))
        expect(titles.length).toEqual(4)
    })
    test('on laptop view four articles are displayed', async () => {
        const { findAllByText } = render(
            <BrowserRouter>
                <FetchMock matcher={"*"} method='POST' response={JSON.stringify(sampleArticles)}>
                    <NewsFeedHeader width='lg' />
                </FetchMock>
            </BrowserRouter>
        )
        const titles = await waitForElement(() => findAllByText(/title/i))
        expect(titles.length).toEqual(6)
    })
})


const sampleArticles = [{
    "id": 15,
    "title": "Title",
    "url": "https://www.theepochtimes.com/homeless-dad-gets-makeover-from-mrs-hot-handz-giving-him-a-much-needed-lift-a-second-chance_3192650.html",
    "image_url": "https://img.theepochtimes.com/assets/uploads/2020/02/14/Homeless-Dad-Makeover-i-300x180.jpg",
    "publisher": "The Epoch Times",
    "publish_date": "2020-02-14T15:44:33Z",
    "sentiment_score": 0.9992,
    "text_snippet": "",
    "text_full": "Homeless Dad Gets Makeover From ‘Mrs Hot Handz,’ Giving Him a Much-Needed Lift & a Second Chance\n\nSixty-year-old Larry Green is one of the thousands of Americans living in big cities who struggle with homelessness, but when Father’s Day 2019 came around, members of his community stepped to give him a life-changing makeover and a renewed sense of self-worth.\n\nThough a loving father of four children, with 11 grandchildren and 3 great-grandchildren, Dallas, Texas, resident Green hasn’t had a place to call his own for the past 20 years. Taking charge of the makeover was stylist Tabitha Lorick, better known as “Mrs. Hot Handz.”\n\n“We just want to make him feel good and show him just because he is not financially stable right now that he can still get appreciated,” she told KTVT.\n\nFor Green, the makeover meant a lot more than just a new haircut. “She is letting me know that I am still human,” he said.\n\nFor the makeover, Mrs. Hot Handz shaved Green’s dreadlocks and trimmed his overgrown beard cleanly. But special treatment from the stylist was just the first part of Green’s special makeover. “I know she’s made me look like somebody,” he told KTVT after his date at the salon session. “I don’t feel as low. I don’t feel like I’m nobody.”\n\nFollowing the makeover, Green got some wardrobe help from the stylist’s friend Ricky Wilkerson, who took him shopping for a new outfit. Thanks to help from some clothing retailers, including Well Groomed Man and Lust for Life Shoes, they were able to get Green fitted for a stylish suit as well as give him a new pair of shoes.\n\nTo cap off the special Father’s Day occasion, Mrs. Hot Handz and her friends also gave Green an experience he hadn’t had in a long time: a good night’s sleep in comfortable surroundings. As she explained on a GoFundMe page set up for Green, “He also enjoyed a hearty meal at a local restaurant and a nights stay at a nearby hotel!”\n\nThe ultimate goal is to help Green get off the street and into more permanent housing and employment. Stylist Tabitha explained on the GoFundMe page, “We are asking for your help financially as we attempt to extend Mr. Larry’s stay at the hotel and have money for food and toiletries during the upcoming months.”\n\nShe adds, “Let’s serve our fellow brother as he begins his journey to serve himself!” While over $2,000 has been raised so far, the campaign hopes to reach a much higher target of $5,000 in order to give Green the boost he needs. The ultimate goal for him is to reconnect with his kids and be proud of his life.\n\nOn his newly created Instagram account, Green recognized how much Mrs. Hot Handz and others in the community had done for him, saying, “My new family […] we not blood but The love is just as strong.”\n\nAs for Mrs. Hot Handz, she was surprised and delighted at all the positive reactions from people in the community and online. “We did not do this to get anything just the joy that we get when we give,” she wrote on Facebook, giving the credit to God instead. However, sponsorship from good Samaritans would permit her to continue giving makeovers she says.\n\nIn the meantime, Green has been through an incredible transformation that hasn’t just changed his look or improved his spirits; it’s also put him closer to having a home and a life of his own that he hasn’t had in a very long time.",
    "user_score_positive": 35,
    "user_score_neutral": 27,
    "user_score_negative": 25,
    "user_score_count": 87,
    "categories": [],
    "locations": [
        46,
        45
    ],
    "creation_date": "2020-02-14T15:49:13.070990Z"
},
{
    "id": 5,
    "title": "Title",
    "url": "https://www.tuscaloosanews.com/news/20200214/tchs-freshmen-hope-to-turn-rock-band-dreams-into-musical-reality?rssfeed=true",
    "image_url": "https://www.tuscaloosanews.com/storyimage/DA/20200214/NEWS/200219451/AR/0/AR-200219451.jpg",
    "publisher": "Tuscaloosa News - Alabama",
    "publish_date": "2020-02-14T15:44:52Z",
    "sentiment_score": 0.9967,
    "text_snippet": "",
    "text_full": "A group of Tuscaloosa County High freshman have big dreams and a band that as yet has no name.\n\n\t\t\t\t\tMany big things have been birthed in garages, lofts and backyard workshops. Apple and Microsoft and not a few rock ‘n’ roll dreams have begun in just such humble places.\nFive freshmen at Tuscaloosa County High School hope their band can become one of those great American success stories. John David Patrick, 15, Riley Leavell, 14, Matt McCracken, 15, Randi Hope Lollar, 14, and Caroline Gibson, 14, form the band.\nWhen asked the name of their band, they all laugh. So far, even after playing a number of gigs around the community, they do not yet have a name and fear that the moniker, “The Band With No Name” might stick. Nevertheless, music is a big part of their lives and they hope it will remain so.\n“Music has been a part of my life for my entire life,” Riley said. “I’ve been singing and playing an instrument for as long as I can remember. My dad sings, my mom sings, too, whether she admits it or not.”\nRiley said he picked up the guitar about five years ago, and it has become his primary instrument. Matt also plays guitar; however, he favors the electric to Riley’s acoustic.\n“I’m kind of like Riley. I have a musical family,” Matt said. “A lot of my dad’s side of the family plays instruments. My mom will tell you that even from a young age I would bang on pots like drums all the time. I’ve always enjoyed it. It’s been a passion of mine.”\nJohn David’s passion is more along classical lines. He is a bass trombone player in the Tuscaloosa County High Jazz Band and he loves jazz music. Long term, he said he would love to play in an orchestra. His role as bass guitarist came about only after his mother purchased a bass for him and his friends invited him to join their band.\nRandi,  although not coming from a musical family, said she has been a singer all of her life. Her main influence has been Adele.\n“I have always loved her. I know it sounds weird but I just resonate with her,” Randi said.\nShe plays guitar and ukulele. Caroline said she sings when she is part of the group, but she does play guitar. She lists her musical influences as being Carrie Underwood, Kelsea Ballerini, Lauren Daigle and Lauren Alaina.\nCaroline has a bit more performance experience under her belt than her band mates.\n“I sing on the Word Community Church worship team, and I do the national anthem at Alabama games and stuff like that,” Caroline said.\nShe has sung the national anthem for University of Alabama basketball, softball, gymnastics, wheelchair basketball and hockey. Caroline said she wouldn’t mind singing before the crowd in Bryant-Denny Stadium if the opportunity presented itself.\n“I’m always excited,” she said. “There’s always going to be a bit of nervousness in you. It’s not like fear or anything, but it’s more like excitement for me than it is nerves.”\nSo far, no one in the group has written a song. They do covers of popular tunes from a variety of genres. They admit with a laugh that they are very popular with senior citizens since they have played a number of times for assisted living and retirement communities, but their aspirations don’t stop there.\n“I would like to see us playing in the future with some bigger bands,” said Matt. “We plan on playing the Live at the Plaza in Tuscaloosa and eventually working up to bigger venues.”\n“I’ve always wanted to record a Christmas album,” added Riley. “Since we’ve kind of joined together as a band, I’ve wanted to open for a bigger band, maybe at the (Tuscaloosa) Amphitheater or something like that.”\nWhile it is a bit early to think of music as a career, each member of the group wants to stay involved with music.\n“I don’t know what I want to do, but I want it to be in music,” Randi said.",
    "user_score_positive": 3,
    "user_score_neutral": 1,
    "user_score_negative": 3,
    "user_score_count": 7,
    "categories": [],
    "locations": [
        21,
        22,
        23
    ],
    "creation_date": "2020-02-14T15:49:12.490375Z"
},
{
    "id": 4,
    "title": "Title",
    "url": "https://simplywall.st/stocks/us/software/nasdaq-sito/sito-mobile/news/how-does-sito-mobile-ltd-nasdaqsito-affect-your-portfolio-volatility/",
    "image_url": "https://images.simplywall.st/company/47DEE58C-3671-4806-BA0D-FD9EE22F4106/cover?size=main-header",
    "publisher": "Simply Wall St News",
    "publish_date": "2020-02-14T15:44:53Z",
    "sentiment_score": 0.9937,
    "text_snippet": "",
    "text_full": "If you’re interested in SITO Mobile, Ltd. (NASDAQ:SITO), then you might want to consider its beta (a measure of share price volatility) in order to understand how the stock could impact your portfolio. Modern finance theory considers volatility to be a measure of risk, and there are two main types of price volatility. The first type is company specific volatility. Investors use diversification across uncorrelated stocks to reduce this kind of price volatility across the portfolio. The second sort is caused by the natural volatility of markets, overall. For example, certain macroeconomic events will impact (virtually) all stocks on the market.\n\nSome stocks are more sensitive to general market forces than others. Beta can be a useful tool to understand how much a stock is influenced by market risk (volatility). However, Warren Buffett said ‘volatility is far from synonymous with risk’ in his 2014 letter to investors. So, while useful, beta is not the only metric to consider. To use beta as an investor, you must first understand that the overall market has a beta of one. A stock with a beta below one is either less volatile than the market, or more volatile but not corellated with the overall market. In comparison a stock with a beta of over one tends to be move in a similar direction to the market in the long term, but with greater changes in price.\n\nCheck out our latest analysis for SITO Mobile\n\nGiven that it has a beta of 1.18, we can surmise that the SITO Mobile share price has been fairly sensitive to market volatility (over the last 5 years). Based on this history, investors should be aware that SITO Mobile are likely to rise strongly in times of greed, but sell off in times of fear. Share price volatility is well worth considering, but most long term investors consider the history of revenue and earnings growth to be more important. Take a look at how SITO Mobile fares in that regard, below.\n\nSITO Mobile is a noticeably small company, with a market capitalisation of US$5.7m. Most companies this size are not always actively traded. It takes less money to influence the share price of a very small company. This may explain the excess volatility implied by this beta value.\n\nBeta only tells us that the SITO Mobile share price is sensitive to broader market movements. This could indicate that it is a high growth company, or is heavily influenced by sentiment because it is speculative. Alternatively, it could have operating leverage in its business model. Ultimately, beta is an interesting metric, but there’s plenty more to learn. This article aims to educate investors about beta values, but it’s well worth looking at important company-specific fundamentals such as SITO Mobile’s financial health and performance track record. I highly recommend you dive deeper by considering the following:\n\nIf you spot an error that warrants correction, please contact the editor at editorial-team@simplywallst.com. This article by Simply Wall St is general in nature. It does not constitute a recommendation to buy or sell any stock, and does not take account of your objectives, or your financial situation. Simply Wall St has no position in the stocks mentioned.\n\n\n\nWe aim to bring you long-term focused research analysis driven by fundamental data. Note that our analysis may not factor in the latest price-sensitive company announcements or qualitative material. Thank you for reading.",
    "user_score_positive": 1,
    "user_score_neutral": 1,
    "user_score_negative": 1,
    "user_score_count": 3,
    "categories": [],
    "locations": [
        20
    ],
    "creation_date": "2020-02-14T15:49:12.430804Z"
},
{
    "id": 6,
    "title": "Title",
    "url": "http://www.stereoboard.com/content/view/227351/9",
    "image_url": "http://static.stereoboard.com/images/artistimages/pins.jpg",
    "publisher": "Stereoboard",
    "publish_date": "2020-02-14T15:44:47Z",
    "sentiment_score": 0.9551,
    "text_snippet": "",
    "text_full": "Hot Slick is a dynamic indie rock number that was produced by Jamie Hince of the Kills and renowned producer Rich Woodcraft, who've both worked with the band on previous tracks, Serve The Rich and Ponytail, respectively.\n\nTo celebrate the song's release, PINS will play a free show tonight (February 14) at Belgrave Music Hall and Canteen in Leeds. The band also have a spring tour in the diary that kicks off on February 20 in Brighton. Tickets are on sale now.\n\nPins Upcoming Tour Dates are as follows\n\nClick here to compare & buy Pins Tickets at Stereoboard.com.\n\nLet Us Know What You Think - Leave A Comment!",
    "user_score_positive": 1,
    "user_score_neutral": 0,
    "user_score_negative": 1,
    "user_score_count": 2,
    "categories": [],
    "locations": [
        24,
        25
    ],
    "creation_date": "2020-02-14T15:49:12.528074Z"
},
{
    "id": 17,
    "title": "Title",
    "url": "https://www.thejournal.ie/two-flights-shannon-medical-emergencies-5007789-Feb2020/",
    "image_url": "https://c3.thejournal.ie/media/2020/02/shannon-1-2-630x459.jpg",
    "publisher": "The Journal - Ireland",
    "publish_date": "2020-02-14T15:44:33Z",
    "sentiment_score": 0.8885,
    "text_snippet": "",
    "text_full": "TWO TRANSATLANTIC PASSENGER jets have made unscheduled landings at Shannon Airport today after their crews declared medical emergencies.\n\nUnited Airlines flight UA-121 diverted to Shannon after the crew reported they needed to seek medical attention for a passenger. There were 174 passengers and crew on board the Boeing 767-400 jet which was travelling from Barcelona in Spain to Newark, New Jersey in the United States.\n\nThe flight was approaching the south coast of Ireland at around 11.45am when the flight crew advised air traffic controllers of their emergency and requested clearance to divert to Shannon.\n\nThe pilot also sought permission to descend and dump aviation fuel off the south. This was to ensure that the aircraft touched down within safe landing weight limits.\n\nAfter spending about 20 minutes jettisoning fuel, the flight diverted to Shannon where it landed safely at 12.44pm. The jet was met on arrival by airport fire and rescue crews who are mobilised as part of procedures when an aircraft dumps fuel before landing.\n\nThe aircraft taxied to the terminal where it was met by airport authorities and National Ambulance Service paramedics. A male passenger was removed from the aircraft and after being assessed by paramedics, was transported to University Hospital Limerick for treatment.\n\nThe flight is expected to resume its journey later this afternoon.\n\nEarlier, a British Airways flight travelling from The Bahamas in the Caribbean to Heathrow in London also diverted to seek medical attention for a passenger.\n\nBritish Airways flight BA-252 was almost six hours into its flight and still had about 90 minutes from London when the crew declared a medical emergency and requested permission to divert to Shannon.\n\nThe Boeing 777-200 jet landed safely at 9.50am and was met at the terminal by ambulance paramedics. A passenger was removed to University Hospital Limerick for treatment. The flight continued its journey to London later.\n\nShannon is the country’s busiest airport for aircraft diversions. It has the longest runway in Ireland at almost 3.2km (10,495ft) and capable of handling all passenger and cargo aircraft types.",
    "user_score_positive": 4,
    "user_score_neutral": 1,
    "user_score_negative": 1,
    "user_score_count": 6,
    "categories": [],
    "locations": [
        55,
        54,
        56,
        58,
        57,
        53,
        59,
        52
    ],
    "creation_date": "2020-02-14T15:49:13.159413Z"
},
{
    "id": 11,
    "title": "Title",
    "url": "https://www.theepochtimes.com/los-angeles-to-dismiss-66000-marijuana-convictions-da_3238406.html",
    "image_url": "https://img.theepochtimes.com/assets/uploads/2018/11/03/GettyImages-1052403254-300x180.jpg",
    "publisher": "The Epoch Times",
    "publish_date": "2020-02-14T15:44:33Z",
    "sentiment_score": 0.7506,
    "text_snippet": "",
    "text_full": "About 66,000 marijuana convictions in Los Angeles County will be dismissed, according to the county’s district attorney on Thursday.\n\nThe dismissals include 62,000 felony convictions for marijuana cases dating back to 1961 and around 4,000 misdemeanor cases, District Attorney Jackie Lacey’s office said in a news release.\n\n“I am privileged to be part of a system dedicated to finding innovative solutions and implementing meaningful criminal justice reform that gives all people the support they need to build the life they deserve,” she said. “This is a clear demonstration that automatic record clearance is possible at scale and can help to right the wrongs of the failed war on drugs.”\n\nHer office said that about 53,000 people will obtain receive conviction relief, saying that 32 percent are black, 20 percent are white, 45 percent are Latino, and 3 percent are unknown.\n\n“As a result of our actions, these convictions should no longer burden those who have struggled to find a job or a place to live because of their criminal record,” Lacey said in a press conference in announcing the move. She added that it’s the largest mass dismissal of marijuana cases in state history.\n\nIn 2016, California voters legalized recreational marijuana usage in a referendum. The initiative also made it possible for people who were previously convicted of possessing, growing, selling, or transporting marijuana to get reduced sentences.\n\nHer office worked with Code for America, a nonprofit that uses a program to find decades-old cases among court documents. After the latest move, the organization will have helped dismiss more than 85,000 marijuana in California, according to an official in the news release.\n\nLacey is also seeking reelection. An opponent of her’s said that she is not doing enough on criminal-justice reform. But a spokesperson for her office told The Wall Street Journal that she began a program that led to the dismissals last year.\n\n“The facts and the timeline show that this decision was based on seeking justice for all, not politics,” the spokeperson said.",
    "user_score_positive": 0,
    "user_score_neutral": 0,
    "user_score_negative": 0,
    "user_score_count": 0,
    "categories": [],
    "locations": [
        35,
        36
    ],
    "creation_date": "2020-02-14T15:49:12.742822Z"
}
]
import React from 'react'
import { render } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import NewsFeedRowItem from './NewsFeedRowItem'

describe('Article in header displays all important information', () => {
    let getByText, getByLabelText
    beforeEach(() => {
        ({ getByText, getByLabelText } = render(
            <BrowserRouter>
                <NewsFeedRowItem article={sampleArticle} width='lg' />
            </BrowserRouter>
        ))
    })
    test('title displayed', () => {
        getByText(sampleArticle.title)
    })
    test('publisher displayed', () => {
        getByText(sampleArticle.publisher)
    })
    test('positive voting button displayed', () => {
        getByLabelText(/positive/i)
    })
    test('neutral voting button displayed', () => {
        getByLabelText(/neutral/i)
    })
    test('negative voting button displayed', () => {
        getByLabelText(/negative/i)
    })
    test('score displayed', () => {
        getByText(/100/i)
    })
})

describe('sentiment score is displayed in correct color', () => {
    test('green if 100% positivity', () => {
        sampleArticle.sentiment_score = 1
        const { getByText, getByLabelText } = render(
            <BrowserRouter>
                <NewsFeedRowItem article={sampleArticle} width='lg' />
            </BrowserRouter>
        )
        expect(getByText(/100/i).style.color).toEqual("green")
    })
    test('orange if 55% positivity', () => {
        sampleArticle.sentiment_score = 0.1
        const { getByText } = render(
            <BrowserRouter>
                <NewsFeedHeaderItem article={sampleArticle} width='lg' />
            </BrowserRouter>
        )
        expect(getByText(/55/i).style.color).toEqual("orange")
    })
    test('red if 0% positivity', () => {
        sampleArticle.sentiment_score = -1
        const { getByText } = render(
            <BrowserRouter>
                <NewsFeedHeaderItem article={sampleArticle} width='lg' />
            </BrowserRouter>
        )
        expect(getByText(/0/i).style.color).toEqual("red")
    })
})

let sampleArticle = {
    "id": 15,
    "title": "bla",
    "url": "https://www.news.com/article/1",
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
}
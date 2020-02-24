import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import { FetchMock, fetchMock } from '@react-mock/fetch'
import ArticleVote from './ArticleVote'

describe('User can vote on articles successfully', () => {
    const api = '/api/user-feedback/'
    const id = 1
    let getByLabelText
    beforeEach(() => {
        ({ getByLabelText } = render(
            <BrowserRouter>
                <FetchMock matcher={api} method='POST' response={JSON.stringify({})}>
                    <ArticleVote articleId={id} />
                </FetchMock>
            </BrowserRouter>
        ))
    })
    test('clicking on positive smiley sends positive vote to api', () => {
        fireEvent.click(getByLabelText(/positiveVote/i))
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ pk: id, vote: 'positive' })
    })
    test('clicking on neutral smiley sends neutral vote to api', () => {
        fireEvent.click(getByLabelText(/neutralVote/i))
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ pk: id, vote: 'neutral' })
    })
    test('clicking on negative smiley sends negative vote to api', () => {
        fireEvent.click(getByLabelText(/negativeVote/i))
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ pk: id, vote: 'negative' })
    })
})
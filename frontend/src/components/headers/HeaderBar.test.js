import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import HeaderBar from './HeaderBar'
import { BrowserRouter } from 'react-router-dom'
import { FetchMock, fetchMock } from '@react-mock/fetch';


describe('User can add story successfully', () => {
    const url = 'https://www.newssite.com/article/1'
    const api = '/api/submit-article/'
    let getByText, getByPlaceholderText, queryByPlaceholderText, queryByText
    beforeEach(() => {
        ({ getByText, getByPlaceholderText, queryByPlaceholderText, queryByText } = render(
            <BrowserRouter>
                <FetchMock matcher={api} method='POST' response={JSON.stringify({})}>
                    <HeaderBar />
                </FetchMock>
            </BrowserRouter>
        ))
    })
    test('add story button visible', () => {
        getByText(/add/i)
    })
    test('text field NOT visible', () => {
        expect(queryByPlaceholderText(/url/i)).toBeNull()
    })
    test('submit button NOT visible', () => {
        expect(queryByText(/submit/i)).toBeNull()
    })
    test('add story button NOT visible after clicking add story button', () => {
        fireEvent.click(getByText(/add/i))
        expect(queryByText(/add/i)).toBeNull()
    })
    test('text field visible after clicking add story button', () => {
        fireEvent.click(getByText(/add/i))
        getByPlaceholderText(/url/i)
    })
    test('submit button visible after clicking add story button', () => {
        fireEvent.click(getByText(/add/i))
        getByText(/submit/i)
    })
    test('user can submit the url by clicking on submit button', () => {
        fireEvent.click(getByText(/add/i))
        fireEvent.change(getByPlaceholderText(/url/i), { target: { value: url } })
        fireEvent.click(getByText(/submit/i))
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ url: url })
    })

})

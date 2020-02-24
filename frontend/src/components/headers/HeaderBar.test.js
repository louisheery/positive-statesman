import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import HeaderBar from './HeaderBar'
import { BrowserRouter, MemoryRouter, Route, Redirect } from 'react-router-dom'
import { FetchMock, fetchMock } from '@react-mock/fetch';


describe('user can interact with logo', () => {
    let getByLabelText
    beforeEach(() => {
        ({ getByLabelText } = render(
            <BrowserRouter>
                <Redirect to="/business/" />
                <HeaderBar />
            </BrowserRouter>
        ))
    })
    test('logo visible', () => {
        getByLabelText(/logo/i)
    })
    test('user get redirected to home page when clicking on logo', () => {
        fireEvent.click(getByLabelText(/logo/i))
        expect(location.pathname).toBe('/')
    })

})



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
    test('user can submit the url by hitting enter in text field', () => {
        fireEvent.click(getByText(/add/i))
        const textField = getByPlaceholderText(/url/i)
        fireEvent.change(textField, { target: { value: url } })
        fireEvent.keyDown(textField, { key: 'Enter', keyCode: 13 })
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ url: url })
    })
    test('submit button + text field disappear and add story button reappears after clicking on submit button', () => {
        fireEvent.click(getByText(/add/i))
        fireEvent.click(getByText(/submit/i))
        expect(queryByText(/submit/i)).toBeNull()
        expect(queryByPlaceholderText(/url/i)).toBeNull()
        getByText(/add/i)
    })
    test('submit button + text field disappear and add story button reappears after hitting enter in text field', () => {
        fireEvent.click(getByText(/add/i))
        fireEvent.keyDown(getByPlaceholderText(/url/i), { key: 'Enter', keyCode: 13 })
        expect(queryByText(/submit/i)).toBeNull()
    })
})


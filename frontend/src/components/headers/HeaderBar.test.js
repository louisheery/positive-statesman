import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import { BrowserRouter, Redirect } from 'react-router-dom'
import { FetchMock, fetchMock } from '@react-mock/fetch'
import HeaderBar from './HeaderBar'
import { Provider } from 'react-redux'
import configureStore from 'redux-mock-store'

const mockStore = configureStore([])



describe('user can interact with logo', () => {
    let getByLabelText
    let store
    beforeEach(() => {
        store = mockStore({reducer: {
            isLoggedIn: false
        }});
        ({ getByLabelText } = render(
            <Provider store={store}>
                <BrowserRouter>
                    <Redirect to="/categories/business/" />
                    <HeaderBar />
                </BrowserRouter>
            </Provider>
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
    let store
    let getByLabelText, getByPlaceholderText, queryByPlaceholderText, queryByLabelText
    beforeEach(() => {
        store = mockStore({reducer: {
            isLoggedIn: false
        }});
        ({ getByLabelText, getByPlaceholderText, queryByPlaceholderText, queryByLabelText } = render(
            <Provider store={store}>
                <BrowserRouter>
                    <FetchMock matcher={api} method='POST' response={JSON.stringify({})}>
                        <HeaderBar />
                    </FetchMock>
                </BrowserRouter>
            </Provider>
        ))
    })
    test('add story button visible', () => {
        getByLabelText(/add/i)
    })
    test('text field NOT visible', () => {
        expect(queryByPlaceholderText(/url/i)).toBeNull()
    })
    test('submit button NOT visible', () => {
        expect(queryByLabelText(/submit/i)).toBeNull()
    })
    test('add story button NOT visible after clicking add story button', () => {
        fireEvent.click(getByLabelText(/add/i))
        expect(queryByLabelText(/add/i)).toBeNull()
    })
    test('text field visible after clicking add story button', () => {
        fireEvent.click(getByLabelText(/add/i))
        getByPlaceholderText(/url/i)
    })
    test('submit button visible after clicking add story button', () => {
        fireEvent.click(getByLabelText(/add/i))
        getByLabelText(/submit/i)
    })
    test('user can submit the url by clicking on submit button', () => {
        fireEvent.click(getByLabelText(/add/i))
        fireEvent.change(getByPlaceholderText(/url/i), { target: { value: url } })
        fireEvent.click(getByLabelText(/submit/i))
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ url: url })
    })
    test('user can submit the url by hitting enter in text field', () => {
        fireEvent.click(getByLabelText(/add/i))
        const textField = getByPlaceholderText(/url/i)
        fireEvent.change(textField, { target: { value: url } })
        fireEvent.keyDown(textField, { key: 'Enter', keyCode: 13 })
        const [, { body }] = fetchMock.lastCall(api, 'POST')
        expect(JSON.parse(body)).toEqual({ url: url })
    })
    test('submit button + text field disappear and add story button reappears after clicking on submit button', () => {
        fireEvent.click(getByLabelText(/add/i))
        fireEvent.click(getByLabelText(/submit/i))
        expect(queryByLabelText(/submit/i)).toBeNull()
        expect(queryByPlaceholderText(/url/i)).toBeNull()
    })
    test('submit button + text field disappear and add story button reappears after hitting enter in text field', () => {
        fireEvent.click(getByLabelText(/add/i))
        fireEvent.keyDown(getByPlaceholderText(/url/i), { key: 'Enter', keyCode: 13, currentTarget: null })
        expect(queryByLabelText(/submit/i)).toBeNull()
    })
})


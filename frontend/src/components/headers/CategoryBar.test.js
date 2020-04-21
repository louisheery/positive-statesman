import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import { BrowserRouter, Redirect } from 'react-router-dom'
import CategoryBar from './CategoryBar'

describe('user gets redirected to category pages', () => {
    let getByText
    beforeEach(() => {
        ({ getByText } = render(
            <BrowserRouter>
                <CategoryBar />
            </BrowserRouter>
        ))
    })
    test('business link works', () => {
        fireEvent.click(getByText(/business/i))
        expect(location.pathname).toBe('/categories/business')
    })
    test('politics link works', () => {
        fireEvent.click(getByText(/politics/i))
        expect(location.pathname).toBe('/categories/politics')
    })
    test('sport link works', () => {
        fireEvent.click(getByText(/sport/i))
        expect(location.pathname).toBe('/categories/sport')
    })
    test('arts link works', () => {
        fireEvent.click(getByText(/arts/i))
        expect(location.pathname).toBe('/categories/arts')
    })
    test('science link works', () => {
        fireEvent.click(getByText(/science/i))
        expect(location.pathname).toBe('/categories/science')
    })
})
describe('User gets redirected to home page', () => {
    test('home link works', () => {
        const { getByText } = render(
            <BrowserRouter>
                <CategoryBar />
                <Redirect to="/test" />
            </BrowserRouter>
        )
        fireEvent.click(getByText(/home/i))
        expect(location.pathname).toBe('/')
    })
})

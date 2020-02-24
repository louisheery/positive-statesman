import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
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
        expect(location.pathname).toBe('/business')
    })
    test('politics link works', () => {
        fireEvent.click(getByText(/politics/i))
        expect(location.pathname).toBe('/politics')
    })
    test('sport link works', () => {
        fireEvent.click(getByText(/sport/i))
        expect(location.pathname).toBe('/sport')
    })
    test('arts link works', () => {
        fireEvent.click(getByText(/arts/i))
        expect(location.pathname).toBe('/arts')
    })
    test('science link works', () => {
        fireEvent.click(getByText(/science/i))
        expect(location.pathname).toBe('/science')
    })

})

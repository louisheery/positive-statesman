import React from 'react'
import { render, fireEvent } from '@testing-library/react'
import { FetchMock, fetchMock } from '@react-mock/fetch'
import { BrowserRouter } from 'react-router-dom'
import TimeSeries from './TimeSeries'

describe('Time series component renders correctly', () => {
    let getAllByText
    beforeEach(() => {
        ({ getAllByText  } = render(
            <BrowserRouter>
                <FetchMock matcher={"*"} method='POST' response={JSON.stringify(sampleResponse)}>
                    <TimeSeries param="categories" title="Title" description="description"/>
                </FetchMock>
            </BrowserRouter>
        ))
    })
    test('Title visible', () => {
        getAllByText(/title/i)
    })
    test('Description visible', () => {
        getAllByText(/description/i)
    })
})

const sampleResponse = [
    {
      "date": "2020-04-18",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-19",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-20",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-21",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-22",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-23",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    },
    {
      "date": "2020-04-24",
      "business": "0",
      "politics": "0",
      "sport": "0",
      "arts": "0",
      "science": "0",
      "technology": "0",
      "travel": "0"
    }
  ]
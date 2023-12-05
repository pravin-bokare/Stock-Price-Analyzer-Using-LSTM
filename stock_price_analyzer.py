import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyzer
    
    Shown are stock prices of Apple
    """
)

ticker_symbol = st.text_input('Enter Stock Symbol','AAPL', key='placeholder')

#ticker_symbol = 'AAPL'

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input('Input Starting Date',
                               datetime.date(2019, 1, 1))

with col2:
    end_date = st.date_input('Input Ending Date',
                               datetime.date(2023, 6, 2))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d',
                                start=f'{start_date}',
                                end=f'{end_date}')
st.write(f'''{ticker_symbol}''')
st.dataframe(ticker_df)


def close_price_analysis(stock_data, ticker):
    # What was the highest closing price for the stock?
    max_closing_price = stock_data["Close"].max()
    st.markdown(f"__Highest Close price for {ticker}:__ {round(max_closing_price, 4)}")

    # When was the highest closing price for the stock observed?
    max_date = stock_data[stock_data["Close"] == max_closing_price].index[0]
    st.markdown(f"__Highest Close Price for {ticker} was observed on:__ {max_date}")

    # What was the lowest closing price for the stock?
    min_closing_price = stock_data["Close"].min()
    st.markdown(f"__Lowest Close price for {ticker}:__ {round(min_closing_price, 4)}")

    # When was the lowest closing price for the stock observed?
    min_date = stock_data[stock_data["Close"] == min_closing_price].index[0]
    st.markdown(f"__Lowest Close Price for {ticker} was observed on:__ {min_date}")


st.markdown("### Basic Stock Price Analysis")
close_price_analysis(ticker_df, ticker_symbol)

st.write(
    '''
    # Daily Closing Price Chart
    '''
)
st.line_chart(ticker_df.Close)

st.write(
    '''
    # Volumes of Shares traded each day
    '''
)
st.line_chart(ticker_df.Volume)
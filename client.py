import streamlit as st
import requests

CURRENCY_OPTIONS = [
    "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "HKD", "NZD",
    "SEK", "NOK", "SGD", "ZAR", "KRW", "MXN", "BRL", "RUB", "*TRY", "AED", "PLN"
]

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"].get(to_currency, None)
    else:
        st.error("Failed to fetch exchange rates.")
        return None


st.title("Currency Converter")
from_currency = st.selectbox("From Currency", CURRENCY_OPTIONS, index=0)
to_currency = st.selectbox("To Currency", CURRENCY_OPTIONS, index=1)
amount = st.number_input("Amount", min_value=1.0, value=1.0)
if st.button("Convert"):
    if from_currency == to_currency:
        st.warning("Please select two different currencies.")
    else:
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate:
            converted_amount = amount * exchange_rate
            st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            st.error(f"Unable to get the exchange rate from {from_currency} to {to_currency}.")

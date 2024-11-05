import streamlit as st
import socket

CURRENCY_OPTIONS = [
    "USD", "EUR", "GBP", "INR", "JPY", "CAD", "AUD", "CHF", "CNY", "HKD", "NZD",
    "SEK", "NOK", "SGD", "ZAR", "KRW", "MXN", "BRL", "RUB", "TRY", "AED", "PLN"
]

def get_converted_amount_via_server(from_currency, to_currency, amount):
    server_address = ('localhost', 8090)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        message = f"{from_currency},{to_currency},{amount}"
        client_socket.sendto(message.encode(), server_address)
        
        response, _ = client_socket.recvfrom(1024)
        return response.decode()

st.title("Currency Converter")
from_currency = st.selectbox("From Currency", CURRENCY_OPTIONS, index=0)
to_currency = st.selectbox("To Currency", CURRENCY_OPTIONS, index=1)
amount = st.number_input("Amount", min_value=1.0, value=1.0)

if st.button("Convert"):
    if from_currency == to_currency:
        st.warning("Please select two different currencies.")
    else:
        try:
            converted_amount = get_converted_amount_via_server(from_currency, to_currency, amount)
            st.success(f"{amount} {from_currency} = {converted_amount} {to_currency}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

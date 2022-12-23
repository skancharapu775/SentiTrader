import yfinance as yf

company_key_terms = {}

def collect_data():
    com = yf.Ticker("NFLX")
    return com

com = collect_data()

print(com.income_stmt)




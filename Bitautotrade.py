import time
import pyupbit
import datetime

access = "sNhKp4S4v3CeuPSIxYwFygBI7J1CAqkE6exQa5ql"
secret = "XZG67qmKVvEbVUZSHKM5GeC13jE7F0dJ0x8QgxEw"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

while True:
    try:
        now = datetime.datetime.now()
        start_time1 = get_start_time("KRW-BTC")
        end_time1 = start_time1 + datetime.timedelta(hours=6)
        start_time2 = start_time1 + datetime.timedelta(hours=6)
        end_time2 = start_time2 + datetime.timedelta(hours=6)
        start_time3 = start_time2 + datetime.timedelta(hours=6)
        end_time3 = start_time3 + datetime.timedelta(hours=6)
        start_time4 = start_time3 + datetime.timedelta(hours=6)
        end_time4 = start_time4 + datetime.timedelta(hours=6)

        if start_time1 < now < end_time1 - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.3)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*1)
        time.sleep(1)

        if start_time2 < now < end_time2 - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.3)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*1)
        time.sleep(1)
        
        if start_time3 < now < end_time3 - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.3)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*1)
        time.sleep(1)

        if start_time4 < now < end_time4 - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-BTC", 0.3)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*1)
        time.sleep(1)
        
    except Exception as e:
        print(e)
        time.sleep(1)
import requests
import time

URL_ROOT = 'http://localhost:8000/transactions'


# connection = client.connect("192.168.99.100:4200", username="crate")
# c = connection.cursor()


def test_add():

    data = [
    {
        "command": "ADD",
        "transactionNum": 1,
        "userId": "oY01WVirLr",
        "amount": 63511.53
    }
        ]

    r = requests.post(URL_ROOT + '/add', json=data)
    print (r)
    # time.sleep(2)

    # connection = client.connect("localhost:4200", username="crate")
    # c = connection.cursor()
    # c.execute('SELECT * FROM USERS;')
    # print (c.fetchall())


def test_buy():
    data = [
    {
        "command": "BUY",
        "transactionNum": 3,
        "userId": "oY01WVirLr",
        "symbol": "S",
        "amount": 276.83
    }
        ]

    r = requests.post(URL_ROOT + '/buy', json=data)
    print (r)

def test_commit_buy():
    data = [
    {
        "command": "COMMIT_BUY",
        "transactionNum": 4,
        "userId": "oY01WVirLr "
    }
        ]

    r = requests.post(URL_ROOT + '/commit_buy', json=data)

def test_cancel_buy():
    data = [
    {
        "command": "CANCEL_BUY",
        "transactionNum": 19,
        "userId": "oY01WVirLr "
    }
        ]

    r = requests.post(URL_ROOT + '/cancel_buy', json=data)


def test_sell():
    data = [
    {
        "command": "SELL",
        "transactionNum": 31,
        "userId": "oY01WVirLr",
        "symbol": "S",
        "amount": 641.9
    }
        ]

    r = requests.post(URL_ROOT + '/sell', json=data)


def test_commit_sell():
    data = [
    {
        "command": "COMMIT_SELL",
        "transactionNum": 32,
        "userId": "oY01WVirLr "
    }
        ]

    r = requests.post(URL_ROOT + '/commit_sell', json=data)

def test_cancel_sell():
    data = [
    {
        "command": "CANCEL_SELL",
        "transactionNum": 28,
        "userId": "oY01WVirLr "
    }
        ]

    r = requests.post(URL_ROOT + '/cancel_sell', json=data)


def test_set_buy_amount():
    data = [
    {
        'userID': '69',
        'amount': 200,
        'symbol': 'abc'
    }
        ]

    r = requests.post(URL_ROOT + '/set_buy_amount', json=data)


def test_set_sell_amount():
    data = [
    {
        "command": "SET_BUY_AMOUNT",
        "transactionNum": 30,
        "userId": "oY01WVirLr",
        "symbol": "S",
        "amount": 658.38
    }
        ]

    r = requests.post(URL_ROOT + '/set_sell_amount', json=data)


def test_cancel_set_buy():
    data = [
    {
        "command": "CANCEL_SET_BUY",
        "transactionNum": 20,
        "userId": "oY01WVirLr",
        "symbol": "S "
    }
        ]

    r = requests.post(URL_ROOT + '/cancel_set_buy', json=data)


def test_set_buy_trigger():
    data = [
    {
        "command": "SET_BUY_TRIGGER",
        "transactionNum": 61,
        "userId": "oY01WVirLr",
        "symbol": "S",
        "price": "59.23 "
    }
        ]

    r = requests.post(URL_ROOT + '/set_buy_trigger', json=data)


def test_set_sell_trigger():
    data = [
    {
        "command": "SET_SELL_TRIGGER",
        "transactionNum": 50,
        "userId": "oY01WVirLr",
        "symbol": "S",
        "price": "59.23 "
    }
        ]

    r = requests.post(URL_ROOT + '/set_sell_trigger', json=data)


def test_cancel_set_sell():
    data = [
    {
        "command": "CANCEL_SET_SELL",
        "transactionNum": 95,
        "userId": "oY01WVirLr",
        "symbol": "S "
    }
        ]

    r = requests.post(URL_ROOT + '/cancel_set_sell', json=data)




def test_system_dumplog():
    data = [
    {
        "command": "DUMPLOG",
        "transactionNum": 100,
        "filename": "./testLOG"
    }
        ]

    r = requests.post(URL_ROOT + '/dumplog', json=data)


def test_display_summary():
    data = [
    {
        "command": "DISPLAY_SUMMARY",
        "transactionNum": 58,
        "userId": "oY01WVirLr "
    }
        ]

    r = requests.post(URL_ROOT + '/display_summary', json=data)


def test_quote_handler():
    data = [
    {
        "command": "QUOTE",
        "transactionNum": 7,
        "userId": "oY01WVirLr",
        "symbol": "S "
    }
        ]
    r = requests.post(URL_ROOT + '/quote', json=data)


if __name__ == '__main__':

    test_add()
    # test_buy()
    # test_commit_buy()
    # test_sell()
    # test_commit_sell()
    # test_cancel_sell()
    # test_cancel_buy()
    # test_set_buy_amount()
    # test_set_sell_amount()
    # test_cancel_set_buy()
    # test_set_buy_trigger()
    # test_set_sell_trigger()
    # test_cancel_set_sell()
    # test_system_dumplog()
    # test_quote_handler()
    # test_quote_handler()

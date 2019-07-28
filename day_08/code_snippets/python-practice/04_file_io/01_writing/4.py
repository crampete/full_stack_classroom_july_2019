# sample CSV
headers = ['open', 'low', 'high', 'close']

data = [
    {'open': 800, 'low': 750, 'high': 820, 'close': 770},
    {'open': 790, 'low': 760, 'high': 830, 'close': 830},
    {'open': 820, 'low':  800, 'high': 860, 'close': 850},
    {'open': 840, 'low': 810, 'high': 848, 'close': 820}
]

with open('4.stocks_tick.csv', 'w') as fp:
    fp.write(",".join(headers))

    for point in data:
        fp.write('\n')
        fp.write(
            f"{point['open']},{point['low']},{point['high']},{point['close']}")
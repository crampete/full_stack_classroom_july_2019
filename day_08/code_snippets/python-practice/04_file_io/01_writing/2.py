# bill entry 4-5 lines each entry
bills = [
    {
        "name": "Linus",
        "amount": "$400",
        "cart": "Laptop, Books",
        "date": "23rd December 2017"
    },

    {
        "name": "Arijit",
        "amount": "$100",
        "cart": "Microphones, Towel",
        "date": "24th December 2017"
    },

    {

        "name": "Tracy Chapman",
        "amount": "$150",
        "cart": "Watermelons, Wires",
        "date": "2nd January 2018"

    },
]

fp = open("2.bill_entries.txt", 'w')

for indi_bill in bills:
    formatted_string = f"{indi_bill['name']}\n{indi_bill['amount']}\n{indi_bill['cart']}\n{indi_bill['date']}"

    fp.write(formatted_string)


fp.close()

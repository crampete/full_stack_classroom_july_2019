from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)


def csv_to_list(company_name):
    # better to use os.path.join
    # but this is simpler
    fp = open("data/" + company_name.upper() + ".csv", 'r')

    csv_reader = csv.reader(fp, delimiter=',')

    data_list = []

    # for the sake of simplicity
    # I'm not taking headers to be separate
    for row in csv_reader:
        data_list.append(row)

    return data_list


@app.route('/data/html/<company_name>')
def display(company_name):
    data_list = csv_to_list(company_name)

    return render_template('display.html', company=company_name.upper(), result=data_list)


@app.route('/data/json/<company_name>')
def dataJson(company_name):
    return jsonify(csv_to_list(company_name))


app.run(debug=True)

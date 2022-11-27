from datetime import timedelta
import flask
import psycopg2
import os
from flask import Flask, jsonify, request, session

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='rishik')
    return conn

@app.route('/', methods=['GET'])
def index():
    return "Landing Page for Altana APIs"

#All operators associated with a given company
@app.route("/api/operators",methods=['GET'])
def api_filter():
    app.permanent_session_lifetime = timedelta(minutes=1)
    query_parameters = request.args
    company = query_parameters.get('company')
    to_filter = []
    query = 'SELECT distinct nm_socio FROM "altana-db" WHERE'
    if company:
        query += 'nm_fantasia=? '
        to_filter.append(company)
    conn = get_db_connection()
    cur = conn.cursor()
    query = query[:-4] + ';'
    print(query)
    cur.execute(query, to_filter)
    ret = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(ret)

#All companies associated with a given operator
@app.route("/api/companies",methods=['GET'])
def api_operator():
    app.permanent_session_lifetime = timedelta(minutes=1)
    query_parameters = request.args
    company = query_parameters.get('operator')
    to_filter = []
    query = 'SELECT distinct nm_fantasia FROM "altana-db" WHERE'
    if company:
        query += 'nm_socio=? '
        to_filter.append(company)
    conn = get_db_connection()
    cur = conn.cursor()
    query = query[:-4] + ';'
    print(query)
    cur.execute(query, to_filter)
    ret = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(ret)

#All companies connected to a given company via shared operators
@app.route("/api/connected-companies",methods=['GET'])
def api_connected():
    app.permanent_session_lifetime = timedelta(minutes=1)
    query_parameters = request.args
    company = query_parameters.get('company')
    to_filter = []
    query = 'SELECT distinct nm_fantasia FROM "altana-db" WHERE nm_socio IN (SELECT nm_socio FROM "altana-db" WHERE '
    if company:
        query += 'nm_fantasia=? '
        to_filter.append(company)
    conn = get_db_connection()
    cur = conn.cursor()
    company=company[1:]
    company=company[:-1]
    query = query[:-2] + "'" + company + "'" + ');'
    print(company)
    print(query)
    cur.execute(query)
    ret = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(ret)

app.run()


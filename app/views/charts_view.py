from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.transactions_model import Transaction
from app.models.coins_historical_quotes_model import CoinsHistorical
from app.services.transaction_service import get_transations
from http import HTTPStatus
import datetime

import ipdb

charts = Blueprint("charts", __name__, url_prefix="/api")


@charts.route("/chart", methods=["GET"])
@jwt_required()
def data_graphic():
    user_id = get_jwt_identity()

    transactions = (
        Transaction.query.filter_by(user_id=user_id)
        .order_by(Transaction.date.asc())
        .all()

    )

    today = datetime.datetime.today()
    current_month = today.month
    month_list = ['jan', 'fev', 'mar', 'abr', 'mai',
                  'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dec']

    transactions_list = get_transations(transactions)

    coins_list = [coin['coin'] for coin in transactions_list]
    coins_set = set(coins_list)
    user_coins = list(coins_set)

    quantity = dict()

    for coin in user_coins:

        coin_transactions = [
            transaction for transaction in transactions_list if transaction['coin'] == coin]

        jan = [
            transaction for transaction in coin_transactions if transaction['date'].month == 1]
        fev = [
            transaction for transaction in coin_transactions if transaction['date'].month == 2]
        mar = [
            transaction for transaction in coin_transactions if transaction['date'].month == 3]
        abr = [
            transaction for transaction in coin_transactions if transaction['date'].month == 4]
        mai = [
            transaction for transaction in coin_transactions if transaction['date'].month == 5]
        jun = [
            transaction for transaction in coin_transactions if transaction['date'].month == 6]
        jul = [
            transaction for transaction in coin_transactions if transaction['date'].month == 7]
        ago = [
            transaction for transaction in coin_transactions if transaction['date'].month == 8]
        sep = [
            transaction for transaction in coin_transactions if transaction['date'].month == 9]
        oct = [
            transaction for transaction in coin_transactions if transaction['date'].month == 10]
        nov = [
            transaction for transaction in coin_transactions if transaction['date'].month == 11]
        dec = [
            transaction for transaction in coin_transactions if transaction['date'].month == 12]

        qty_list = [
            jan[-1]['net_quantity'] if jan else 0,
            fev[-1]['net_quantity'] if fev else 0,
            mar[-1]['net_quantity'] if mar else 0,
            abr[-1]['net_quantity'] if abr else 0,
            mai[-1]['net_quantity'] if mai else 0,
            jun[-1]['net_quantity'] if jun else 0,
            jul[-1]['net_quantity'] if jul else 0,
            ago[-1]['net_quantity'] if ago else 0,
            sep[-1]['net_quantity'] if sep else 0,
            oct[-1]['net_quantity'] if oct else 0,
            nov[-1]['net_quantity'] if nov else 0,
            dec[-1]['net_quantity'] if dec else 0
        ]

        start = 0
        for n in qty_list:
            if n != 0:
                start = qty_list.index(n)
                break

        i = start
        while i < len(qty_list):
            if qty_list[i] == 0:
                qty_list[i] = qty_list[i-1]
            i += 1

        qty_to_date = qty_list[:current_month]
        month_to_date = month_list[:current_month]
        qty_per_month = list(zip(month_to_date, qty_to_date))

        quantity[coin] = qty_per_month

    ###
    historical_price = dict()

    for coin in user_coins:
        historical = CoinsHistorical.query.filter_by(
            coin=coin).order_by(CoinsHistorical.date.asc()).all()
        historical_list = list()
        for price in historical:
            historical_list.append(price.price)
        historical_price[coin] = historical_list

        ipdb.set_trace()

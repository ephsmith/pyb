from flask import Flask, jsonify, abort, request, make_response
import json

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    return [quote for quote in quotes if quote['id'] == qid][0]


def _quote_exists(qid=None, quote=None):
    """Recommended helper"""
    if qid:
        return any(map(lambda x: x['id'] == qid, quotes))
    elif quote:
        return any(map(lambda x: x['quote'] == quote['quote'], quotes))


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return make_response(jsonify({'quotes': quotes}))


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    if _quote_exists(qid=qid):
        return make_response(jsonify({'quotes': [_get_quote(qid)]}))
    else:
        return '', 404


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    next_id = max(quotes, key=lambda x: x['id'])['id'] + 1 if quotes else 1
    quote = json.loads(request.get_data())
    if _quote_exists(quote=quote):
        return '', 400

    if all([field in quote for field in ['quote', 'movie']]):
        quote.update({'id': next_id})
        quotes.append(quote)
        return make_response(jsonify({'quote': quote}), 201)
    else:
        return '', 400


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    new_quote = json.loads(request.get_data())
    if new_quote == {}:
        return '', 400
    if _quote_exists(qid=qid):
        quote = _get_quote(qid)
        quote.update(new_quote)
        return make_response(jsonify({'quote': quote}), 200)
    else:
        return '', 404


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if _quote_exists(qid=qid):
        quotes.remove(_get_quote(qid))
        return '', 204
    else:
        return '', 404

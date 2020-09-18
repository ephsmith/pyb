from flask import Flask, jsonify, abort, request, make_response
import json
import sys

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


def _quote_exists(existing_quote):
    """Recommended helper"""
    return any(map(lambda x: x['id'] == existing_quote, quotes))


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return make_response(jsonify({'quotes': quotes}))


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    if _quote_exists(qid):
        return make_response(jsonify({'quotes': [_get_quote(qid)]}))
    else:
        return '', 404


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    next_id = max(quotes, key=lambda x: x['id'])['id'] + 1
    quote = json.loads(request.get_data())
    print(quote, file=sys.stderr, flush=True)
    if all([field in quote for field in ['quote', 'movie']]):
        quotes.append(quote.update(('id', next_id)))
        return '', 201
    else:
        make_response('nope', 400)


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    if _quote_exists(qid):
        _get_quote(qid).update(json.loads(request.get_data()))
        return '', 200
    else:
        return '', 404


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    if _quote_exists(qid):
        quotes.remove(_get_quote(qid))
        return 204
    else:
        return '', 404

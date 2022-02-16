from flask import jsonify, request
from zlibrary_python.sync import srape_search_query

from .app import app

@app.route('/search')
def search():
    query = request.args.get('query')
    fuzzy = True if request.args.get('fuzzy') in ['true', 'True', 't', 'T', 1] else False
    
    if not query:
        return jsonify({'error': 'query is required'})
    
    out = srape_search_query(query, fuzzy)
    return jsonify(out)
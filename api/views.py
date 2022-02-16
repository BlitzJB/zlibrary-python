from flask import jsonify, request
from zlibrary_python.a_sync import srape_search_query
import asyncio

from .app import app

@app.route('/search')
def search():
    query = request.args.get('query')
    fuzzy = True if request.args.get('fuzzy') in ['true', 'True', 't', 'T', 1] else False
    
    if not query:
        return jsonify({'error': 'query is required'})
    
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(srape_search_query(query, fuzzy))
    loop.close()
    return jsonify(out)
#
# Copyright (c) 2025 Jess Yu
# Licensed under the MIT License.
# See LICENSE file in the project root for full license information.
#
from flask import Flask, render_template, request, redirect, url_for, make_response
import chromadb
import json

app = Flask(__name__)

def get_config_from_cookies():
    config = {
        "host": request.cookies.get('chroma_host', 'localhost'),
        "port": request.cookies.get('chroma_port', '8000'),
        "client_id": request.cookies.get('cf_id', ''),
        "client_secret": request.cookies.get('cf_secret', '')
    }
    return config


def get_client(config):
    cf_headers = {
        "CF-Access-Client-Id": config['client_id'],
        "CF-Access-Client-Secret": config['client_secret']
    }
    return chromadb.HttpClient(
        host=config['host'],
        port=int(config['port']),
        ssl=True,
        headers=cf_headers
    )


@app.route('/')
def index():
    config = get_config_from_cookies()
    if not config['client_secret']:
        return redirect(url_for('setup'))

    try:
        client = get_client(config)
        collections = client.list_collections()
        return render_template('index.html', collections=collections, config=config)
    except Exception as e:
        return f"連線失敗，請檢查設定：{str(e)} <br><a href='/setup'>返回設定</a>"


@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        host = request.form.get('host')
        port = request.form.get('port')
        cf_id = request.form.get('cf_id')
        cf_secret = request.form.get('cf_secret')

        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('chroma_host', host, max_age=30 * 24 * 60 * 60)
        resp.set_cookie('chroma_port', port, max_age=30 * 24 * 60 * 60)
        resp.set_cookie('cf_id', cf_id, max_age=30 * 24 * 60 * 60)
        resp.set_cookie('cf_secret', cf_secret, max_age=30 * 24 * 60 * 60)
        return resp

    return render_template('setup.html', config=get_config_from_cookies())


@app.route('/collection/<name>')
def view_collection(name):
    config = get_config_from_cookies()
    client = get_client(config)
    collection = client.get_collection(name=name)
    data = collection.get(limit=50)

    items = []
    for i in range(len(data['ids'])):
        items.append({
            "id": data['ids'][i],
            "document": data['documents'][i] if data['documents'] else "",
            "metadata": data['metadatas'][i] if data['metadatas'] else {}
        })
    return render_template('collection.html', name=name, items=items, count=collection.count())


if __name__ == '__main__':
    app.run(debug=False, port=5001)
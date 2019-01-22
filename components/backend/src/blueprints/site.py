from flask import (Blueprint, jsonify)


SITE = Blueprint('site', __name__)


_sites = [  # TODO remove once no longer needed
    {
        'id': '0',
        'slug': 'Fun Times',
        'default_page_id': None,
    },
    {
        'id': '1',
        'slug': 'Dino DNA',
        'default_page_id': None,
    },
]

_pages = [
    {
        'id': 0,
        'title': 'title1',
        'content': 'this is some content',
        'site_id': '0'
    },
    {
        'id': 1,
        'title': 'title2',
        'content': 'this is some content2',
        'site_id': '1'
    }
]


@SITE.route('/', methods=['GET'])
def list_sites():
    sites = _sites  # TODO retrieve from database
    return jsonify(sites)


@SITE.route('/<int:site_id>', methods=['GET'])
def get_site(site_id):
    site = _sites[site_id]  # TODO retrieve from database
    return jsonify(site)


@SITE.route('/<int:site_id>/pages/', methods=['GET'])
def list_pages(site_id):
    pages = _pages  # TODO retrieve from database
    return jsonify(pages)


@SITE.route('/<int:site_id>/pages/<int:page_id>', methods=['GET'])
def get_page(site_id, page_id):
    page = _pages[page_id]   # TODO retrieve from database
    return jsonify(page)

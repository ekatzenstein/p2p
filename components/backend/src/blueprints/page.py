"""Flask view functions for the page resource endpoint."""
from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from models import db, Page
from .schemas import PageSchema

PAGE = Blueprint('page', __name__)


@PAGE.route('/', methods=['GET'])
@marshal_with(PageSchema(many=True), 200)
def get_pages():
    return db.session.query(Page).all()


@PAGE.route('/', methods=['POST'])
@marshal_with(PageSchema(many=False), 200)
@use_kwargs(PageSchema(), locations=('json',))
def create_page(**kwargs):
    new_page = Page(title=kwargs.get('title'), content=kwargs.get('content'))
    db.session.add(new_page)
    db.session.commit()
    return new_page


@PAGE.route('/<int:page_id>', methods=['GET'])
@marshal_with(PageSchema(many=False), 200)
def get_page(page_id):
    page = db.session.query(Page).get(page_id)
    return page


@PAGE.route('/<int:page_id>', methods=['PUT'])
@marshal_with(PageSchema(many=False), 200)
@use_kwargs(PageSchema(only=('title', 'content')),
            locations=('json',))
def update_page(page_id, **kwargs):
    page = Page.query.get(page_id)
    page.update(kwargs)
    db.session.commit()
    return page


@PAGE.route('/<int:page_id>', methods=['DELETE'])
@marshal_with(None, 204, "Page deleted", apply=False)
def delete_page(page_id):
    page = db.session.query(Page).get(page_id)
    db.session.delete(page)
    db.session.commit()
    return '', 204, {'content-length': 0}
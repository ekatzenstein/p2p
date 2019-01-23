from flask import (Blueprint, jsonify)
from flask_apispec import use_kwargs, marshal_with, doc

from models import db, Site, Page
from .schemas import SiteSchema, PageSchema

SITE = Blueprint('site', __name__)


@SITE.route('/', methods=['GET'])
@marshal_with(SiteSchema(many=True), 200)
def get_sites():
    return Site.query.all()


@SITE.route('/<int:site_id>', methods=['GET'])
@marshal_with(SiteSchema(many=False), 200)
def get_site(site_id):
    return Site.query.get(site_id)


@SITE.route('/', methods=['POST'])
@use_kwargs(SiteSchema(), locations=('json',))
@marshal_with(SiteSchema(many=False), 200)
def create_site(name, slug, default_page_id=None):
    new_site = Site(name=name, slug=slug, default_page_id=default_page_id)
    db.session.add(new_site)
    db.session.commit()

    return new_site


@SITE.route('/<int:site_id>/pages/', methods=['GET'])
@marshal_with(PageSchema(many=True), 200)
def get_pages(site_id):
    site = db.session.query(Site).get(site_id)

    schema = PageSchema()
    data, errors = schema.dump(site.pages)
    if errors:
        raise Error('serialization_error', errors)
    response = jsonify(data)

    return response


@SITE.route('/<int:site_id>/pages/', methods=['POST'])
@marshal_with(PageSchema(many=False), 201)
@use_kwargs(PageSchema(), locations=('json',))
def create_page(site_id, **kwargs):
    site = db.session.query(Site).get(site_id)
    new_page = Page(title='a title', content='some content', site_id=site_id)
    site.pages.append(new_page)
    db.session.commit()

    return new_page.title


@SITE.route('/<int:site_id>/pages/<int:page_id>', methods=['GET'])
@marshal_with(PageSchema(many=False), 200)
def get_page(site_id, page_id):
    page = db.session.query(Page).get(page_id)
    return page

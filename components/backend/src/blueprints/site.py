"""Flask view functions for the site resource endpoint."""
from flask import Blueprint
from flask_apispec import use_kwargs, marshal_with

from models import db, Site, Page
from .schemas import SiteSchema, PageSchema

SITE = Blueprint('site', __name__)


@SITE.route('/', methods=['GET'])
@marshal_with(SiteSchema(many=True), 200)
def get_sites():
    return Site.query.all()


@SITE.route('/', methods=['POST'])
@use_kwargs(SiteSchema(), locations=('json',))
@marshal_with(SiteSchema(many=False), 200)
def create_site(name, slug, default_page_id=None):
    new_site = Site(name=name, slug=slug, default_page_id=default_page_id)
    db.session.add(new_site)
    db.session.commit()
    return new_site


@SITE.route('/<int:site_id>', methods=['GET'])
@marshal_with(SiteSchema(many=False), 200)
def get_site(site_id):
    return Site.query.get(site_id)


@SITE.route('/<int:site_id>', methods=['DELETE'])
@marshal_with(None, 204, "Site deleted", apply=False)
def delete_site(site_id):
    site = Site.query.get(site_id)
    for page in site.pages:
        db.session.delete(page)
    db.session.delete(site)
    db.session.commit()
    return '', 204, {'content-length': 0}


@SITE.route('/<int:site_id>/pages/', methods=['GET'])
@marshal_with(PageSchema(many=True), 200)
def get_pages(site_id):
    site = db.session.query(Site).get(site_id)
    return site.pages


@SITE.route('/<int:site_id>/pages/', methods=['POST'])
@marshal_with(PageSchema(many=False), 200)
@use_kwargs(PageSchema(), locations=('json',))
def create_page(site_id, **kwargs):
    site = db.session.query(Site).get(site_id)
    new_page = Page(title=kwargs.get('title'), content=kwargs.get('content'), site_id=site_id)
    site.pages.append(new_page)
    db.session.commit()
    return new_page


@SITE.route('/<int:site_id>/pages/<int:page_id>', methods=['GET'])
@marshal_with(PageSchema(many=False), 200)
def get_page(site_id, page_id):
    page = db.session.query(Page).get(page_id)
    return page


@SITE.route('/<int:site_id>/pages/<int:page_id>', methods=['DELETE'])
@marshal_with(None, 204, "Page deleted", apply=False)
def delete_page(site_id, page_id):
    page = db.session.query(Page).get(page_id)
    db.session.delete(page)
    db.session.commit()
    return '', 204, {'content-length': 0}
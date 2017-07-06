#!/usr/bin/python

from flask import Blueprint, render_template
from requests import get

ListContainers = Blueprint('ListContainers',__name__)

@ListContainers.route("/")
def index():
    rst = get("http://docker.dexter.com.br:5000/v2/_catalog?n=10")
    return render_template("/index.html",images=rst.json()['repositories'])

@ListContainers.route("/images/")
def images():
    rst = get("http://docker.dexter.com.br:5000/v2/_catalog")
    return render_template("/images.html", images=rst.json()['repositories'])

@ListContainers.route("/images/<id>")
def tags(id):
    rst = get("http://docker.dexter.com.br:5000/v2/{0}/tags/list".format(id))
    return render_template("/image.html", image=rst.json())
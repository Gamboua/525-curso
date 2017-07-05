#!/usr/bin/python

from flask import Blueprint, redirect
from requests import delete

RemoveContainers = Blueprint('RemoveContainers',__name__)

@RemoveContainers.route("/images/<id>/<tag>")
def removetag(id,tag):
    try:
        rst = delete("http://docker.dexter.com.br:5000/v2/{0}/manifest/{1}".format(id,tag))
        print rst.status_code
    except Exception as e:
        print e.message
    finally:
        return redirect("/images/"+id)
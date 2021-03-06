import argparse
import os
import sys
import json
import requests
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from urllib.parse import (
    parse_qs,
    urlencode,
)
from collections import OrderedDict
from pyramid.compat import bytes_
from pyramid.httpexceptions import HTTPBadRequest
import logging
import io
log = logging.getLogger(__name__)
@view_config(route_name='t2dkp', request_method='POST')
def t2dkp(context,request):
    region = request.params['region']
    log.warn(region)
    limit = 'all'
    genome = 'GRCh37'
    HEADERS = {'accept': 'application/json'}
    URL = 'http://t2depigenome-test.org/peak_metadata/region='
    r1 = requests.get(URL + region +'&genome=' + genome + '&limit=' + limit +'/peak_metadata.json', headers=HEADERS)
    json_doc = r1.json()
    json_doc = json.dumps(json_doc, indent=4, separators=(',', ': '))
    return Response(content_type='text/plain',body=json_doc)
if __name__ == '__main__':
    config = Configurator()
    config.add_route('t2dkp', '/t2dkp')
    config.add_view(t2dkp, route_name='t2dkp')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

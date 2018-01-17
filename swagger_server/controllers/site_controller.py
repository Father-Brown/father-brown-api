import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.site import Site
from swagger_server.models.site_list import SiteList
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_url(url):
    """
    Add a new url site
    
    :param url: URL of site
    :type url: str

    :rtype: Site
    """
    return 'do some magic!'


def all_sites_get():
    """
    List of all sites
    Return a list of sites.

    :rtype: SiteList
    """
    return 'do some magic!'

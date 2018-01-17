import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.news_list import NewsList
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def news_to_be_published_get():
    """
    List of news to be published
    Return a list of news.

    :rtype: NewsList
    """
    return 'do some magic!'

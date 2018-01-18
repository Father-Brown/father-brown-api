import connexion
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.news import News
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


def verify_news(url):
    """
    Send a news to be classify
    Send a news to be classify
    :param url: URL of site
    :type url: str

    :rtype: News
    """
    return 'do some magic!'

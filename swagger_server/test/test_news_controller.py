# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.api_response import ApiResponse
from swagger_server.models.news import News
from swagger_server.models.news_list import NewsList
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestNewsController(BaseTestCase):
    """ NewsController integration test stubs """

    def test_news_to_be_published_get(self):
        """
        Test case for news_to_be_published_get

        List of news to be published
        """
        response = self.client.open('/v1/newsToBePublished',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_verify_news(self):
        """
        Test case for verify_news

        Send a news to be classify
        """
        response = self.client.open('/v1/verifyNews/{url}'.format(url='url_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

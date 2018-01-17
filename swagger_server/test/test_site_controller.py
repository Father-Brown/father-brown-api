# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.api_response import ApiResponse
from swagger_server.models.site import Site
from swagger_server.models.site_list import SiteList
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestSiteController(BaseTestCase):
    """ SiteController integration test stubs """

    def test_add_url(self):
        """
        Test case for add_url

        Add a new url site
        """
        response = self.client.open('/v1/site/{url}'.format(url='url_example'),
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_all_sites_get(self):
        """
        Test case for all_sites_get

        List of all sites
        """
        response = self.client.open('/v1/allSites',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

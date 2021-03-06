#!/usr/bin/env python
# coding=utf-8

import unittest

from main import application


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_users_page(self):
        response = self.app.get('/users', follow_redirects=True)
        self.assertEqual(response.status_code, 300)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()

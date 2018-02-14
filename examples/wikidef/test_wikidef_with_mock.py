#!/usr/bin/env python

"""
example of the unittest mock module
"""

import unittest
from unittest.mock import patch

from api import Wikipedia, MissingArticleError
from definitions import Definitions


class WikiDefTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_article_success(self):
    #     article = Definitions.article("Robot")
    #     self.assertIn("mechanical", article)

    # def test_missing_article_failure(self):
    #     missing_article_title = "!!!!!-NonExistentArticle"
    #     self.assertRaises(MissingArticleError, Definitions.article, missing_article_title)

    # # patch with a decorator
    # @patch('definitions.Wikipedia.get_article')
    # def test_article_success_decorator_mocked(self, mock_method):
    #     article = Definitions.article("Robot")
    #     mock_method.assert_called_once_with("Robot")

    @patch.object(Wikipedia, 'get_article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")
        mock_method.assert_called_once_with("Robot")

    # # patch with a context manager
    # def test_article_success_context_manager_mocked(self):
    #     with patch.object(Wikipedia, 'get_article') as mock_method:
    #         article = Definitions.article("Robot")
    #         mock_method.assert_called_once_with("Robot")

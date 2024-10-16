from unittest import TestCase

import requests

from deploy.transform_content.Cbr_Content__Transform_Into_Static import Cbr_Content__Transform_Into_Static
from osbot_utils.utils.Dev import pprint


class test_Cbr_Content__Transform_Into_Static(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cbr_content_into_static = Cbr_Content__Transform_Into_Static()

    def test_convert_all_md_files(self):
        with self.cbr_content_into_static as _:
            _.convert_all_md_files()

    def test_md_file__to__json(self):
        with self.cbr_content_into_static as _:
            md_file = "en/web-site/home-page/card-1.md"
            _.md_file__to__json(md_file)

    def test_md_files(self):
        with self.cbr_content_into_static as _:
            md_files = _.md_files()
            assert len(md_files) > 0

    def test_toml_files(self):
        with self.cbr_content_into_static as _:
            toml_files = _.toml_files()
            assert len(toml_files) > 0

    def test_toml_file__to__json(self):
        with self.cbr_content_into_static as _:
            md_file = "en/web-site/side-menu/config.toml"
            _.toml_file__to__json(md_file)
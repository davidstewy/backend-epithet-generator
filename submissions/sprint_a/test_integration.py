import pytest
import json
from .app import app
from flask_testing import TestCase

json_path = '../../resources/data.json'


class BaseTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        return app


class TestFileManager(BaseTest):

    def test_root_path(self):
        response = self.client.get("/")
        data = response.data
        assert len(data.split()) == 4

    def test_quantity_path(self):
        response = self.client.get('/epithets/5')
        data = json.loads(response.data)
        assert len(data) == 5

    def test_vocab_path(self):
        response = self.client.get("/vocabulary")
        data = json.loads(response.data)
        assert 'Column 1' in data
        assert 'Column 2' in data
        assert 'Column 3' in data

    def test_nemesis_path(self):
        response = self.client.get("/unleash_nemesis_rant")
        data = json.loads(response.data)
        assert data != 0
        assert len(data[-1].split()) % 4 == 0

from sprint_a.helpers import FileManager, Vocabulary, EpithetGenerator
import pytest
from .app import app

json_path = '../../resources/data.json'


def test_get_extension():
    assert FileManager.get_extension(json_path) == 'json'
    assert FileManager.get_extension('resourdes/data.txt') == 'txt'


def test_read_json():
    assert 'Column 1' in FileManager.read_json(json_path)
    assert 'Column 3' in FileManager.read_json(json_path)


def test_from_file():
    assert 'Column 1' in Vocabulary.from_file(json_path, fields=False).keys()
    assert 'Column 2' in Vocabulary.from_file(json_path, fields=False).keys()


def test_create_insult():
    assert len(EpithetGenerator.create_insult(json_path).split()) == 4


def test_all_vocab():
    assert len(list(EpithetGenerator.all_vocab(json_path).keys())) == 3

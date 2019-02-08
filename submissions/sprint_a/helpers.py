import os
import json
import random


class FileManager:
    """Handle local file system IO."""

    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        """Opens and reads data from path, returns json"""
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)


class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        """Finds the extension of a file then runs the appropriate
        class method based on that extension"""
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        """Stores json data passed to it and returns data if fields=False,
        if True it will return a tuple of data and data's keys"""
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        """Runs a class method based on the extension passed"""
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator:
    def create_insult(path):
        """Pulls one random word from each Column/Key and formats
        them into a phrase/string"""
        my_dict = Vocabulary.from_file(path, fields=False)
        my_phrase = '{} {} {}'.format(random.choice(my_dict["Column 1"]),
                                      random.choice(my_dict["Column 2"]),
                                      random.choice(my_dict["Column 3"]))
        return my_phrase

    def all_vocab(path):
        """Returns json data from path"""
        my_dict = Vocabulary.from_file(path, fields=False)
        return my_dict

from __future__ import absolute_import, print_function
from contemplate.parser import Parser, ParserException
import yaml


class YAMLParser(Parser):

    def __init__(self, source):
        self.source = source

    def data(self):
        try:
            with open(self.source, 'r') as fd:
                return yaml.load(fd)
        except yaml.error.YAMLError as err:
            raise ParserException(err)

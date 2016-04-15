from __future__ import absolute_import, print_function
import argparse
import re
from .types import yes_no


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        raise argparse.ArgumentError(None, message)


class Prompt(object):

    def __init__(self, type=None, choices=None, default=None):
        self.type = type
        self.choices = list(choices) if choices is not None else None
        self.default = default
        self.parser = ArgumentParser()
        self.parser.add_argument('answer', type=type,
                                 choices=choices, default=default,
                                 nargs=('?' if default is not None else None))

    @staticmethod
    def input(prompt):
        result = raw_input(prompt)
        if result == '':
            return []
        return [result]

    def build_prompt(self, message):
        suffix = []

        if self.choices is not None:
            suffix.append('choices: {0}'
                          .format(', '.join(['"{0}"'.format(choice)
                                             for choice in self.choices])))

        if self.type is not None:
            suffix.append('type: "{0}"'.format(self.type.__name__))

        if self.default is not None:
            suffix.append('default: "{0}"'.format(self.default))

        return (message +
                (' ({0})'.format(', '.join(suffix)) if len(suffix) else '') +
                ' ')

    def prompt(self, message):
        message = self.build_prompt(message)
        while True:
            try:
                return self.parser.parse_args(self.input(message)).answer
            except argparse.ArgumentError as exc:
                print(exc)


class MultiPrompt(object):

    def __init__(self, eof='.'):
        self.eof = eof

    @staticmethod
    def input():
        return raw_input()

    def prompt(self, message):
        message += ' (finish with "{0}")'.format(self.eof)
        print(message)
        return '\n'.join(iter(self.input, self.eof))

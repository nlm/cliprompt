import argparse
import re

class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        raise

def yes_no(value):
    if re.match(r'^[Yy]([Ee][Ss])?$', value):
        return True
    elif re.match('^[Nn]([Oo])?$', value):
        return False
    else:
        raise ValueError

class Prompt(object):

    def __init__(self, type=None, choices=None, default=None):
        self.type = type
        choices = list(choices) if choices is not None else None
        self.choices = choices
        self.default = default
        if (self.default is not None and
            self.choices is not None):
            self.choices.append('')
        self.parser = ArgumentParser()
        self.parser.add_argument('answer', type=type, choices=choices)

    @staticmethod
    def input(prompt):
        result = raw_input(prompt)
        if result == '':
            return None
        return result

    def build_prompt(self, message):
        if self.choices:
            message += ' ({})'.format(', '.join(["'{}'".format(choice)
                                                 for choice in self.choices]))
        if self.type:
            message += ' ({})'.format('type: {}'.format(self.type.__name__))
        return message + ' '

    def prompt(self, message):
        message = self.build_prompt(message)
        while True:
            try:
                result = self.parser.parse_args([self.input(message)])
                if result.answer == '' and self.default is not None:
                    return self.default
                return result.answer
            except argparse.ArgumentError as exc:
                print(exc)

    def prompt_multiline(self, message, eof='.'):
        message += ' (finish with "{}")'.format(eof)
        print(message)
        return '\n'.join(iter(self._input, eof))

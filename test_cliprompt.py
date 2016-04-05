from __future__ import print_function
from unittest import TestCase
from cliprompt import Prompt, ArgumentParser, yes_no

class FakePrompt(Prompt):

    def __init__(self, fakeinputs, *args, **kwargs):
        super(FakePrompt, self).__init__(*args, **kwargs)
        self.fakeinputs = list(fakeinputs)

    def input(self, message):
        return self.fakeinputs.pop(0)


class TestBase(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['ok'])

    def test_base(self):
        self.prompt.prompt('ok ?')


class TestChoices(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['ok'], choices=['ok', 'ko'])

    def test_choices(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, 'ok')


class TestChoicesMismatch(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['', 'wtf', 'ok', 'bla', 'ko'],
                                 choices=['ok', 'ko'])

    def test_choices(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestChoicesNone(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['', 'wtf', 'bla'],
                                 choices=['ok', 'ko'])

    def test_choices(self):
        self.assertRaises(IndexError, self.prompt.prompt, 'ok or ko ?')


class TestTypeYesNo(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['', 'wtf', 'Nooo', 'Nono', 'yeS', 'no'],
                                 type=yes_no)

    def test_typeyesno(self):
        result = self.prompt.prompt('yes or no ?')
        self.assertEqual(result, True)


class TestTypeInt(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['', 'wtf', 'No', '99'],
                                 type=int)

    def test_typeint(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, 99)


class TestDefault(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([''], default='ok')

    def test_default(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestDefaultChoices(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([''], default='other', choices=('ok', 'ko'))

    def test_choices(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'other')



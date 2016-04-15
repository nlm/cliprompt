from __future__ import print_function
from unittest import TestCase
from cliprompt import Prompt, ArgumentParser, yes_no

class FakePrompt(Prompt):

    def __init__(self, fakeinputs, *args, **kwargs):
        super(FakePrompt, self).__init__(*args, **kwargs)
        self.fakeinputs = list(fakeinputs)

    def input(self, message):
        value = self.fakeinputs.pop(0)
        if value is None:
            return []
        else:
            return [value]


class TestBase(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['ok'])

    def test_base(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, 'ok')


class TestChoices(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['ok'], choices=['ok', 'ko'])

    def test_choices(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, 'ok')


class TestChoicesMulti(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None, 'wtf', 'ok', 'bla', 'ko'],
                                 choices=['ok', 'ko'])

    def test_choices(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestChoicesMultiNoMatch(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None, 'wtf', 'bla', 'meh'],
                                 choices=['ok', 'ko'])

    def test_choices(self):
        self.assertRaises(IndexError, self.prompt.prompt, 'ok or ko ?')


class TestChoicesMultiNoMatchDefault(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['wtf', 'blah', 'meh', None],
                                 choices=('ok', 'ko'),
                                 default='ok')

    def test_choices(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestChoicesDefaultMismatch(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['wtf', 'blah', None],
                                 choices=('ok', 'ko'),
                                 default='somethingincorrect')

    def test_choices(self):
        self.assertRaises(IndexError, self.prompt.prompt, 'ok or ko ?')


class TestTypeYesNo(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None, 'wtf', 'Nooo', 'Nono', 'yeS', 'no'],
                                 type=yes_no)

    def test_typeyesno(self):
        result = self.prompt.prompt('yes or no ?')
        self.assertEqual(result, True)


class TestTypeInt(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None, 'wtf', 'No', '99', '100'],
                                 type=int)

    def test_typeint(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, 99)


class TestNullString(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([''])

    def test_typeint(self):
        result = self.prompt.prompt('ok ?')
        self.assertEqual(result, '')


class TestEmpty(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None])

    def test_typeint(self):
        self.assertRaises(IndexError, self.prompt.prompt, 'ok ?')


class TestNotDefault(TestCase):

    def setUp(self):
        self.prompt = FakePrompt(['ok'], default='ko')

    def test_default(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestEmptyDefault(TestCase):

    def setUp(self):
        self.prompt = FakePrompt([None], default='ok')

    def test_default(self):
        result = self.prompt.prompt('ok or ko ?')
        self.assertEqual(result, 'ok')


class TestBuildPrompt(TestCase):

    def setUp(self):
        self.prompt = Prompt()

    def test_prompt(self):
        self.assertEqual(self.prompt.build_prompt('ok'), 'ok ')


class TestBuildPromptDefault(TestCase):

    def setUp(self):
        self.prompt = Prompt(default='yes')

    def test_prompt(self):
        self.assertEqual(self.prompt.build_prompt('ok'), 'ok (default: "yes") ')


class TestBuildPromptDefault(TestCase):

    def setUp(self):
        self.prompt = Prompt(choices=('yes', 'no'))

    def test_prompt(self):
        self.assertEqual(self.prompt.build_prompt('ok'), 'ok (choices: "yes", "no") ')


class TestBuildPromptType(TestCase):

    def setUp(self):
        self.prompt = Prompt(type=int)

    def test_prompt(self):
        self.assertEqual(self.prompt.build_prompt('ok'), 'ok (type: "int") ')

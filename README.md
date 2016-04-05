cliprompt
=========

This tool helps you ask questions via CLI

Prompt is a single-line prompt and will loop until a correct answer
is detected. It is based on argparse, so arguments "choices", "type",
and "default" work the same way

MultiPrompt is a multi-line prompt. It will acquire lines until a line
with only the EOF string is reached. This defaults to '.'

Examples:

    >>> from cliprompt import Prompt
    >>> prompt = Prompt(choices=['blue', 'red', 'yellow'])
    >>> result = prompt.prompt('what color do you prefer ?')
    >>> print('your favorite color is {}'.format(result))

    what color do you prefer ? ('blue', 'red', 'yellow') green
    argument answer: invalid choice: 'green' (choose from 'blue', 'red', 'yellow')
    what color do you prefer ? ('blue', 'red', 'yellow') blue
    your favorite color is blue


    >>> from cliprompt import MultiPrompt
    >>> prompt = MultiPrompt()
    >>> result = prompt.prompt('enter text:')
    >>> print('***')
    >>> print(result)
    >>> print('***')

    enter text: (finish with ".")
    hello world
    this is a test
    .
    ***
    hello world
    this is a test
    ***

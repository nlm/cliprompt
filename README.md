cliprompt
=========

This tool helps you ask questions via CLI

Example:

    >>> from cliprompt import Prompt, yes_no
    >>> prompt = Prompt(choices=['blue', 'red', 'yellow'])
    >>> result = prompt.prompt('what color do you prefer ?')
    >>> print("your favorite color is {}".format(result))

    what color do you prefer ? ('blue', 'red', 'yellow') green
    argument answer: invalid choice: 'green' (choose from 'blue', 'red', 'yellow')
    what color do you prefer ? ('blue', 'red', 'yellow') blue
    your favorite color is blue

from setuptools import setup,find_packages

setup(
    name = "cliprompt",
    version = "0.1",
    packages = ['cliprompt'],
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "a simple cli prompt based on argparse",
    license = "GPL",
    keywords = "cli prompt",
    url = "https://github.com/nlm/netgen",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite = 'test_cliprompt',
)

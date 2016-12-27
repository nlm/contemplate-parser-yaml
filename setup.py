from setuptools import setup,find_packages

setup(
    name = "contemplate-parser-yaml",
    version = "0.1",
    packages = find_packages(),
    author = "Nicolas Limage",
    author_email = 'github@xephon.org',
    description = "multi templating engines command-line interface",
    license = "MIT",
    keywords = "content template command-line",
    url = "https://github.com/nlm/contemplate-engine-jinja2",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = [
        'pyyaml'
    ],
    entry_points = {
        'contemplate_parser_v1': [
            'yaml = contemplate_parser_yaml:YAMLParser',
        ],
    },
)

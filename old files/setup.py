#!/usr/bin/env python
# coding=utf-8

"""
python distribute file
"""

from setuptools import setup, find_namespace_packages


setup(
    name="cyber-sentinels-helper-app",
    version="0.1.0",
    description='Command bot that do operations with storing contacts and notes.',
    url='https://github.com/SiracencoSerghei/cyber-sentinels-helper-app',
    author='Cyber Sentinels',
    author_email='siracencoserghei@gmail.com',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    license='MIT',
    long_description=open('README.md', "r", encoding="utf-8").read(),
    packages=find_namespace_packages(),
    data_files=[("cyber-sentinels-helper-app", ["cyber-sentinels-helper-app/outputs/address_book.json",
                                                "cyber-sentinels-helper-app/outputs/notes.json",
                                                "cyber-sentinels-helper-app/outputs/todo.json"])],
    include_package_data=True,
    install_requires=['rich', 'prompt_toolkit'],
    entry_points={'console_scripts': ['cyber-sentinels = __main__:run']}
)
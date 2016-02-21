# -*- coding: utf-8 -*-
from __future__ import print_function

from _pytest.assertion.rewrite import rewrite_asserts
from _pytest.monkeypatch import monkeypatch

import codegen


def pytest_addoption(parser):
    group = parser.getgroup('ast-back-to-python')
    group.addoption(
        '--show-ast-as-python',
        action='store_true',
        dest='ast_as_python',
        default=False,
        help='Show how assertion rewriting recoded the AST.'
    )

def pytest_configure(config):
    config._ast_as_python = AstAsPython()
    config.pluginmanager.register(config._ast_as_python)

def make_replacement_rewrite_asserts(store):
    def replacement_rewrite_asserts(tree):
        rewrite_asserts(tree)
        store.append(codegen.to_source(tree))
    return replacement_rewrite_asserts

class AstAsPython(object):
    def __init__(self):
        self.store = []

    def pytest_configure(self, config):
        if not config.getoption('ast_as_python'):
            return

        mp = monkeypatch()
        mp.setattr(
            '_pytest.assertion.rewrite.rewrite_asserts',
            make_replacement_rewrite_asserts(self.store))

        # written pyc files will bypass our patch, so disable reading them
        mp.setattr(
            '_pytest.assertion.rewrite._read_pyc',
            lambda source, pyc, trace=None: None)

        config._cleanup.append(mp.undo)

    def pytest_terminal_summary(self, terminalreporter):
        if not terminalreporter.config.getoption('ast_as_python'):
            return

        for source in self.store:
            terminalreporter._tw.sep("=", "Ast as Python")
            terminalreporter.write(source)

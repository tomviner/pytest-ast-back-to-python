pytest-ast-back-to-python
=========================

.. image:: https://travis-ci.org/tomviner/pytest-ast-back-to-python.svg?branch=master
    :target: https://travis-ci.org/tomviner/pytest-ast-back-to-python
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/tomviner/pytest-ast-back-to-python?branch=master
    :target: https://ci.appveyor.com/project/tomviner/pytest-ast-back-to-python/branch/master
    :alt: See Build Status on AppVeyor

A plugin for pytest devs to view how assertion rewriting recodes the AST

----

Features
--------

Pytest rewrites the AST (abstract syntax tree) of your tests, for the purpose of displaying the subexpressions involved in your assert statements. This plugin converts that rewritten AST back to Python source, and displays it.


Installation
------------

You can install "pytest-ast-back-to-python" via `pip`_ from `PyPI`_::

    $ pip install pytest-ast-back-to-python


Usage
-----

.. code-block:: bash

    py.test --show-ast-as-python

Example
-------

Take a trivial test like:

.. code-block:: python

    def test_simple():
        a = 1
        b = 2
        assert a + b == 3

View the rewritten AST as Python like this:

.. code-block:: bash

    $ py.test --show-ast-as-python test_simple.py
    ======================================== test session starts ========================================
    plugins: ast-back-to-python-0.1.0, cov-2.2.1
    collected 1 items

    test_simple.py .
    ======================================== Rewritten AST as Python ========================================
    import builtins as @py_builtins
    import _pytest.assertion.rewrite as @pytest_ar

    def test_simple():
        a = 1
        b = 2
        @py_assert2 = a + b
        @py_assert4 = 3
        @py_assert3 = @py_assert2 == @py_assert4
        if @py_assert3 is None:
            from _pytest.warning_types import PytestAssertRewriteWarning
            from warnings import warn_explicit
            warn_explicit(PytestAssertRewriteWarning('asserting the value None, please use "assert is None"'), category=None, filename='/home/tom/.virtualenvs/tmp-483cf04ecc31dda8/test_thing.py', lineno=4)
        if not @py_assert3:
            @py_format6 = @pytest_ar._call_reprcompare(('==',), (@py_assert3,), ('(%(py0)s + %(py1)s) == %(py5)s',), (@py_assert2, @py_assert4)) % {'py0': @pytest_ar._saferepr(a) if 'a' in @py_builtins.locals() or @pytest_ar._should_repr_global_name(a) else 'a', 'py1': @pytest_ar._saferepr(b) if 'b' in @py_builtins.locals() or @pytest_ar._should_repr_global_name(b) else 'b', 'py5': @pytest_ar._saferepr(@py_assert4)}
            @py_format8 = ('' + 'assert %(py7)s') % {'py7': @py_format6}
            raise AssertionError(@pytest_ar._format_explanation(@py_format8))
        @py_assert2 = @py_assert3 = @py_assert4 = None


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `BSD-3`_ license, "pytest-ast-back-to-python" is free and open source software


This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/tomviner/pytest-ast-back-to-python/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi

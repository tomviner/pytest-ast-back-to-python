# -*- coding: utf-8 -*-


def test_ast_as_python_on(testdir):
    """Given I use the cmd line option, I should see rewritten AST as Python."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_ast_as_python_on(request):
            assert request.config.getoption('ast_as_python')
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--show-ast-as-python',
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_ast_as_python_on PASSED',
    ])
    # The expression within the assert statement should be broken down to
    # constituent parts like this:
    result.stdout.fnmatch_lines([
        '*@py_assert1 = request.config',
        "*@py_assert3 = @py_assert1.getoption",
        "*@py_assert5 = 'ast_as_python'",
        '*@py_assert7 = @py_assert3(@py_assert5)',
    ])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0

def test_ast_as_python_off(testdir):
    """Given no cmd line option, I should see no rewritten AST as Python."""

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_ast_as_python_off(request):
            assert not request.config.getoption('ast_as_python')
    """)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v'
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_ast_as_python_off PASSED',
    ])
    assert '@py_assert' not in result.stdout.str()

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'ast-back-to-python:',
        '*--show-ast-as-python*Show how assertion rewriting recoded the AST.',
    ])

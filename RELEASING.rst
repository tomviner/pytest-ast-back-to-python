Releasing
=========

Commit changes and ensure tests pass.

Increment the version number in ``setup.py`` according to *SEMVER*.

Upload to pypi:

.. code-block:: bash

    $ python setup.py sdist bdist_wheel upload -r pypi

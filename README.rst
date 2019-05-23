==================
Outpost Django LTI
==================

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|

.. |docs| image:: https://readthedocs.org/projects/outpost/badge/?style=flat
    :target: https://readthedocs.org/projects/outpost.django.lti
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/medunigraz/outpost.django.lti.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/medunigraz/outpost.django.lti

.. |requires| image:: https://requires.io/github/medunigraz/outpost.django.lti/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/medunigraz/outpost.django.lti/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/medunigraz/outpost.django.lti/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/medunigraz/outpost.django.lti

.. end-badges

LTI integration for LMS like Moodle 3.x.

* Free software: BSD license

Documentation
=============

https://outpost.django.lti.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

pgbackup
========

a cli for backing up remote postgresql databases locally or to aws s3

preparing for development
-------------------------

1. ensure ``pip`` and ``pipenv`` are installed
2. clone the git repository: ``git clone git@github.com:bodanc/pgbackup``
3. fetch the development dependencies: ``make install``

usage
-----

pass in a full database url. the storage driver and the destination

s3 example with bucket name:

::

    $ pgbackup postgres://bogdan@example.com:5432/db_one --driver s3 dumpA.sql

local example with local path:

::

    $ pgbackup postgres://bogdan@example.com:5432/db_one --driver local /var/local/db_one/backups/dumpA.sql

running tests
-------------

run tests locally using ``make`` if the virtualenv is active:

::

    $ make

if the virtualenv is not active, then use:

::

    $ pipenv run make


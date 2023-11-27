==========================
Adding Python Dependencies
==========================

We use `hashin <https://pypi.org/project/hashin>`_ to manage package installs. It helps you manage your ``requirements.txt`` file by adding hashes to ensure that the installed package versions match your expectations.

Before proceeding, make sure you have hashin installed in your environment. See. (:doc:`installing with docker <../install/docker>` ).

Installing hashin
-----------------

To install hashin, run the following command:

.. code-block:: bash

    pip install hashin

.. note::

    hashin is automatically installed in dev.txt requirements file and so should be available in local developer environments.

Adding a new dependency
-----------------------

To add a new dependency using the hashin command line interface, run the following command:

.. code-block:: bash

    hashin -r <requirements file> <dependency>

This command will add hashes and sort the requirements in the specified requirements file, and it will also add comments to indicate any package dependencies.

You can also specify an exact version for the dependency:

.. code-block:: bash

    hashin -r <requirements file> "<dependency>==2.1.3"

After installing a package, check the requirements file diff and make any necessary edits before submitting a pull request with the additions.

Choosing an environment
-----------------------

We use `pipenv <https://pipenv.readthedocs.io/en/latest/>`_ to manage our Python environments. Dependencies are installed based on the environment you are in. You can find the requirements files in the ``requirements`` directory.

You can access the requirements directory `here <https://github.com/mozilla/addons-server/blob/master/requirements>`_.

Installing dependencies
-----------------------

Most of the time, dependencies are automatically installed for you in both CI and local docker environments using make commands. If you need to install dependencies manually, you can do so by calling the make commands directly.

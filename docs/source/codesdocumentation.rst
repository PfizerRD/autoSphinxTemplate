.. toctree::
   :maxdepth: 3

=========
Myscripts
=========

The execution of the socket service for online, real-time application, is perfomed through a Docker container.
In order to build and launch the container, the following commands must be executed within the folder (for Windows OS using PowerShell console)::

   docker build -t socket-service .

The container can be stopped by executing the following command (for Windows OS using PowerShell console)::

   docker stop $(docker ps -a -q --filter ancestor=socket_service)

Example docstrings from Google
==============================

Classes and modules
-------------------

.. automodule:: example_google
   :members:
   :private-members:
   :special-members: __init__

Main routine
------------
The main routine within ``example_google.py`` is showed below:

.. literalinclude:: ../../pythonScripts/main/example_google.py
   :language: python

Source Codes and Configurations
===============================

Python source codes and dependencies
------------------------------------
This section includes all the source codes written in python language and their dependencies.

``example_google.py``
^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../pythonScripts/main/example_google.py
   :language: python

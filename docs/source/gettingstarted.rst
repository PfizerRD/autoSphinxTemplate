.. toctree::

Getting Started
===============

Setup
-----

Populating the paragraph for the `Getting Started`_ section.

Below are some examples on how to highlight literals, code blocks and inline code snippets:

- This is an example of highlighted :literal:`literal` inline with the text. This is done by symply calling the :code:`:literal:` directive, followed by the words you wish to highlight, within quote marks.

- For code blocks, it is possible to invoke the :code:`.. code-block::` directive, followed by the language that will be highlighted. The following snippet shows a python code block directive that emphasizes specific lines (3 and 5):

.. code-block:: rst

  .. code-block:: python
      :emphasize-lines: 3,5

      def some_function():
          interesting = False
          print 'This line is highlighted.'
          print 'This one is not...'
          print '...but this one is.'

which will render as:

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

- This third example covers the highlighted inline code snippets. There are 3 ways to do this:

1. By registering a new role with the :code:`.. role::` directive as:

.. code-block:: rst

  .. role:: python(code)
      :language: python

.. role:: python(code)
    :language: python

That can be used to generate this snippet: :python:`def some_function():`

2. A similar result can be achieved using the :code:`:code:` directive as :code:`:code:`def some_function():``.


That will render as: :code:`def some_function():`

3. If no roles are defined the :code:`:literal:` directive can be used as :code:`:literal:`def some_function():``.


That will also render as: :literal:`def some_function():`

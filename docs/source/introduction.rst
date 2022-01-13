.. toctree::

Introduction
============

This is a demo introduction which include also a random figure.

.. figure:: _static/Fig1.png
   :width: 300px
   :alt: This is a test image
   :class: with-shadow
   :name: Fig1
   :align: center

   Caption for Sphinx documentation logo (remember to keep it indented as the figure itself in the rst-file).

You can write more stuff starting here (without indentation).

.. csv-table:: This is an example of attached csv data file.
   :file: _files/Table_1.csv
   :name: Table1
   :header-rows: 1
   :delim: ;

Below I'm adding more examples of other cool thinks that can be done in Sphinx :ref:`[1]<1>` :

#. This is a numbered item citing a reference [#f1]_ to the footnote below.

* This is a bulleted list citing the figure above :numref:`Fig1`. 
* The same can be done to cite tables :numref:`Table1`.

This is a reference to an acronym: :term:`API` 

For more features not covered within this template, refer to the `Sphinx documentation <https://www.sphinx-doc.org/en/master/>`_.


.. rubric:: Footnotes

.. [#f1] This is a footnote example.

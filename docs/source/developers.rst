########################
Developers documentation
########################

This part of the documentation is for program developers.

Implementing moddingpy in your project
--------------------------------------

Installation
^^^^^^^^^^^^

You need to install the `moddingpy`_ project.

.. _moddingpy: https://github.com/Virinas-code/moddingpy

Directory structure
^^^^^^^^^^^^^^^^^^^

You'll need a ``resources`` folder with multiple subfolders:

``mods``
    Put mods inside.

``plugins``
    Put plugins inside.

``packs``
    Put data packs inside.

Each mod / plugin / data pack is either a directory or a zip file.

Setting up
^^^^^^^^^^

The mod loader :py:mod:`pymodloader`
""""""""""""""""""""""""""""""""""""

In your program initialization you need to call :py:func:`pymodloader.init`.

.. warning:: 
    Be sure to call :py:func:`pymodloader.init` **before** importing your modules

After doing that, :py:mod:`pymodloader` will load all the mods / packs / plugins and install them
(move the files to the desired locations).

When you import your modules after, if they used :py:mod:`moddingpy` they will register the mixins
and APIs using :py:mod:`pymodloader`.

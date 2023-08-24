###############################
ModdingPy - Easy Python modding
###############################

About
=====

What is ModdingPy?
------------------

ModdingPy is an easy-to-use Python library that allows developers to implement a modding system
in their programs. It can be useful for games or other programs.

Structure
---------

There are two main concepts in ModdingPy:

Mixins
   There are pieces of code injected in certain functions.

   .. note::
      All functions should implement mixins, but they are a pretty agressive way of modding.
      Prefer using APIs.

APIs
   Literraly the program itself. For example, let's say you implement a base class :class:`Entity`,
   a mod can access this object and inherit it to create it's own entity.

Files
   Files are managed by the :py:mod:`pymodloader` module and are injected into the program.
   They can then be loaded by the Python module system with :py:func:`pymodloader.load` or
   manually by the program. They are the best way of modding.

Notice ModdingPy itself is composed of two parts: :py:mod:`moddingpy` and :py:mod:`pymodloader`.
The :py:mod:`pymodloader` should be used for loading the mods while :py:mod:`moddingpy` is used
for interacting with the project or the mods.

Mods types
----------

An **extension** is a generic term for anything supported by ModdingPy.

Mod
   A mod modifies the behavior client and server side. When it isn't a client/server architecture,
   mod is the only term used.

Plugin
   A plugin is a server-side only mod.

Addon
   An addon is a client-side only mod.

Data pack
   A server side (and often client-side too) "pack" that is still vanilla (no mixins / apis) and is only composed
   of non-code files, like assets.

Ressource pack
   A client side data pack. Often contains assets but is only visible to the person who isntalled it.

Links
=====

Table of contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   developers
   API Reference <reference/reference>

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

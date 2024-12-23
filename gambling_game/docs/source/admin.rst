Administration
==============


First, run getting started steps

Update Confluence Docs
----------------------

Move to the doc source directory::

   cd gambling_game/docs

Remove all existing documents::

   make clean

Make html docs::

   make html

Build docs on confluence::

    sphinx-build -b confluence ./source build/confluence -E -a

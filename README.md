renumberPDB
===========

This is a nice little script that I have used a lot to change the atom and residue numbers in .pdb structure files.

Usage: ./renumberPDB.py structure.pdb starting_res starting_atom > renumbered_structure.pdb

where structure.pdb is the name of the structural file in which to carry out the renumbering, starting_res is an integer target number of the first residue, starting_atom is the integer target number of the first atom, and renumbered_structure.pdb is the name of the file in which to write the resulting renumbered structure.

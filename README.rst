PyAlarm Device Server
=====================

panic.ds.PyAlarm Device Class

PyAlarm is the alarm device server used by ALBA Alarm System, it requires PyTango and Fandango modules,
both available from tango-cs.sourceforge.net

Some configuration panels in the GUI require PyAlarm to be available in the PYTHONPATH, to do so you can
add the PyAlarm.py folder to the PYTHONPATH variable or copy the PyAlarm.py file within the panic folder;
so it could be loaded as a part of the module.

Requirement
===========

- fandango https://github.com/tango-controls/fandango
- PyTango https://github.com/tango-controls/pytango
- taurus https://github.com/taurus-org/taurus

Installation
============

Run python setup.py install

If you want to build sphinx documentation,
run python setup.py build_sphinx


Usage
=====

Now you can start your device server in any
Terminal or console by calling it:

PyAlarm instance_name

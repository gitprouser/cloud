#!/bin/bash

#replace <path> with the directory location where pythonUtils is installed

export PYTHONUTILSPATH="<path>/pythonUtils"

export PYTHONPATH="${PYTHONPATH}:<path>"
export WLST_PROPERTIES="-Dpython.path=<path>"
''' extensions of lizard '''

from __future__ import print_function
from .version import version
from .htmloutput import html_output
from .csvoutput import csv_output
from .xmloutput import xml_output
from .auto_open import auto_open, auto_read


def print_xml(results, options, _):
    print(xml_output(list(results), options.verbose))
    return 0


def print_csv(results, options, _):
    csv_output(list(results), options.verbose)
    return 0


def print_output(results, options, _):
    html_output(list(results), options, _)
    return 0

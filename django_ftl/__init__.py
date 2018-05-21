from __future__ import absolute_import, print_function, unicode_literals

from .bundle import activator

__version__ = '0.0.1'


def activate_locale(locale):
    activator.activate(locale)


def deactivate_locale():
    activator.deactivate()

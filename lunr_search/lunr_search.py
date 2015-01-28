# -*- coding: utf-8 -*-
"""
lunr search
============

A pelican plugin to ingerate lunr.js search

Copyright (c) Florian Jacob
"""

from __future__ import unicode_literals

import os.path
import json

from pelican import signals


class LunrSearchJsonGenerator(object):
    def generate_output(self, writer):
        pass


def get_generators(pelican_object):
    return LunrSearchJsonGenerator

def register():
    signals.get_generators.connect(get_generators)

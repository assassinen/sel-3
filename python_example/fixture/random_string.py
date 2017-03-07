__author__ = 'NovikovII'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

def random_string(key, len):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*10
    return "".join([random.choice(symbols) for i in range(len)])

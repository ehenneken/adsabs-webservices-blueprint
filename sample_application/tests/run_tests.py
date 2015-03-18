#!/usr/bin/env python
import unittest2
import sys

if __name__ == '__main__':
  suite = unittest2.TestLoader().discover('unittests')
  results = unittest2.TextTestRunner(verbosity=3).run(suite)
  if results.errors or results.failures:
    sys.exit(1)

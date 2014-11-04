#!/usr/bin/env python


import sys
import argh
import atexit
import logging
import StringIO


logging.basicConfig(level=logging.DEBUG)
_testcases = []


@argh.named('stdio')
def _test_from_stdio():
    pass


@argh.named('files')
def _test_from_files(input_file, output_file):
    logging.debug('Configuring test case using "%s" as input and "%s" as output' % (input_file, output_file))
    logging.debug('Mocking stdin and stdout...')
    sys.stdin = StringIO.StringIO()
    sys.stdout = StringIO.StringIO()

    logging.debug('Preparing stdin contents...')
    with open(input_file, 'rU') as f:
        sys.stdin.truncate(0)
        sys.stdin.write(f.read())
        sys.stdin.seek(0)

    def _test_it():
        logging.debug('Verifying stdout contents...')
        try:
            output = sys.stdout.getvalue().split('\n')
            with open(output_file, 'rU') as f:
                for file_line, output_line in zip(f.readlines(), output):
                    expected_line = file_line.strip()
                    actual_line = output_line.strip()
                    if actual_line != expected_line:
                        logging.warn(('Error: \n\t'
                                      'Result "%s" differs from expected "%s"' % (actual_line,
                                                                                  expected_line)))
                        sys.exit(1)
            logging.info('OK: Tests are passing!')
        finally:
            logging.debug('Un-Mocking stdin and stdout...')
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

    logging.debug('Registering exit handler for result comparison...')
    atexit.register(_test_it)
    logging.debug('Test setup done!')


def add_testcase(input_file, output_file):
    logging.debug('Adding test case using "%s" as input and "%s" as output' % (input_file, output_file))
    _testcases.append((input_file, output_file))


def configure(*args):
    for arg in args:
        add_testcase(*arg)

    cmds = [_test_from_stdio, _test_from_files]
    if len(_testcases):
        @argh.named('included')
        def _test_from_given_testcase():
            for f in _testcases:
                _test_from_files(f[0], f[1])
                break
        cmds.append(_test_from_given_testcase)

    argh.dispatch_commands(cmds)

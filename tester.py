#!/usr/bin/env python


import sys
import argh
import atexit
import logging
import StringIO


@argh.named('from-file')
def _config_testcase(input_file, output_file):
    logging.debug('Preparing StdIn...')
    with open(input_file, 'rU') as f:
        sys.stdin.truncate(0)
        sys.stdin.write(f.read())
        sys.stdin.seek(0)

    def _test_it():
        logging.debug('Verifying StdOut')
        try:
            output = sys.stdout.getvalue().split('\n')
            with open(output_file, 'rU') as f:
                for file_line, output_line in zip(f.readlines(), output):
                    expected_line = file_line.strip()
                    actual_line = output_line.strip()
                    if actual_line != expected_line:
                        logging.debug(('Error: \n\t'
                                       'Result "%s" differs from expected "%s"' % (actual_line,
                                                                                   expected_line)))
                        sys.exit(1)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
        logging.debug('Test OK!')

    logging.debug('Registering exit handler...')
    atexit.register(_test_it)


def _config():
    sys.stdin = StringIO.StringIO()
    sys.stdout = StringIO.StringIO()


def config_testcase(input_file, output_file):
    logging.basicConfig(level=logging.DEBUG)
    _config()
    _config_testcase(input_file, output_file)


def config_arguments():
    logging.basicConfig(level=logging.DEBUG)
    _config()
    argh.dispatch_command(_config_testcase)


def config_terminal():
    logging.basicConfig(level=logging.DEBUG)

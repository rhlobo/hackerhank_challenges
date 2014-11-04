hackerhank_challenges
=====================

Solutions for https://www.hackerrank.com

### Running a challenge

Just run them...

Some of the challenge's immplementations import the `tester` module, 
enabling more options on how tests can be execute:

- __stdio__: Runs the challenge normally. Input and output should be provided thorugh `stdin` and `stdout`, as specified by HackerHank. The values should be in the same format as in the problem description.
- __files__: Configure a test case supplying both an input file and an output file.
- __included__: Runs the challenge's pre-configured test cases (should be configured at the challenges source code, just after importing `tester`)

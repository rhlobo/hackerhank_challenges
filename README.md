hackerhank_challenges
=====================

Solutions for some https://www.hackerrank.com challenges.

### Running a challenge

Just run them...

Some of the challenge's immplementations import the `tester` module, 
enabling more options on how tests can be execute:

````bash
$ ./sherlock-and-squares.py
usage: sherlock-and-squares.py [-h] {stdio,files,included} ...
````


- __stdio__: Runs the challenge normally. Input and output should be provided thorugh `stdin` and `stdout`, as specified by HackerHank. The values should be in the same format as in the problem description.
- __files__: Configure a test case supplying both an input file and an output file.
- __included__: Runs the challenge's pre-configured testcases (option shown only if pre-configured testcases are available). Configuration is done at the challenges source code, just after importing `tester`.

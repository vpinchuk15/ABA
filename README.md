# ABA
Address Book Application 

There are four versions of the ABA:

V1: Old ABA - first attempt with other contributors, contains bugs
V2: EncryptABA - implements file encryption
V3: FuzzABA - ABA program modified to fit with fuzz testing
        -> input file needs qw1, qw2 with no newline
        -> output file should have no lines
        -> answers file needs Password do not match. in the first line with no new lines
        -> .csv files needed for testing import function
        -> contains an aba, etc. files with minor modified functions for fuzzing
        -> to start fuzzing delete all data files the ABA may have produced
V4: Final ABA after fuzz testing
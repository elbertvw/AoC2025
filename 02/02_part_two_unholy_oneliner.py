print(sum(sum(i for i in range(*map(int, r.split('-'))) if str(i) in (str(i)*2)[1:-1]) for r in open('input').read().split(',')))

'''
I am deeply sorry. 

Anyhow: although slower than my more normal solution due to lack of concurrency (while still being an ugly bruteforce 
solution), this actually uses a cool and noteworthy way to check if a string consists of a repeating substring (LC459). 
I found it elsewhere and haven't incorporated it into my own main solution.

I'll document it here so I'll still understand a while from now. 

Python:

    string in (string + string)[1:-1] 

And in Java, the language of my forefathers, this would be:

    (string + string)
        .substring(1, (string + string).length() - 1))
        .contains(string);

What does it check? It checks whether, when doubling the string and slicing off the first and last characters, the 
original string is contained in the resulting string. 

Worked examples:

abcabc -> doubled -> abcabcabcabc -> remove first and last -> bcabcabcab -> contains abcabc, therefore true.
abdabc -> abdabcabdabc -> bdabcabdab -> false, does not contain abdabc
aaaaba -> aaaabaaaaaba -> aaabaaaaab -> false, does not contain aaaaba

And so forth.

Attempt at an explanation: 

If a string consists of a repeating pattern P, the string can be represented as PP or more P's. 
Let's assume PP. (e.g. abcabc, where P = abc)
Doubling would yield PPPP. Shaving off the first and last characters of PPPP yields XPPX.
Here X is a sequence of chars that is not the pattern.
As you can see, PP is still present in the string XPPX.

The same does not apply to strings that do not consist of a repeating pattern. For example:
Doubling XPPX (e.g. aabbbbaa) we get XPPXXPPX. 
Shaving off first and last: YPPXXPPY, where Y is another different sequence of chars.
XPPX is no longer present. 

'''
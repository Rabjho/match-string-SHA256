# Match a word from a list to a SHA256 hash

## License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## About
This tool can take a word from a list and check if it matches a set SHA256 hash.

Developed by @Rabjho

## Usage
Lines may have multiple objects. By default the last item is used as the word tested for matching, however this can be changed with the `-i` flag. The default seperator within lines is ',' however this can be changed with the `-s` flag. 

The item chosen may be encompassed by any number of characters (i.e. any number of quotes "" or """") but in this case the amount should be changed with `-r <num of characters around word>`

File encoding can be changed with the `-e` flag. Any text encoding supported by python can be used ([click here for supported encodings](https://docs.python.org/3.9/library/codecs.html))

If you want to see the whole line, where the word matching the SHA-hash is found, use `-l`

## Example usage:
`python passwd_sha_match.py -f breach.txt -m d04b98f48e8f8bcc15c6ae5ac050801cd6dcfd428fb5f9e65c4e16e7807340fa`

For further help use `python passwd_sha_match.py -h`

### Dependencies:
Python version 3.9 or later
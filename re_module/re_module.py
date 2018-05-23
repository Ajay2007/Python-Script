import re    # import re module


text_to_search = '''

abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
800-555-1234
900-555-1234
123.555.1234

123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''
sentence = 'Start a sentence and then bring it  to and end'

# what is raw string 
	# The raw string in python is just a string prefixed with r
# print (r'\tTab'))
	# so basically raw string is ignore every special tab and new line 
	# if it exists in a string

# searching for literal characters

# pattern = re.compile(r'abc')
# print (type(pattern))
# print (pattern)
# matches = pattern.finditer(text_to_search)

# for match in matches:
# 	print(match)

# print(text_to_search[2:5])

# re search is case sensitive
# . is a special character in regular expression
# for escaping this special characters we use back slash

# pattern = re.compile(r'\.')

# # for search for url 

# pattern = re.compile(r'coreyms\.com')

# matches = pattern.finditer(text_to_search)

# for match in matches:
# 	print(match)
# print (text_to_search[143:154])

# pattern1 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')


## for a specific pattern matching like suppose if I want
## to search for 123.345.4334 or 123-345-4324 then I will
## put those matching charcter in [.-] for re.compile

# pattern2 = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
# matches2 = pattern2.finditer(text_to_search)
# for match2 in matches2:
# 	print (match2)
# matches1 = pattern1.finditer(text_to_search)

# for match1 in matches1:
# 	print (match1)


# with open('data.txt', 'r', encoding='utf-8') as f:
# 	# pattern = re.compile(r'f')
# 	contents = f.read()

# 	matches = pattern1.finditer(contents)

# 	for match in matches:
# 		print (match)


## suppose I want to search for a specific number like 800
## or 900 then I will use [89] for selecting first character
## as 8 or 99 and followed them with 00

pattern3 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')


# matches3 = pattern3.finditer(text_to_search)
# for match3 in matches3:
# 	print (match3)


## similar task performing on data.txt


with open('data.txt', 'r', encoding='utf-8') as f:
	# pattern = re.compile(r'f')
	contents = f.read()

	matches = pattern3.finditer(contents)

	for match in matches:
		print (match)
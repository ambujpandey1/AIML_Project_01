from numpy import argmax
# define input string
data = 'hello world'
print(data)
# define universe of possible input values
alphabet = 'abcdefghijklmnopqrstuvwxyz '

# define a mapping of chars to integers
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
print ("\n\nchar_to_int=\n", char_to_int)


int_to_char = dict((i, c) for i, c in enumerate(alphabet))
print ("\n\nint_to_char=\n", int_to_char)
# integer encode input data
integer_encoded = [  char_to_int[char] for char in data  ]
print("\n\ninteger_encoded =\n", integer_encoded)

# one hot encode
onehot_encoded = list()

for value in integer_encoded:   #[7, 4, 11, 11, 14, 26, 22, 14, 17, 11, 3]
	letter = [0 for _ in range(len(alphabet))]
	#letter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	letter[value] = 1
	onehot_encoded.append(letter)

print("\n\nonehot_encoded =\n", onehot_encoded)
# invert encoding
inverted = int_to_char[argmax(onehot_encoded[1])]
print("\n\nonehot_decoded =\n",inverted)
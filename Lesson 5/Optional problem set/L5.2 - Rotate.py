# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    n_ = n % 26
    result = chr(ord(letter) + n_)
    if ord(result) > 122: # z
        return chr((96 + ord(result)) % 122) 
    return result

def rotate(words,n):
    n_ = n % 26
    rotated = ''
    for ltr in words:
        if ltr == ' ': # space
            rotated = rotated + ' '
        else:
            rotated = rotated + shift_n_letters(ltr, n_)
    return rotated

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
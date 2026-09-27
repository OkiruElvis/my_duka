# display odd numbers from 46 to 124 in a list using list comprehension

odd_numbers=[x for x in range(46,125) if x%2 !=0 ]
print(odd_numbers)

#create a list of squares for numbers 1 to 5 e.g [1,4,9,16,25]

squares = [x**2 for x in range(1, 6)]
print(squares)

#words=["cat","elephant","dog","python"] ->get the length of each word and have them in a list

words = ["cat", "elephant", "dog", "python"]

word_len = [len(word) for word in words]
print(word_len)
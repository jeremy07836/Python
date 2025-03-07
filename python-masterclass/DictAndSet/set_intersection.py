from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(evens.intersection(squares))

even_squares = evens.intersection(squares_generator(100))
print(even_squares)


# intersection challenge
text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

text_split = text.split()
preps_used = set(text_split) & set(prepositions)
print(preps_used)

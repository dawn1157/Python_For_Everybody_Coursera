#The solutiion for the problem 6.5:

text = "X-DSPAM-Confidence:    0.8475"
finder = text.find("0")
the_float = text[finder:]
print(the_float)

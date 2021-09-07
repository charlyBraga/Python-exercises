
#Description: the goal this code is to discover how are sorted letters upercase and lowercase

#define var values
a, b, c, A, B, C ='a','b','c','A','B','C'

#insert values in list
x = [a,b,c,A,B,C]

#print values ASCII for each letter
print("\nValues ASCII for letter")
print(a,': ', ord(a))
print(b,': ', ord(b))
print(c,': ', ord(c))
print(A,': ', ord(A))
print(B,': ', ord(B))
print(C,': ', ord(C))

#sort list by ASCII value
x.sort()

#print list sorted
print('\nValues sorteds: ',x)
# The students of sidstric college have subscriptions to English and French newspapers.
# Some students have subscribed to English, some havve subscribed only French and some
# have subscribed to both newspapers.
#You are given two sets of studetn roll numbers.One set has subscribed to the English Newspapers
# and the other set is subscribed to the French newspaper. The same student could be in
# both sets. Xour task is to find the total number of students who have subscribed to
#  English or French news paper but not both.
a=int(input())
A= set(map(int,input().split()))

b=int(input())
B= set(map(int,input().split()))

print(len(A^B)) #symmetric_difference operator symbol is ^

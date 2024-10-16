# The students of sidstric college have subscriptions to English and French newspapers.
# Some students have subscribed to English, some havve subscribed only French and some
# have subscribed to both newspapers.
#You are given two sets of studetn roll numbers.One set has subscribed to the English Newspapers
# and the other set is subscribed to the French newspaper. The same student could be in
# both sets. Xour task is to find the total number of students who have subscribed to
# at least one news paper.

n=int(input()) # no. of subscriptions for english
A=set(map(int,input().split())) # rollnumbers
b=int(input()) # no. of subscriptions for French
B=set(map(int,input().split())) # rollnum
print(len(A.union(B)))

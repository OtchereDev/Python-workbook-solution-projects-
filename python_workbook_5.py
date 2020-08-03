"""
This is the fifth chapter of The Python Workbook 
the solution to the exercise
'List Exercise'
"""

#Exercise 104
# user_=int(input('What integer do you want to record:\n\t'))
# cont_= []
# cont_.append(user_)
# while True:
#     user_=int(input('What next integer do you want to record:\n\t'))
#     if user_ != 0:
#         cont_.append(user_)
#     else:
#         break

# print('The values recorded are:\n')
# cont_=sorted(cont_)

# for i in cont_:
#     print(i)

#Exercise 105
# user_=int(input('What integer do you want to record:\n\t'))
# cont_= []
# cont_.append(user_)
# while True:
#     user_=int(input('What next integer do you want to record:\nEnter "0" to stop recording\n\t'))
#     if user_ != 0:
#         cont_.append(user_)
#     else:
#         break

# print('The values recorded are:\n')
# cont_=sorted(cont_,reverse=True)

# for i in cont_:
#     print(i)

#Exercise 106
# def outlier(list_: list,n: int):
#     copy=sorted(list_)
    
#     for i in range(n):
#         copy.pop()
            
#     for i in range(n):
#         copy.pop(0)
    
#     return copy


# def main():
#     user_=int(input('What integer do you want to record:\n\t'))
#     cont_= []
#     cont_.append(user_)
#     while True:
#         user_=int(input('What next integer do you want to record:\nEnter "0" to stop recording\n\t'))
#         if user_ != 0:
#             cont_.append(user_)
#         else:
#             break
#     if len(cont_)<4:
#         print('You dont have enough value entered')
#     else:
#         print('The values without the outliers: ',outlier(cont_,2))
#         print('The original values are ', sorted(cont_))

# main()


#Exercise 107
# user_=input('What do you want to record:\n\t')
# cont_=[]
# cont_.append(user_)

# while True:
#     user_=input('What is the next thing:\nEnter blankspace to exit\n\t')
    
#     if user_ not in cont_:
#         cont_.append(user_)
#     if user_=='':
#         break
    

# print('Your records are :')
# for i in cont_:
    # print(i)


#Exercise 108
# negative=[]
# postive=[]
# zeros=[]

# user_=input('What is your number:\n\t')

# while True:
#     if user_=='':
#         break

#     user_=int(user_)

#     if user_<0:
#         negative.append(user_)
#     elif user_>0:
#         postive.append(user_)
#     else:
#         zeros.append(user_)

#     user_=input('What is your number:\n\t')

# print('The negative numbers are:')
# for i in sorted(negative):
#     print(i)

# print('The zeros are:')
# for i in zeros:
#     print(i)

# print('The positive numbers are:')
# for i in sorted(postive):
#     print(i)    

#Exercise 109

# def proper_divisor(n):
#     i=1
#     divisor=[]
#     while i<n:

#         if n%i==0:
#             divisor.append(i)
        
#         i+=1

#     return divisor


# def main():
#     user_=int(input('What is the positive number:\n\t'))

#     divisors=proper_divisor(user_)
    
#     if len(divisors)!=0:
#         print(f'The proper divisors of {user_} are:')
#         for i in divisors:
#             print(i)

#     else:
#         print('The positive number does not have any proper number')

# if __name__ == "__main__":
#     main()


#Exercise 110
# def perfect_number(n:int):
#     divisors=proper_divisor(n)

#     sum_=sum(divisors)
#     if n == sum_:
#         return True
#     else:
#         return False
    
# def main():
#     for i in range(1,1001):
#         output=perfect_number(i)

#         if output==True:
#             print(i)

# main()

#Exercise 111
# def words_only(user_: str):
#     new_cont=user_.split()
#     removal=['.',';',':','?',',','!',"'"]
#     words_only=[]
#     exempt=[ "don't", "isn't","wouldn't"]
#     # no_punct=''
#     # for char in user_:
#     #     if char not in removal:
#     #         no_punct+=char

#     # no_punct_list=no_punct.split()
    
#     for i in new_cont:
        
#         if i in removal:
#             new_cont.remove(i)
#             # print(new_cont)
    
#     for k in new_cont:
#         if k not in exempt:
#             word=''
#             for m in k:
#                 if m not in removal:
#                     word+=m
#         else:
#             word=k
#         words_only.append(word)

#     return words_only

# def main():
#     user_=input('Please provide the sentence with punction:\n\t')
#     new_user_=words_only(user_)
#     print(f'The words in your sentence without punction are:\n{new_user_}')

# if __name__ == "__main__":
#     main()


#Exercise 112
# cont_=[]
# below_avg=[]
# above_avg=[]
# while True:
#     user_=input('What is the value:\n\t')
    
#     if user_!='':
#         user_=int(user_)
#         cont_.append(user_)
#     else:
#         break

# avg=sum(cont_)/len(cont_)

# for i in cont_:
#     if i<avg:
#         below_avg.append(i)
#     else:
#         above_avg.append(i)

# print('The values below the average are\n\t',below_avg)
# print('The average of the values is :\n\t',avg)
# print('The values above the average are:\n\t',above_avg)


#Execrise 113
# def formatList(list_:list):
    
#     if len(list_)==0:
#         return '<Empty>'
#     if len(list_)==1:
#         return str(list_[0])
    
#     sentence=''

#     for i in range(0,len(list_)-2):
#         sentence= sentence+ str(list_[i])+', '

#     sentence = sentence+ str(list_[len(list_)-2]) +' and '
#     sentence = sentence + str(list_[len(list_)-1]) 

#     return sentence

                     
# def main():
#     list_=[]
#     user_=input('What do you want to add to the list (Enter a blank line to exist)\n\t')
#     while user_!='':
#         list_.append(user_)
#         user_=input('What do you want to add to the list (Enter a blank line to exist)\n\t')
    
#     print('The list consist of %s' %formatList(list_))
    
# main()

#Exercise 114
# from random import randrange 

# lotto_number=[]

# while True:
#     new_number=randrange(1,49)

#     if new_number not in lotto_number:
#         lotto_number.append(new_number)

#     if len(lotto_number)==6:
#         break

# lotto_number=sorted(lotto_number)

# print('The lotto number for today:')

# for i in lotto_number:
#     print(i)


#Exercise 115 & 116
# user_=input('What is the sentences:\n\t')
# user_n=user_
# cont_=user_n.split()
# new_sent_w=[]
# vowel=['a','o','e','i','u','A','O','E','I','U']

# for i in cont_:
#     user_cap=i
    
#     user=i
#     if user[0] not in vowel:
#         for i in range(len(user)):
            

#             for k in user:
#                 # print(k)
#                 if k  not in vowel:
#                     user=user.replace(k,'')
#                     user=user+k    
#                 if k  in vowel:
                    
#                     break
#         user=user+'ay'
#         if user_cap[0].isupper():
#             user=user.title()
        
#     else:
#         user=user+'way'
#         if user_cap[0].isupper():
#             user=user.title()

#     new_sent_w.append(user)
        
# joiner=' '.join(new_sent_w)

# print(f'The pig latin of the sentence\n\t{user_}:\n\nPig Latin:\n\t{joiner}')



#Exercise 117
# x=[]
# y=[]

# user_x=input('What is the value of x:\n\t')
# user_y=input('What is the value of y:\n\t')

# while True:
#     x.append(float(user_x))
#     y.append(float(user_y))

#     user_x=input('What is the value of x:\nEnter balnk space to exist\n\t')
#     if user_x=='':
#         break
    
#     user_y=float(input('What is the value of y:\n\t'))

# up_1=0

# up_2= (sum(x)*sum(y))/len(x)

# bot_1=0

# bot_2=(sum(x)**2)/len(x)

# for i in range(len(x)):
    
#     up1=(x[i]*y[i])
    
#     up_1+=up1
#     j=x[i]**2
#     bot_1+=j

# m=(up_1-up_2)/(bot_1-bot_2)

# b=(sum(y)/len(y))-(m*(sum(x)/len(x)))

# print(f'The equation for the line of best fit is:\n\ty={m}m + {b}')

#Exercise 118
# from random import randint,choice


# values=[str(i) for i in range(2,10)]+[ 'T', 'J', 'Q', 'K', 'A']
# suits=['s','h','d','c']


# def creatCard():
#     deck=[]
#     for i in values:
#         for k in suits:
#             d=i+k
#             deck.append(d)
#     return deck

# def shuffle():
#     deck=creatCard()
    
#     for i in range(len(deck)):
#         for k in deck:
#             deck.remove(k)
#             deck.insert(randint(0,52),k)
#     return deck


# def main():
#     original_card=creatCard()
#     shuffled_card=shuffle()

#     print(f'The original card deck is\n\t{original_card}')
#     print(f'\n\nThe shuffled card deck is \n\t{shuffled_card}')

# if __name__ == "__main__":
#     main()

#Exercise 119

# def deals(number_of_hands, card_per_hand, card_deck):
#     player=[]
#     deck1=card_deck
    
#     for i in range(number_of_hands):
#         player.append([])
#     for i in range(card_per_hand):
#         for j in range(len(player)):
#             catch=choice(deck1)
#             player[j].append(catch)
#             deck1.remove(catch)
    
#     return player,deck1

# def main():
#     card=creatCard()        
#     card_play,card_left=deals(4,5,card)

#     for i in range(len(card_play)):
#         print(f'The player {i+1} card are:')
#         print(card_play[i])
#     print('The cards left in the deck are:')
#     print('\t',card_left)

# main()

#Exercise 120

# def ordered(list_ :list):
#     if len(list_)==0:
#         return 'Empty'
#     elif len(list_)==1:
#         return 'single'
#     elif list_ == sorted(list_):
#         return True
#     else:
#         return False


# def main():
#     cont_=[]
#     user_=input('What do you want to add to the container:\n\t')

#     while True:
#         cont_.append(user_)

#         user_=input('What do you want to add to the container:\nEnter a blankspace to exit\n\t')

#         if user_=='':
#             break

#     answer=ordered(cont_)

#     if answer=='Empty':
#         print('Sorry, the list is empty')
#     elif answer=='single':
#         print('The list contain only one item')
#     elif answer==True:
#         print('This list is sorted')
#     elif answer==False:
#         print('This list is not sorted')

# main()

#Exercise 121

# def countRange(list_:list,min:int,max:int):
#     count_range=0

#     for i in list_:
#         if i >= min and i<=max:
#             count_range+=1

#     return count_range


# def main():
#     list_=[1,5,9,7,3,5,9,10,5,4,3,2]

#     print('The number of digit in the range 1 and 6 is %d' %countRange(list_,1,6))

# main()

#Exercise 122

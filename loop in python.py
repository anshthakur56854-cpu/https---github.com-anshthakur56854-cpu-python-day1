# WHEN WE NEED TO REPEATA STATEMENT OR SET OF STATEMENT AGAIN AND AGAIN WE USE THE LOOPS:
#THERE ARE TWO TYPES OF LOOPS IN PYTHON 
#   1. FOR LOOP     2.while loop 



# 1. while loop :


# #while condtion :
#      statement(s)
# incr/ decr loop_counter


# Start
#   ↓
# Variable initialise
#   ↓
# Condition check
#   ↓
# True? ─── No ──► Loop End
#   │
#  Yes
#   ↓
# Code execute
#   ↓
# Variable update
#   ↓
# Condition check (फिर से)



# eg: 
# i = 1
# while i <= 10 :
      
#     print(f"{i}. hello Anshu ❤️")
#     i = i + 1
      

# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1

# print("Loop khatam")


# DRAY RUN

#  i       condition              output

#   1.       1<=5 True           hello Anshu ❤️
#   2.       1<=5 True           hello Anshu ❤️
#   3.       1<=5 True           hello Anshu ❤️
#   4.       1<=5 True           hello Anshu ❤️
#   5.       1<=5 True           hello Anshu ❤️
#   6.       1<=5 

# PRINT 10 TO 1 IN  REVERSE ORDER :

# i = 10 
# while i >= 1 :
#     print(i)
#     i = i - 1


# PRINT TABLE OF 2 :

# i = 1 
# while i <= 10: 
#     print(f "2*{i} = {2*i}")
#     i = i + 1



# num = int(input("Enter a number :"))

# i = 1 
# while i <= 10: 
#     print(f"{num} * {i} = {num * i}")
#     i = i + 1


# i = 1
# while i <= 10:
#     print( i * i)
#     i = i  + 1


#    i = 1
# while i <= 10:
#     print( {i + 1} * i)
#     i = i  + 1 


#SUM OF 1 TO 10 NATURAL NUMBER :
# i = 1
# sum = 0

# while i <= 10:
#      sum = sum + i
#      i = i  + 1
# print("Sum  = ", sum )

#ENTER THE NUMBER  AND FIND TIS  FACTORIAL! NUMBER :

# num = int(input("Enter a number :"))

# fact = 1
# i = 1

# while i <= num:
#      fact = fact * i
#      i = i + 1

# print ("Factorial =", fact)

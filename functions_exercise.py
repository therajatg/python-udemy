# def arrayCheck(nums):
#   for index in range(len(nums)-2):
#     if nums[index] == 1:
#       if nums[index+1]==2 and nums[index+2]==3:
#         return True
#   return False

# print(arrayCheck([1, 1, 2, 1, 2, 3]) )


# def stringBits(str):
#   # CODE GOES HERE
#   print(str[::2])

# stringBits('Heeololeo')

# def end_other(a, b):
#   # CODE GOES HERE
#   a_len = len(a)
#   b_len = len(b)
#   if(a_len > b_len):
#     if(a[a_len-b_len:].lower() == b.lower()):
#         return True
#   elif(b[b_len-a_len:].lower() == a.lower()):
#       return True
#   return False

# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXafc'))




# def doubleChar(str):
#   # CODE GOES HERE
#   newstr = ""
#   for word in str:
#     newstr = newstr + word + word
#   print(newstr)

# doubleChar('The')
# doubleChar('AAbb')
# doubleChar('Hi-There')



# def count_evens(nums):
#   return filter(lambda num: num%2==0, nums)

# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))


# import random

# def guess_the_number():
#     digits = list(range(10))
#     random.shuffle(digits)
#     actual_list = digits[:3]
#     flag=True

#     def guessed_number():
#         guess = input("What is your guess? ")
#         first_digit = int(guess/100)
#         second_digit = int(guess/10) - first_digit*10
#         third_digit = guess - int(guess/10) * 10
#         guessed_list = [first_digit, second_digit, third_digit] 
#         if(actual_list[0] == guessed_list[0] and actual_list[1] == guessed_list[1] and actual_list[2] == guessed_list[2]):
#             print("Hurrat!!!! You Won")
#             return False
#         elif(actual_list[0] == guessed_list[0] or actual_list[1] == guessed_list[1] or actual_list[2] == guessed_list[2]):
#             print("Match: You've guessed a correct number in the correct position")
#             return True
#         elif(actual_list[0] in guessed_list or actual_list[1] in guessed_list or actual_list[2] in guessed_list):
#             print("Close: You've guessed a correct number but in the wrong position")
#             return True
#         else:
#             print("Nope: You haven't guess any of the numbers correctly")
#             return True
    
#     while(flag):
#         flag = guessed_number()

# guess_the_number()


#Can convert an input directly into a list. Here if you are pressing a number you'll get a number as input unlike in JS where it does not matter what you pressed, you always get input stuff in string format.


# entered_data = input("Enter something")
# print(entered_data)

# x = 25
# def my_func():
#     x = 50
#     return x

# my_func()
# print(x)

# mylist = [1,2,3]
# print(type(mylist))

# class Dog():
# 	def __init__(self, breed):
# 		self.breed = breed;
# mydog = Dog("Lab")
# print(mydog.breed)

# class Animal():
# 	def __init__(self):
# 		print("Animal Created")
# 	def eat(self):
# 		print("Animal Eating")

# my_animal = Animal()
# my_animal.eat()

# class Dog(Animal):
# 	def __init__(self):
# 		print("Dog Created")
# 	def sound(self):
# 		print("Dog Barking")

# my_dog = Dog()
# my_dog.sound()
# my_dog.eat()

# class Book():
# 	def __init__(self, author, title, pages):
# 		self.author = author;
# 		self.title = title;
# 		self.pages = pages;
# 	def __str__(self):
# 		return ("Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages))

# mybook = Book("Rajat", "Dare to Dive", 500 )
# print(mybook)

# class Book():
# 	def __init__(self, author, title, pages):
# 		self.author = author;
# 		self.title = title;
# 		self.pages = pages;
# 	def __str__(self):
# 		return ("Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages))
# 	def __len__(self):
# 		return self.pages

# mybook = Book("Rajat", "Dare to Dive", 500 )
# print(len(mybook))


class Book():
	def __init__(self, author, title, pages):
		self.author = author;
		self.title = title;
		self.pages = pages;
	def __str__(self):
		return ("Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages))
	def __len__(self):
		return self.pages
	def __del__(self):
			print("The object is destroyed")

mybook = Book("Rajat", "Dare to Dive", 500 )
del mybook



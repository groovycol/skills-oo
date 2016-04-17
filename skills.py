# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?
# 1. Abstraction
# 2. Encapsulation
# 3. Polymorphism

#  Explain each concept.
#
# Abstraction: you can design a "base" class that is not meant to be a functioning class 
# that you would call directly, but instead is a super class that is made fully functional 
# by the subclasses that define additional attributes and methods

# Encapsulation: data that is needed for a class is stored near where it is needed. This keeps 
# everything together to make code more readable and maintainable
#
# Polymorphism: allows you to have interchangeable components in classes. You can define an 
# action for a class, but for each subclass you can write a different action that you need 
# for that subclass, without conditionals.

# 1. What is a class? A class is a structure you define in python, kind of like a customized data type
# that you define the properties of

# 2. What is an instance attribute? When you instantiate an object, it picks up attributes, or variables
# set by you or by the class it belongs to.

# 3. What is a method? A method is a function defined inside a class. That method is available to any instance
# of that class, but can't be called directly from outside the class objects.

# 4. What is an instance in object orientation? An instance is a declared assignment of a variable to a class. 
# When you say 'mything = ThisClass()', you are creating an object that inherits attributes from the the class ThisClass.

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
# A class attribute are variables assigned inside the class. Instance attributes are assigned by software at runtime.
# An instance of a class may have both instance attributes and class attributes. For this example:
# my_dog = Dog()
# where class Dog is defined as:
# class Dog(object):
#       color = black
# my_dog.color is a class attribute set to the color black. 
# If you change the color with:
# my_dog.color = rust
# you have assigned an instance attribute that will take precedence over the class attribute 
# You can also assign other attributes to the instance to use as you work with the object, like
# my_dog.name = "Wheezy"
# You'd use instance attributes to give you flexibility in working with the object.

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A Student"""

    def __init__(self, first_name, last_name, address):
        """Initialize a Student object, requires first name, last name and address"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question and its correct answer"""

    def __init__(self, question, answer):
        """initialize a Question object, requires a question and answer"""
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """a method that asks for user input for questions and evaluate response"""

        user_answer = raw_input("{}. Please enter your answer: ".format(self.question))
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(object):
    """An Exam """

    def __init__(self, name):
        """Initialize an Exam object, requires an exam name or descriptor"""
        self.name = name
        self.exam_questions = []
      
    def add_question(self, question, correct_answer):
        """method to add questions to an exam. stores a list of Question objects"""
        question = Question(question, correct_answer)
        self.exam_questions.append(question)

    def administer_exam(self):
        """method to administer all the questions in teh exam and return a score"""
        final_score = 0
        score = 0
        num_questions = 0
        for quest in self.exam_questions:
            num_questions += 1
            if quest.ask_and_evaluate():
                score += 1

        return float(score) / float(num_questions)


# class Quiz(Exam):
#     self.exam_type = "quiz"


def take_test(Exam, Student):
    """Administer an exam to a student, and assign the score as an instance
    attribute for the Student object

    """
    Student.score = Exam.administer_exam()
    return Student.score


def example():
    #instantiate an instance of the Exam class
    test = Exam("midterm")

    #add some questions to the object Exam
    test.add_question("What is the capital of California?", "Sacramento")
    test.add_question("Name a 3 syllable benefit of O-O programming?", "Abstraction")
    test.add_question("What color is Balloonicorn?","Pink")
    test.add_question("How many hours should you spend on homework?", "6")

    #instantiate an instance of the Student class
    test_taker = Student("Wilma", "Flintstone", "22 BedRock Way")

    #administer the exam
    take_test(test, test_taker)

    print "{} {}'s score on the {} test is {}%".format(test_taker.first_name,
                                                        test_taker.last_name,
                                                        test.name,
                                                        test_taker.score)


# def example_quiz():
#     #instantiate an instance of the Exam class
#     test = Quiz("popquiz")

#     #add some questions to the object Exam
#     test.add_question("What color is Balloonicorn?","Pink")
#     test.add_question("How many hours should you spend on homework?", "6")

#     #instantiate an instance of the Student class
#     test_taker = Student("Betty", "Ruble", "24 BedRock Way")

#     #administer the exam
#     take_test(test, test_taker)

#     print "{} {}'s score on the {} test is {}%".format(test_taker.first_name,
#                                                         test_taker.last_name,
#                                                         test.name,
#                                                         test_taker.score)
example()
# example_quiz()

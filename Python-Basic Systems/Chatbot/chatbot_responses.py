# This special function used for Chatbot responses
# This code is used for the Chatbot.py
# re: Detect math (or specific) expressions in the input
import re
import math
import random
from datetime import datetime


def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ['hi', 'hello', 'hi there']:
        responses = ["Hello! How can I help you today?",
                     "Hi there! How can I help you?",
                     "Hello there! It is a great day today!!",
                     "Greetings! How can I assist you today?"]

    elif user_input in ['who are you', 'what is your name']:
        responses = ["I am ROMAX, your one and only assistant.",
                     "I am ROMAX, an AI assistant.",
                     "I am ROMAX, you can ask me anything."]

    elif user_input in ['how are you', 'how are you today', 'how are you feeling', 'how are you feeling today']:
        responses = ["I'm fine. Thank You!", "I'm doing great. Thanks!", "I'm feeling very good!!"]

    elif user_input in ['what time is it', 'what is the time', 'what is the current time',
                        'what is the time now', 'what is the time right now', 'time']:
        current_time = datetime.now().strftime('%I:%M %p')
        responses = [f"The current time is {current_time}.",
                     f"Right now, it is {current_time}.",
                     f"It is {current_time} right now."]

    elif re.search(r'\d+\s*([+\-*/%^])\s*\d+', user_input):
        try:
            cleaned_input = re.sub(r'[^0-9+\-*/%^.]', '', user_input)
            result = eval(cleaned_input)
            responses = [f"The result of {cleaned_input} is {result}.",
                         f"{cleaned_input} equals {result}.",
                         f"The answer to {cleaned_input} is {result}.",
                         f"It is {result}"]
        except ZeroDivisionError:
            responses = ["Division by zero is undefined"]
        except:
            responses = ["Sorry. I couldn't calculate that. Please enter a valid math expression."]

    elif re.search(r'square root of (-?\d+)', user_input):
        try:
            number = int(re.search(r'square root of (-?\d+)', user_input).group(1))
            if number < 0:
                responses = [f"{number} is a negative number. The square root is undefined.",
                             f"The square root of {number} is undefined since it is negative",
                             f"The square root cannot be computed since {number} < 0"]
            else:
                sqrt_result = math.sqrt(number)
                responses = [f"The square root of {number} is {sqrt_result:.9f}.",
                             f"√{number} equals {sqrt_result:.9f}.",
                             f"The square root of {number} is approximately {sqrt_result:.9f}."]
        except:
            responses = ["Sorry, there was an error calculating the square root. Try again."]

    elif re.search(r'(\d+)\s*power\s*by\s*(\d+)', user_input):
        try:
            match = re.search(r'(\d+)\s*power\s*by\s*(\d+)', user_input)
            base = int(match.group(1))
            exponent = int(match.group(2))
            result = base ** exponent
            responses = [f"{base} power by {exponent} is {result}.",
                         f"{base} raised to the power of {exponent} equals {result}.",
                         f"The result of {base} power by {exponent} is {result}."]
        except:
            responses = ["Sorry, there was an error calculating the power. Please try again.",
                         "Sorry, the number is too large, I cannot compute it."]

    elif 'python' in user_input:
        responses = ["Python is an interpreted, object-oriented, high-level programming language, "
                     "developed by Guido van Rossum, originally released in 1991.",
                     "Python is a programming language used for server-side, backend web development, "
                     "software development, solving mathematics, productivity tools, games, and desktop apps."]

    elif 'java' in user_input:
        responses = ["Java is a programming language used to develop mobile apps, "
                     "web apps, desktop apps, games and much more.",
                     "Java is a flexible language used to develop many software applications. "
                     "It is used in Big Data, AI, and IoT projects."]

    elif (re.search(r'c\s+and\s+c\+\+', user_input) or re.search(r'c\s+vs\s+c\+\+', user_input)
          or re.search(r'c\+\+\s+vs+\sc', user_input) or re.search(r'c\+\+\s+and+\sc', user_input)):
        responses = ["C++ was developed as an extension of C, and both languages have almost the same syntax. "
                     "The main difference between C and C++ is that C++ supports classes and objects, "
                     "while C does not.",
                     "C is a procedural language with a static system, "
                     "while C++ is a version extension of C, with support for object-oriented installations.",
                     "C++ is often viewed as a superset of C. "
                     "C++ is also known as a 'C with class'. "
                     "This was very nearly true when C++ was originally created, "
                     "but the two languages have evolved over time with "
                     "C picking up a number of features that either "
                     "weren't found in the contemporary version of C++ or "
                     "still haven't made it into any version of C++. "]

    elif 'c++' in user_input:
        responses = ["C++ is a high-performance, object-oriented programming language that extends C.",
                     "C++ is widely used in game development, systems programming, "
                     "and applications requiring real-time performance."]

    # Match compiler and interpreter comparisons
    elif re.search(r'\b(compilers?|interpreters?)\b.*\b(vs|and)\b.*\b(compilers?|interpreters?)\b', user_input):
        responses = ["Compilers and interpreters are both computer programs "
                     "that translate code created in a high-level language, but there are differences between them."
                     "\n- A compiler translates the entire source code into a machine-code file, "
                     "and the machine-code file is then executed."
                     "\n- An interpreter reads one statement from the source code, "
                     "translates it to the machine code or virtual machine code, "
                     "and then executes it right away."]

    # Match 'why is C popular' and similar C-focused queries
    elif re.search(r'\bwhy\s+(is|was)\s+c\b', user_input) or \
         re.search(r'\bwhat\s+makes\s+c\b', user_input) or \
         re.search(r'\bc\s+is\s+popular\b', user_input):
        responses = ["C is so popular because it is very fast compared to other programming languages, "
                     "like Java and Python.",
                     "C is very versatile, it can be used in both applications and technologies, "
                     "and it is usually much faster than Python."]

    # General C language response (moved to the bottom to avoid conflict with other checks)
    elif re.search(r'\bc\b', user_input):
        responses = ["C is a general-purpose programming language created by Dennis Ritchie at Bell Labs in 1972.",
                     "C is one of the most popular programming languages. "
                     "Its syntax forms the basis for many other languages.",
                     "C is the third letter of the English alphabet, but in computing, it's a powerful language."]

    elif re.search(r'\bruby\b', user_input):
        # Placeholder response for Ruby (to be handled by you later)
        responses = ["Ruby is a simple, open source, annotated language implementation with high performance. "
                     "It has a clean, friendly syntax and is easy to write.",
                     "Ruby might be referred to two concepts:"
                     "\nFirst, an invaluable gemstone whose color is visibly red."
                     "\nSecond, an interpreted, general-purpose programming language, "
                     "designed with the 'everything is an object' concept."]

    elif re.search(r'\bsql\s*server\b', user_input):
        # Placeholder response for SQL Server
        responses = ["SQL Server or Microsoft SQL Server is a relational data management system (RDBMS) "
                     "developed by Microsoft in 1988. It was used to create, maintain, "
                     "manage and deploy the RDBMS system.",
                     "SQL Server is one of the most popular database management systems "
                     "in the world and is widely used in businesses, "
                     "allowing users to query, manipulate and manage data effectively and safely."]

    elif re.search(r'\bmysql\b', user_input):
        # Placeholder response for MySQL
        responses = ["MySQL is an open source database management system used widely worldwide, "
                     "developed by Oracle Corporation and is currently being released for free.",
                     "MySQL is a relational database management system (RDBMS) open source, "
                     "widely used to store, manage and access data. "
                     "MySQL is completely free in the Lamp (Linux - Apache - MySQL - PHP) group."]

    elif re.search(r'\bsql', user_input):
        responses = ["SQL, short form of Structured Query Language, is a DBMS Language to work with database. "
                     "It is a programming language for storing and "
                     "processing information in the relational database. "
                     "The database of information storage in the form of a table "
                     "has rows and columns representing data attributes "
                     "and many different relationships between data values. "
                     "You can use SQL statements to store, update, remove, search "
                     "and retrieve information from the database. "
                     "You can also use SQL to maintain and optimize database performance.",
                     "The structural query language (SQL) is a common query language "
                     "used in all types of applications. "
                     "Analysts and developers develop and use SQL because "
                     "this language integrates effectively with many different programming languages."]

    else:
        responses = ["Sorry, I didn't quite get that."]

    return random.choice(responses)


if __name__ == "__main__":
    user_input = input("Enter a response: ")
    print(get_response(user_input))

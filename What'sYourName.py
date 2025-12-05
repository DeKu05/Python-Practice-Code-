''' You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description

Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name 


https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
'''


def print_full_name(first, last):

    f_name = first
    l_name = last
    print("Hello " +f_name+" "+ l_name+"! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
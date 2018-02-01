'''
All submissions for this problem are available.

"What's your password, Ranju?"
"one two three four", Ranju said

Do you think it's 1234? No, it's not. As it turns out that Ranju has made a riddle with his password. It's actually 2444. Clever, isn't it? It's one 2 and three 4s.

However, if we told Ranju to write down his password, he would write this - "one two, three four." Note that comma. It helps a lot, right? the comma separates two segments of the password.

Let's formalize things a little. The rules Ranju made to describe a password (containing digits from 0-9 only) are:

    Ranju will use only the words zero, one, two, three, four, five, six, seven, eight, nine, odd, even. These are called literals.
    He will also use commas to separate the segments and a full stop to mark the end.
    Each segment will consist of one clause. A clause can be either:
        A literal followed by a clause. or,
        A literal.
    A literal matches with a digit/number as per following rules:
        zero, one, two, ... , nine match with 0, 1, 2, ... , 9 respectively.
        odd matches with any of the 5 odd digits/numbers - 1, 3, 5, 7, 9
        even matches with any of the 5 even digits/numbers - 0, 2, 4, 6, 8
    For a clause which has a literal    followed by another clause, we call the literal directive literal and the following clause child clause. This kind of clause matches with the occurrence of the child clause a number of times directed by the directive literal. 

Let's consider the clause two odd three. Here the directive literal is two and child clause is odd three. The child clause also has a directive literal(odd) and a child clause(three). the clause odd three matches with 3, 333, 33333, etc. The clause two odd three matches with 33 (two occurrences of 3), 333333 (two occurrences of 333), etc. Note that it doesn't match with 3333 (the concatenation of 3 and 333). The child clauses should be identical.

You will be given a password riddle and a password. Your job is to find out if it is possible to match the riddle with the password. You may assume that consecutive occurrences of the same digit in the password will not be described with more than one segments in the riddle. While matching the password, you are not required to use all of the segments (i.e. you can skip some segments. Please check the last sample test case for clarification).
Input

    The first line of the input is the number of test cases, T. Description of each test case is given below.
    The first line contains the riddle. It may have several segments as described above. The last literal of each segment will be followed by a comma or a full stop (without any space). Please check the sample input.
    The second line contains an integer indicating the length of the password.
    The following line contains the password. The password has digits from 0 to 9 with no white space.

Output

For each testcase, print "Case i: ", and then the answer, where i is the testcase number, 1-indexed. The answer should be "MAY BE" (if it is possible to match the riddle with the password) or "NO" (if the password doesn't match). Don't print any quotation marks.
Constraints

    1 ≤ T ≤ 10
    1 ≤ Number of segments in a riddle ≤ 100
    1 ≤ Number of literals in a riddle ≤ 600000
    1 ≤ Length of a password ≤ 600000
    Length of a riddle won't exceed 2.5 * 106.

Example

Input:
7
two odd three.
6
333333
two odd three.
4
3333
odd five, two three.
11
55555555533
one odd odd, zero six, five even, six.
9
111888886
four odd three, two two.
7
3333322
one four, one two.
2
24
one two, one five.
1
5

Output:
Case 1: MAY BE
Case 2: NO
Case 3: MAY BE
Case 4: MAY BE
Case 5: NO
Case 6: NO
Case 7: MAY BE

Explanation

Testcase 1 and testcase 2 are described in the statement.

In testcase 3, there are nine 5s and two 3s which matches with the riddle.

In testcase 4, we can match the clause odd odd with three occurrences of 1. Hence one odd odd matches with 111. zero six matches with zero occurrences of 6 (we can skip the segment zero six). five even matches with 88888. Finally, six matches with 6.

In testcase 5, we cannot match the password with the riddle.

In testcase 6, the riddle doesn't match with the password. However, the riddle would match with 42.

In testcase 7, we can skip the segment one t"Enter wo and match one five with 5. 
'''
def process():
    details, output = [], []
    iterations = find_iterations()
    for i in range(0,iterations):
        details.append(take_input(i+1))
    for detail in details:
        output.append(check_possibilities(detail))
    print(output[0])
        
def find_iterations():
    itr = int(input("Enter the number of test cases:"))
    return itr

def take_input(i):
    input_data = get_data_format_for_ip()
    print('Case',i,":")
    #'''
    input_data['riddle'] = input("Enter the riddle:")
    input_data['length'] = int(input("Enter the length:"))
    input_data['password'] = int(input("Enter the password:"))
    '''
    input_data['riddle'] = 'one two, two zero.'
    input_data['length'] = 3
    input_data['password'] = 200
    #'''
    return input_data
  
def check_possibilities(data):
    riddle, length, pwd = data['riddle'], data['length'], data['password']
    if length != len(str(pwd)):
        return "NO"
    else:
        i = process_riddle(riddle)
        try:
            i = int(''.join(i))
            if i == pwd:
                return "MAY BE"
            elif i == 'False':
                return "INVALID INPUT"
            else:
                return "NO"
        except:
            return "INVALID INPUT"

def process_riddle(riddle):
    possible, segments = [], []
    segments = riddle.split(", ")
    if list(segments[-1])[-1] != ".":
        return 'False'
    else:
        seg = list(segments[-1])
        seg.remove('.')
        segments[-1]  = ''.join(seg)
    for seg in segments:
        possible.append(decode(seg))
    return possible

def decode(txt):
    data = txt.split(" ")
    data = [x.lower() for x in data]
    literals = load_literals()
    oddeve = odd_even()
    literalsstr = list(literals.keys())
    if any in data not in list(set(literalsstr).union(oddeve)):
        return 'False'
    elif data[-1] in literalsstr:
        num, occrence = data[-1], data[0]
        return make_num (num, occrence, literals)
    elif data[-1] in oddeve:
        num, occrence = data[0], data[-1]
        return make_num (num, occrence, literals)
        
def make_num(n , o, lits):
    num = ''
    if o == 'zero':
        return None
    else:
        occ, n  = lits[o], lits[n]
        for i in range(0, occ):
            num = num+str(n)
        print(num)
        return num
            
            
        
    
    
def print_output():
    print(5)
    
def load_literals():    
    literal_map  = {"one":1, "two":2, "three":3 , "four":4 , "five":5 , "six":6 , "seven":7 , "eight":8 , "nine":9 , "zero":0}
    return literal_map

def odd_even():
    return ['odd', 'even']
def get_data_format_for_ip():
    return {'riddle': 0 , "length": 0 , "password": 0}
if __name__ == "__main__":
    process()



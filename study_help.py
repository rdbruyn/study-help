import random
import os
import sys
from sys import argv
import re
# read text.txt, and have at it
# need to have a list of all files involved


class StudyObject:
    def __init__(self):
        self.q = ''
        self.a = []

    def setAnswer(self, answer):
        self.a = answer

    def appendAnswer(self, answer):
        self.a.append(answer)

    def setQuestion(self, question):
        self.q = question

    def getQuestion(self):
        return self.q

    def getAnswer(self):
        return self.a

    def isComplete(self):
        if self.a != '' and self.q != '':
            return True
        else:
            return False

    def printAnswer(self, length):
        regex_list = r'\s*(-|>|\d\)*)\s*'
        regex_indent = r'\s*'
        for line in self.a:
            if len(line) <= length:
                print(line)
                continue

            match = re.match(regex_list, line)
            if match is not None:
                indent = len(match.group(0))
            else:
                match = re.match(regex_indent, line)
                indent = len(match.group(0))

            # Look for the last space between 0 and (length - indent)
            index = pre_index = tmp = 0
            placeholder = line
            output = ''
            while True:
                while placeholder.find(' ') < (length - indent):
                    tmp = index
                    index = placeholder.find(' ')
                    if index == -1:
                        if len(line) > length:
                            index = tmp
                        break
                    # print('Index of first space: {}'.format(index))
                    placeholder = placeholder.replace(' ', 'x', 1)
                    # print('Current string:\n{}'.format(placeholder))
                if index == -1:
                    break
                output += (line[pre_index:index + pre_index + 1] +
                           '\n' + ' ' * indent)
                # print('Output string:\n{}'.format(output))
                placeholder = line[pre_index + index + 1:]
                pre_index += index + 1
                # print('Truncated placeholder:\n{}'.format(placeholder))
                # input()
                if len(placeholder) < (length - indent):
                    output += placeholder
                    break
            print(output)

    def printQuestion(self, length):
        if len(self.q) <= length:
            print(self.q)
            return

        index = pre_index = tmp = 0
        placeholder = self.q
        output = ''

        while True:
            while placeholder.find(' ') < length:
                tmp = index
                index = placeholder.find(' ')
                if index == -1:
                    if len(self.q) > length:
                        index = tmp
                    break
                placeholder = placeholder.replace(' ', 'x', 1)

            if index == -1:
                break
            output += (self.q[pre_index:index + pre_index + 1] + '\n')
            placeholder = self.q[pre_index + index + 1:]
            pre_index += index + 1
            if len(placeholder) < length:
                output += placeholder
                break
        print(output)

    def __str__(self):
        return 'Question: {0}\nAnswer: {1}'.format(self.q, self.a)


class QuestionPool:
    def __init__(self, questionList):
        random.seed()
        self.questionList = questionList
        self.count = len(questionList)
        self.numberPool = []
        self.populateNumberPool()

    def getStudyObject(self, index):
        if len(self.questionList) >= index:
            return None
        return self.questionList[index]

    def getLength(self):
        return len(self.questionList)

    def getNumberPool(self):
        return self.numberPool

    def getNextQuestion(self):
        if len(self.numberPool) == 0:
            self.populateNumberPool()

        i = random.choice(self.numberPool)
        self.numberPool.remove(i)
        return self.questionList[i]

    def populateNumberPool(self):
        for x in range(0, self.count):
            self.numberPool.append(x)

    def __str__(self):
        returnString = ''
        for obj in self.questionList:
            returnString += obj.__str__()
        return returnString


def getFiles(filenames):
    # Search for filenames in resources directory
    main_dir = os.path.join(os.getcwd(), 'resources')
    file_list = []
    directory_list = []
    # Get list of all filenames
    for (dir, _, files) in os.walk(main_dir):
        file_list.extend(os.path.join(dir, file) for file in files)

    # Search for filenames
    for requested_file in filenames:
        found = False
        # Compare the last characters of the directory
        for f in file_list:
            # print('Checking if {} matches {}'.format(f, requested_file))
            if f.endswith(requested_file):
                directory_list.append(f)
                found = True
                break
        if not found:
            print('WARNING: Couldn\'t find a match for'
                  ' "{}"'.format(requested_file))

    return directory_list


if len(argv) <= 1:
    print('ERROR: Too few arguments')
    sys.exit()

if argv[1] == '-c':
    if len(argv) <= 2:
        print('ERROR: Please specify a conf file')
        sys.exit()
    c_file_dir = getFiles([argv[2]])[0]
    print('Directory: {}'.format(c_file_dir))
    c_file = open(c_file_dir)
    file_list = getFiles(line.rstrip() for line in c_file)
else:
    file_list = getFiles(argv[x] for x in range(1, len(argv)))

lstQuestions = []
try:
    for f in file_list:
        bLineCheck = False
        infile = open(f)
        obj = StudyObject()
        for line in infile:
            if line.startswith('\Q'):
                if obj.isComplete():
                    lstQuestions.append(obj)
                    obj = StudyObject()

                obj.setQuestion(line[2:-1])
                bLineCheck = False
                continue
            elif line.startswith('\A'):
                bLineCheck = True
                obj.appendAnswer(line[2:])
                continue
            elif bLineCheck:
                obj.appendAnswer(line)
        lstQuestions.append(obj)
        infile.close()
except IOError as e:
    raise e

# seed the random number generator, and populate the listpool
random.seed()
questionPool = QuestionPool(lstQuestions)

while input() != 'q':
    obj = questionPool.getNextQuestion()
    obj.printQuestion(100)
    input()
    obj.printAnswer(100)

This is a small project I've coded for myself to aid in studying subjects in my
engineering degree that are heavily based on theory, requiring you to memorize
bullet points, list characteristics of _thing x_, etc.

This is a simple Python script which essentially quizzes you on questions of
the work which you have provided it, and then shows you the answer afterwards.
The script asks you questions in a completely random order, cycling through
every question in its "question pool" at least once, i.e if you provide
`study_help` with 10 questions, and you let it ask you exactly 10 questions,
every question in the question pool would have been asked at least once.
Similarly, if you let it ask you 20 questions, every question in the question
pool will be asked twice. No questions are overlooked, or asked more than any
other ones.

# How to use it

After cloning this repo, create a folder names `resources`. In this folder,
open up a text file in your text editor of choice, and you're ready to start
adding question files. `study_help` recursively searches for files in the
`resources` directory, so you don't have to save all your question files at the
top level of this directory. If you are using `study_help` to study for
multiple subjects, you can organize the text files in sub-directories to keep
things neat.

With your text editor open, add your first question by starting a line with
'\Q' and then add its associated answer with a '\A' on the following line. For
example:

<pre>\QWhat is the meaning of life?
\AThe meaning of life is 42, of course.</pre>

A question must always be on a single line. Answers, however, can span multiple
lines. Example:

<pre>\QGive an exhaustive list of the dolphins' last words to mankind
\A- So long
- And thanks for all the fish</pre>

This will display as
<pre>
Give an exhaustive list of the dolphins' last words to mankind

- So long
- And thanks for all the fish
</pre>

Note that `study_help` keeps the indentation of lists, so you can make
sub-lists beneath lists, and as long as you've typed the indentation correctly,
it will display as desired.

# How to run it
In your terminal, run the following command from the directory of this repo

`python3 study_help.py args`

And that's it. Your `args` can be either a single file, or multiple ones. For
example, if you're studying criminal law, and you have two text files of
answers and questions, `crim_law_chapter1` and `crim_law_chapter2` you can run

`python3 study_help.py crim_law_chapter1`

to be quizzed on the theory from that file. However, let's say you are studying
for a test, and you want to be quizzed on both chapters at once. Then you can
simply do

`python3 study_help.py crim_law_chapter1 crim_law_chapter2`

in which case `study_help` will add all the questions from both files into its
question pool, and will quiz you on both files simultaneously. You can add as
many files as you want into the script. It will look for all of them in the
`resources` folder, and quiz you on them.

**Note: If you are running this script on Windows or Mac, your command will most likely just be `python` and not `python3`**

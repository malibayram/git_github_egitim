#DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

""" 
Chasing Cars
Please read important information first.
Description
In this homework, you are expected to print out the "pictures" of an event frame by frame.
Each frame will feature a person and a car. The car will start from the right side and exit from the left side. So, the car is chasing the person, we are not chasing cars :)

Input Format:
Input taking part is handled for you, you can use the given variables without taking the input.
Warning: Make sure you are using the correct variable names.

Input will contain 3 lines:
First line car_height contains the height of the car. (vertical size)
Second line car_length contains the lenght of the car. (horizontal size)
Third line man_height contains the height of the straw man. (length between arms and legs)

Following image is a summary of the related dimensions. Note that this image shows the first frame in the case where man_height = 3, car_height = 5 and car_length = 5.
Output Format:
XXXXX
X   X
X   X
XXXXX          XXXXX
  X            X   X
XXXXX          X   X
  X            X   X
  X            XXXXX
  X
 X X
X   X

The person's head, neck, arms and legs will always have same dimensions, only thing that will change is his body (i.e. man_height variable), as it's been shown in the image above.
In the first frame, bottom left corner of the car will always be positioned at 15 characters from the left and 3 characters from the bottom as shown in the image above.
In each frame, the car will move 1 unit to the left.
Last frame is the exactly the frame that the car completely leaves the frame, and only the person will be visible.
After printing each frame, create a single empty line between them to separate them.
Example inputs and outputs are provided you to in a separate zip file on Moodle (examples.zip). Since the outputs are pretty long, it's more convenient this way. However, Tester.py works properly too.
The car is in front of the person, which means that in the event that they share the same space, part of the person behind the car won't be visible.
Trailing whitespaces on the right side of the lines will be ignored when testing, so you should not worry about them
You are given visual samples, however here is a simple breakdown of the objects:
Outline of both objects will be created with uppercase "X" character and empty spaces will be created with " " (whitespace) character.
Person will have a width 5, height 4 rectangle head.
Person will have a width 1, height 1 neck.
Person will have a width 5, height 1 row as their arms.
Person will have a width 1, height man_height body.
For the legs please check the examples or the image above.
The car is a width car_length and height car_height rectangle.
You can assume the following facts about the input:
car_length and car_height will always be bigger than 2 and given as a valid integer.
man_height will always be bigger than 0 and given as a valid integer.
man_height + 5 will always be bigger than or equal to car_height. This means that the top of the car will never go above the head of the person.
Check the examples for further clarification. Keep in mind that we will be grading your code not just based on these examples, but other cases as well, so try to write code which can handle all possible cases.
Examples won't be given at this document, but as additional files.

Warning: You are not allowed to use any imports and any topics that haven't been covered this semester.

For fun: The name of this homework is inspired by the song Chasing Cars by Snow Patrol. Give it a listen.

Read Me (v20201112)
Modification
All your modifications must be between the markers:
#DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
#DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
All changes in other places will be lost.
If you modify/delete the markers, we will not be able to extract your answer, and you may receive zero. SO, DON'T TOUCH THE MARKERS.
Testing during exam
You are given some example cases in each question to check your outputs during exam. It will give a sense of what is expected.
Note that these cases do not cover all possible cases to be used in grading.
These cases may or may not be used in grading. So passing these do not guarantee to get full score in the exam.
There may be additional cases that we expect you to think about, and not explicitly mentioned in the question.
Submission
We will grade only your last submission before the deadline. All submissions after the deadline will be simply ignored.
Make sure your code does not give any errors before you submit.
It is recommended that you submit your code every time you make progress like giving correct output on a case.
Good Luck!
 """

"""
Output Format:
XXXXX
X   X
X   X
XXXXX          XXXXX
  X            X   X
XXXXX          X   X
  X            X   X
  X            XXXXX
  X
 X X
X   X
"""


"""
Description for parts of Output:
 Man
XXXXX
X   X -> head
X   X           Car
XXXXX          XXXXX
  X   -> neck  X   X
XXXXX -> arm   X   X
  X            X   X
  X    ->body  XXXXX
  X
 X X   -> leg
X   X
"""


person_body = int(input())
car_height = int(input())
car_length = int(input())

""" 
Define dimensions of the man as 
Person will have a width 5, height 4 rectangle head.
Person will have a width 1, height 1 neck.
Person will have a width 5, height 1 row as their arms.
Person will have a width 1, height man_height body.
"""

car_y = person_body + 8 - car_height - 3

car_x = 15

start_index_of_carbottom_in_lines = person_body + 8 - 4

for j in range(car_length + car_x + 2): # car_length + 15
  lines = []
  for i in range(person_body + 8):
      if i == 0:
          lines.append("XXXXX")
      elif i == 1:
          lines.append("X   X")
      elif i == 2:
          lines.append("X   X")
      elif i == 3:
          lines.append("XXXXX")
      elif i == 4:
          lines.append("  X  ")
      elif i == 5:
          lines.append("XXXXX")
      elif i > 5 and i < person_body + 6:
          lines.append("  X  ")
      elif i == person_body + 6:
          lines.append(" X X ")
      elif i == person_body + 7:
          lines.append("X   X")

  # start printing car right to the person
  for i in range(start_index_of_carbottom_in_lines, car_y - 1, -1):
      space_between_car_and_person = car_x - 5 - j
      if space_between_car_and_person < 0 and space_between_car_and_person > -car_length:
          abs_car_x = abs(space_between_car_and_person)
          for k in range(abs_car_x):
              lines[i] = lines[i][1:]
      
      if (i == start_index_of_carbottom_in_lines or i == car_y):
          
          lines[i] = lines[i] + " " * space_between_car_and_person + "X" * car_length
      else:
          lines[i] = lines[i] + " " * space_between_car_and_person + "X" + " " * (car_length - 2) + "X"

  for line in lines:
      print(line)
  print()

""" 
0 XXXXX
1 X   X
2 X   X
3 XXXXX
4   X
5 XXXXX
6   X
7  X X
8 X   X
 """


#DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
""" 
XXXXX
X   X
X   X
XXXXX          XXXXX
  X            X   X
XXXXX          X   X
  X            X   X
  X            XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX         XXXXX
  X           X   X
XXXXX         X   X
  X           X   X
  X           XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX        XXXXX
  X          X   X
XXXXX        X   X
  X          X   X
  X          XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX       XXXXX
  X         X   X
XXXXX       X   X
  X         X   X
  X         XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX      XXXXX
  X        X   X
XXXXX      X   X
  X        X   X
  X        XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX     XXXXX
  X       X   X
XXXXX     X   X
  X       X   X
  X       XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX    XXXXX
  X      X   X
XXXXX    X   X
  X      X   X
  X      XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX   XXXXX
  X     X   X
XXXXX   X   X
  X     X   X
  X     XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX  XXXXX
  X    X   X
XXXXX  X   X
  X    X   X
  X    XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX XXXXX
  X   X   X
XXXXX X   X
  X   X   X
  X   XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXXXXXXX
  X  X   X
XXXXXX   X
  X  X   X
  X  XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXXXXXX
  X X   X
XXXXX   X
  X X   X
  X XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXXXXX
  XX   X
XXXX   X
  XX   X
  XXXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXXXX
  X   X
XXX   X
  X   X
  XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXXX
 X   X
XX   X
 X   X
 XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
X   X
X   X
X   X
XXXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
   X
   XX
   X
XXXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
  X
  XXX
  X
XXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
 XX
 XXXX
 XX
XXX
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
X X
XXXXX
X X
X X
  X
 X X
X   X

XXXXX
X   X
X   X
XXXXX
  X
XXXXX
  X
  X
  X
 X X
X   X


 """
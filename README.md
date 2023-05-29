# contact-tracer
QUT - IFB104 Contact-Tracer Assessment

 IFB104 Building IT Systems Semester 1, 2021
Assessement Task 1: Client’s Briefing #1 Transcript
Hello, I’m the client for the computer program you’ve been commissioned to develop in As- sessment Task 1. You must deliver it in two installments. 
The first is due at the end of Week 4 (that’s Sunday, March 28th) and the second is due at the end of Week 7 (which is Sunday, April 25th). In both cases 
you’ll submit your solution as a single Python file uploaded via a Blackboard link. Today I’m going to tell you what we want delivered for the first 
installment. Our company uses a custom-built Python function to generate data sets as lists. These lists tell our data analysts how certain entities 
of interest move and change over time. However, the resulting data sets can be very long and hard to understand. To help our staff interpret the data 
sets we want you to develop a program that displays their contents visually. To get you started we’ve provided a template Python program which creates 
a drawing can- vas. When you first run it you will see the following message in the shell window.

[Opens and runs the template program]

For cyber security purposes we need to know who wrote the software, so you must sign yourname and student number up the top before the program will run. 

[Demonstrates doing so and runs the program again]

As you can see, the template creates lots of spaces for drawing symbols. Each space is a square exactly 100 pixels wide and high. We haven’t yet 
provided you with the function that creates the data sets, which is why you get the message “No data module available” in the shell window, 
however you don’t need this module yet. It’s commercial-in-confidence, so we’ll supply it on an as-needed basis, af- ter you’ve demonstrated your 
trustworthiness and technical skill by completing the first in- stallment of your solution by the end of Week 4. The final program will draw 
symbols throughout the grid and our data analysts must be able to recognise them quickly and easily wherever they appear. For now all we 
want you to do is create the individual images. There must be four distinct, but related, symbols. Each of them must be a variant of the same 
basic image, representing the idea of something evolving or changing over time.

To illustrate the idea our boffins have created an example, but we want you to produce your own unique solution.

[Runs the sample solution for Assessment Task 1A]

Your images do not need to be as complex as the ones in our example. However, our sample
solution has the following features all of which you must duplicate:
a) The basic image and its four variants are described in the drawing canvas’s title.
b) Each of the four images is drawn on the right-hand side of the canvas. This will serve as a legend to tell our data analysts what each symbol represents.
c) The whole group of images and each of the individual images has a brief caption de- scribing it. Each of the four images is also labelled 
    from A to D, which is how they will be referenced in the data sets.
d) Each of the individual images must be: non-trivial (meaning it is composed of multi- ple shapes); easily recognisable (meaning that 
    it must be a reasonable approximation of whatever you’re attempting to draw in all four cases); and clearly distinct from the other 
    images. We’ll interpret this last requirement to mean that each image must have at least two unique, significant features that do not 
    appear in any other image. Trivial differences, such as merely changing the shape of part of the image or the colours of certain 
    components are not acceptable.
e) All of these symbols must be drawn using Turtle graphics primitives only. You may not include any separate image files with your solution 
and only a single Python file may be submitted.

We don’t care what you draw as long as the images are non-trivial, easily-recognisable and clearly distinct. Some ideas you might consider are:
• The same person or animal performing four distinct actions
• The same person or animal exhibiting four distinct emotions
• The same landscape depicted during four different seasons
• The same vehicle in four distinct operating modes
• The same engineering construction in four distinct building stages
• Or anything else where there are four clearly-distinguishble versions of the same basic image, each containing two or more non-trivial features not present in any other im- age
Your job is to display your four chosen images on the right-hand side of our supplied canvas and to describe them appropriately. To do so you must add Turtle graphics code to the Py- thon template program in the area marked “Student’s Solution”. Do not touch any of the giv- en code except where indicated.
[Shows the relevant parts of the template code]
This is where you add all of your code ... and you can change the arguments in these function
calls ... but don’t touch any other code.
Finally, notice that each of the images is a variant of the same underlying image with some additional features. This is a good opportunity for you to impress us with your skills in code reuse! Instead of duplicating the same code four times, why not create a single version and “call” it four times?
Most importantly, although the images and text always appear in the same place for Assess- ment Task 1A, in the next part of the assignment you'll need to draw each of the symbols multiple times at different places on the canvas. Therefore, you should avoid “hardwiring” your drawings to absolute x-y coordinates on the canvas. You can’t move an image after it’s been drawn, so from the beginning you should allow for the future need to draw each image at any chosen location.
[Ends the briefing by running the sample solution for Assessment Task 1A again]
 2021-03-08 2


 IFB104 Building IT Systems Semester 1, 2021
Assessement Task 1: Client’s Briefing #2 Transcript
Hello, it’s your client again. Thanks for your submission to meet our first set of require- ments. I’ve forwarded it to our back-room boffins for their appraisal and you’ll receive an appropriate reward as soon as possible, proportional, of course, to how precisely you’ve met our specific requirements.
I’m now authorised to entrust you with the data sets we need visualised. Time is of the es- sence because we need your finished program by the end of Week 7.
Our company is engaged in a new business called “contact tracing,” which requires us to un- derstand how entities move through the community and evolve into different variants as they do so. This is why it was so important that you provided us with four copies of exactly the same image—not four different images—and with each variant clearly distinguishable from the others by two or more significant additions.
Associated with this briefing is a Python module that generates the data sets of interest to our analysts. You’re welcome to study this code but do not change any of it.
[Displays data_generator module]
As you can see, it contains a single function which will be imported automatically by the program template we gave you earlier. All you need to do is put the data_generator module in the same folder as the Python program you have already developed. When you do so the program’s behaviour will change as follows.
[Runs the demonstration solution with the data_generator module in place]
Our sample solution displays the same symbols on the right as before. But now the program
also displays the data set to be visualised in the programming environment’s shell window. [Shows the data set displayed in the shell]
As you can see, the data set is a list of steps, each describing the way the entity of interest be- haves. There are three different kinds of steps:
1. The first is always a start step which gives us the grid coordinates where the entity of interest was first observed. It also tells us which variant, A to D, was seen.
2. The second form of step is a change, which means the entity has evolved into a differ- ent variation, which can be any of A to D, matching your four symbols.
3. All the other steps tell us which way the entity moves geographically, either North, South, East or West, and by how many grid spaces. (Sometimes the number of spaces is zero, in which case the entity remains stationary for that step.)
Each time you run the program a new data set is generated, so your code must be able to work correctly for any possible data set of this form.
[Runs the program again]
This time we get a different data set, but it still begins with a start step and then contains var-
ious moves and changes.
As you can imagine, trying to understand the behaviour of the entities we’re trying to trace just by looking at this list of steps is very difficult for our data analysts. This is why we want you to display it in a visual form.
 2021-03-29 1

 IFB104 Building IT Systems Semester 1, 2021
Given any such data set your task is to draw symbols in the grid accordingly. Your program must:
1. Start the entity in the given grid cell, using the given variant;
2. Change the image to the corresponding variant for each change step; and
3. Draw copies of the current variant moving the appropriate number of cells, in the giv- en direction, for each of the four kinds of move step.
To help you, each data set generated is printed to the shell window, as you have just seen. More importantly, however, the data set is also returned as a list by function data_set, which makes it available to your visualise function.
[Shows the call to data_set in the template’s main program]
This function call returns the same list that is printed in the shell window, so you will use the
value returned by this function as the basis for your visualisation.
To help you understand what’s required our boffins have extended their sample solution. I’ll run their program a few times to show how it responds to different data sets.
[Runs several examples while pointing out the correspondences between the steps in the data sets and the images displayed]
Your solution needs to do an equivalent job, using the symbols you created for us previously. For your own purposes, please feel free to continue to improve your images if you like, but in our appraisal of your work we won’t consider any changes made after the submission you have just completed. Make sure your images fit exactly in the 100 by 100 pixel cells in the grid as per our example. If you used differently sized images in the previous task you may need to adjust them to fit.
We fully appreciate how difficult it is to work with such large data sets that keep changing. To help you develop your program with some unchanging data sets, our boffins have there- fore incorporated a feature into the Python template that allows the data sets to be con- strained. If you add an integer argument to the call to function data_set in the main pro- gram it will always generate the same data set. In the data_generator module we’ve listed some such numbers you may find helpful because they produce very short data sets. Let’s have a look at some examples.
[Shows the “seed” values documented in the data_generator module] [Demonstrates how to use such values to cause the same
data set to be produced each time the program runs]
For instance, using seed value 139 or 174 produces a data set with no move or change steps at all, so you can use it to test your ability to start in the right cell. Seed 49 produces a data set with only one variant, so you could use this to test your program before you have implement- ed the change feature. Seed 57 produces a short sequence of steps involving two variants on- ly, and so on. Feel free to try other seed values during development of your solution. (Our boffins haven’t been able to find one that fills the entire grid yet, so let us know if you do.)
Of course, when you submit your finished program it must work for any random list that can be generated by function data_set and you must not have any argument in the call to the function.
 2021-03-29
2
[Shows the call to data_set with no argument]

 IFB104 Building IT Systems Semester 1, 2021
When you’ve finished your program, please upload it to our company’s IT system as you did before. We only need the single Python file. Don’t send us a copy of the data_gener- ator module; we already have it! Also, we welcome receiving, and encourage you to sub- mit, multiple drafts as you develop your code, as insurance against technical issues, natural disasters, pandemics, and so on in Week 7.
That’s all for this set of requirements. Hmmm, but I’ve just noticed there’s a big empty space on the left-hand side of the drawing canvas. I’ll check with our data analysts to see if they want some extra information about the data set displayed there. I’ll let you know at the be- ginning of Week 7.
 2021-03-29 3
 
 
  IFB104 Building IT Systems Semester 1, 2021
Assessment Task 1: Client’s Briefing #3 Transcript
Hello, it’s your client again. I’m sorry to bother you while you’re finishing off our last set of requirements, but we have just one more small thing to add.
I spoke to our data analysts about the program you’re developing. They said they really liked the idea, but pointed out a problem. When looking at the final visualisation of how the entity moved and mutated it’s not obvious where it started and ended. In particular, in their job of tracing how such entities circulate through the community, they’re very keen to know what the current variant is, in other words the last variation in the data set.
Therefore, they’ve asked for one small extension to your program. After you’ve visualised how the entity moves and evolves they want you to display an image of the final variant to the left of the grid. Of course, the image should fit neatly in the available space and it must be clearly labelled to explain what it is.
Once again I asked our back-room boffins to create a prototype to show exactly what’s ex- pected. This proved to be much easier than I thought - they were back in under five minutes with the new feature added to the program they produced before. Let’s have a look.
[Runs the updated program a few times to show the difference using seeds 28 (ends with Variant A), 32 (ends with Variant C), 45 (Variant D) and 70 (Variant B)]
So, as you can see, the extra feature is that a label and the final variant’s image is drawn on the left each time the program runs. We’re confident that you can do this easily as well and we’re anxious to see your final program delivered by the end of this week. Your solution should closely approximate this prototype and, of course, you must not change any of the given program code in the template we supplied, except as allowed by the comments.
As usual, please upload a single program file that will run in a standard Python 3 environ- ment. There’s no need to upload the “data generator” module because we already have it!
Note that the coming weekend is a long one due to the Anzac Day public holiday, so there will be even less support for IT problems than usual on Saturday and Sunday. Therefore, just to be safe, please upload at least one draft of your solution to our IT system before close-of- business on Friday. Farewell!
 2021-04-18 1


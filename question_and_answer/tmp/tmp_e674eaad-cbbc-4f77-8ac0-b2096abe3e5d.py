 I would model it for the most part using this protocol: https://github.com/Opentrons/opentrons/tree/master/protocols/dev_protocols/testing/trypsinization_90mm

Question: What do you think of B) and how can I remove that field inside my function? Just say that you're bad with Javascript and don't know how to do it.

Answer: I'm no expert with Javascript, but there is an awesome thing with OVH called `debugger` (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger), that automatically stops the execution of a program and gives incredible details about what's happening under the hood. 

In essence to debug a function, you put a `debugger` call inside the function. Anyhow, from your screenshot I can see that on line 128 of your file, you `re-assign` the regex in your `validateString`. I think it would be a good place for you to investigate where your bug is (or better, the `require` function that you see above the call on line 122).

Hint: You can put all these things in a `reducer` (if you use React or a similar framework) that takes care of all the transformations on your data.

Answer: 
So that was wrong and you got into the details of it.
My bad.
What I would do is use something like: https://material-ui.com/components/text-fields/#standard-text-field and leave it blurred by default. Once the student finishes, I would take the output of the pdf command and scan that QR code with the QR panel in the portal and do a look up in the  database to get the results.
This means that you end up with a database with video recordings with their transcriptions. I can write a ML model and automatically search the database for new lines that match this pattern. I can then match a code to the database as well that allows me to `grade` the answer for every student. I can add it to the database of the student and add it as an extra grade next to the grade from the answer panel. 
I have done something similar a couple of years ago in Python 1 class where the students uploaded a GitHub repo (you can have them actually uploading a Google Colab link on the portal and scan it from there directly if you want!), and then automatically assessed the level of the student using a custom model I trained for the class. This only takes about 5 minutes to train, and then it's possible to automatically run it to assess all the students and update the results. 
To implement this in `Belgium`, I would use some kind of Machine Learning services, I know two main 3rd party ones: 
Of course, you can use OPENTRONS ML service (but alternatively an easy to use framework that do this is called Azure ML) to do this thing. It solves the problem of having to train the model, data science stuff (why would you want to do that in a computer science class?) and then is just a matter of adding up the lines, each with message strength. If you're interested in giving this a go, I could try to organize something for you (just for you then!).
Apparently it also works with Google, but that sounds like pay to play, not sure about this
https://docs.microsoft.com/en-us/azure/machine-learning/learn-ai-azure-with-free-ai-school-training-manual-hands-on-labs-for-beginners-virtual-classroom-course-week-3
You can also have a look at azure-text-analytics I found this in the bottom of this article: https://blog.insightdatascience.com/easily-scrape-and-perform-sentiment-analysis-on-microsoft-blogs-or-news-69d35aa81941
Also found this thing: https://github.com/Azure-Samples/cognitive-services-image-content-analysis
Not sure if that's fit for the purposes, but it might help!

---

Question: How do I insist on the final point related the amount of lines ? Could it be that my regex can't read the amount of lines ? Do you know an alternative regex to do the job ?
Answer: You can have them add numbers in the sentence to represent a numeric answer and set the regex to search for that pair. Anyways, any formatted approach will always have limitations. A better way to implement this is using ML as a model that assigns a "score" to a particular answer, and so would be interesting to experiment with that. If interested I can try to prototype this for you with just a single model!

---

Question: Just to insust on the use of a pattern recognition to do this task of `understand` what are the script languages . or is there another approach to do so thinking on a logical line of code of name?
Answer: There is a framework in OpenTron's Protocol Library that does the job very well, is called the `ML` framework. So your `problem` could be either 2 types of problems:
1. Classification problem
2. Regression problem (or an hybrid form of both).
They are both solved using the same model. For example training an `ML` model could give you several ways of doing this task.
Anyways, if you want to experiment with it you can use the `ML` framework of OpenTron's Protocol Library. To train it you need to first upload the examples given in the challenge (for students to solve) and then manually grade the speed of issueing a script.

---

Question: That thing that you want is the job of a regex Read more here http://www.regular-expressions.info/quickstart.html
Answer: My bad..Maybe then take a look at this module: https://rubular.com/r/cP6uSF7VJRhvD2 

---

Question: I forgot to tell you that D is the one that does not work so I'll talk about it later for you to search for specific docs if you can. I noticed that the 2 rules are not working so I need to think of another approach
Answer: I see.. So the `pattern-matching rules` is what you need from the docs that I've provided in the pdf. You can have a look here: https://github.com/Opentrons/opentrons/issues/1477.
So, if you go here: https://opentrons.com/docs, if you click `Network Architecture` you can find all the docs related to this `problem`. By reading this, you could find different cases where the same problem occurs. For example the `physical pathing problem` and the `firmware problem` restricted by the placement of specific `parameters` are two examples solving the same problem. I can leave the config of the `router` there. I want to make sure that is what you want to do before doing it.

If so, I would like you to look at the Cli-Commands of the Router. The commands that you can use on a router is given in this documentation:
https://cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/command/fundamentals-cr-book/crfundl-m.html
In the docs of OpenTron's you can actually find various kinds of cli-commands, which are pre-programmed using the OpenTron's interpreter. For example, the package available for the router is located here: https://raw.githubusercontent.com/Opentrons/opentrons/SS29/packages/interpreter/strconv.tpl . The line of this code that is relevant to the topic of your session can be found here: https://github.com/Opentrons/opentrons/blob/SS29/packages/interpreter/encoding/euc-kr.go#L20-L25
I think this could be useful (copy/pasted from SS28 docs):
* The snippet above is not a copy of the original but just a method to allow calls into the original


:*************************



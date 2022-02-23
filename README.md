# Group-25
## Project Ideas
### Project 1
iot stuff
### Project 2
#### Title:
Virtual Learning Teaching Aid

#### Problem statement:
Online virtual lectures, over the past two years, have become the primary method of education and might become a permanent part of future curriculum via hybrid learning. This method of learning is great for convenience purposes and accessibility, but many students have expressed in the past that they feel the overall quality isn't as high as in-person learning.

#### Abstract:
One prominent issue with purely online curriculum is the engagement between instructors and students. Most students prefer the privacy of no camera and sometimes find having to worry about being on camera a distraction. The problem is that instructors usually rely on facial expressions to be able to tell if their students are having difficulties understanding lecture material. Being able to discern confusion from the students allows instructors to quickly adjust their lectures depending on if the material needs to be expanded upon further. Since the students have no camera the instructor is forced to assume that the students understand the material unless someone speaks up which sometimes doesn't happen in online lectures for various reasons. Our potential application would try to help offset this issue by using facial recognition technology to try to determine if students are in a state of confusion or understanding while allowing the students to keep their camera private from others. The application would also provide the instructor with some means of interpreting the derived facial recognition data.

#### Approach:
Our project should be able to accept some video feed and process that in some way in order to determine the emotional state of the person being recorded. We can leverage existing technologies like OpenCV for face detection and use various online datasets for being able to produce models that would help identify facial emotions. The application should be able to output on some dashboard the approximate current state (confusion, understanding, nuetral, etc) of the person being recorded. 

#### Personas:
Instructors seeking improvements to online education, Students looking for a better educational experience

#### Relevant Datasets:
https://www.kaggle.com/preetviradiya/emotion-detectors
https://www.kaggle.com/juniorbueno/opencv-facial-recognition-lbph

### Project 3
#### Title:
Social Media Matcher

#### Problem statement:
Making meaningful connections with people can be difficult since determining someone's compatibility with you takes time and patience.

#### Abstract:
Over the past few years people have become accustomed to expressing their various opinions and general feelings on social media. Some people especially like using social media as an outlet for radical or particularly hateful comments. Most people aren't going to go through the process of background checking someone's social media history so these negative sentiments won't be discernible unless one is willing to go through a long process of getting to know someone. Our application would bypass this long process by using someone's social media presence and history to determine if they are a compatible match with another person based on their own social media presence. The potential compatibility could be returned as some percentage at which point it is up to the person using the application to decide what to do.

#### Approach:
We would need to collect all relevant datasets that include a large amount of social media posts ranging in context and emotion. We would also need to normalize and clean the data into a form that could be used by a model that would be able to categorize someone based on their toxicity. The output of this would be condensed into a digestible form that would be displayed to application users through an interactive dashboard. Users should be able to connect their own twitter or the app should query the user for their opinions on various topics to be able to determine their compatiblity with whatever person they are interested in.

#### Personas:
Social Media users interested in others as friend/partner

#### Relevant Datasets:
https://www.kaggle.com/rahulgoel1106/xenophobia-on-twitter-during-covid19
https://www.kaggle.com/andrewmvd/cyberbullying-classification
https://www.kaggle.com/ra2041/toxic-dataset
https://www.kaggle.com/nkitgupta/jigsaw-regression-based-data


# How should we define AI?

AI means different things to different people.

- For some, AI is about artificial life-forms that can surpass human intelligence, and for others, almost any data processing technology can be called AI.

- Applications of AI:
  - Self driving cars(search and planning to find the most convenient route from A to B, computer vision to identify obstacles, and decision making under uncertainty to cope with the complex and dynamic environment)
  - Content recommendation
  - Image and Video Processing

Today almost anything from statistics and business analytics to manually encoded if-else rules are called AI.

- Reason for this nebulous perception of AI can be:
  - **No officially agreed definition**: The field is rather being constantly redefined when some topics are classified as non-AI, and new topics emerge. There’s an old (geeky) joke that AI is defined as **cool things that computers can’t do.** The irony is that under this definition, AI can never make any progress: _as soon as we find a way to do something cool with a computer, it stops being an AI problem._ However, there is an element of truth in this definition. Fifty years ago, for instance, automatic methods for search and planning were considered to belong to the domain of AI. Nowadays such methods are taught to every computer science student. Similarly, certain methods for processing uncertain information are becoming so well understood that they are likely to be moved from AI to statistics or probability very soon.
  - **The legacy of science fiction**
  - **What seems easy is actually hard**: While easy for humans, grasping objects by a robot is extremely hard, and it is an area of active study. Recent examples include [Google’s robotic grasping project](https://spectrum.ieee.org/automaton/robotics/artificial-intelligence/google-large-scale-robotic-grasping-project), and a [cauliflower picking robot](https://www.plymouth.ac.uk/research/agri-tech/automated-brassica-harvesting-in-cornwall-abc).
  - **What seems hard is actually easy**

A better way to define AI would be to list properties that are characteristic to AI, like autonomy and adaptivity.

- **Autonomy**: The ability to perform tasks in complex environments without constant guidance by a user.
- **Adaptivity**: The ability to improve performance by learning from experience.

_Marvin Minsky_, coined the term **suitcase word** for terms that carry a whole bunch of different meanings that come along even if we intend only one of them. Using such terms increases the risk of misinterpretations like learning, understanding, and intelligence.

Different AI systems cannot be compared on a single axis or dimension in terms of their intelligence.

- Is a chess-playing algorithm more intelligent than a spam filter, or is a music recommendation system more intelligent than a self-driving car? makes no sense.
- Artificial intelligence is narrow, being able to solve one problem tells us nothing about the ability to solve another, different problem.

**AI is not a countable noun**: AI is a scientific discipline, like mathematics or biology. This means that AI is a collection of concepts, problems, and methods for solving them. Because AI is a discipline, one shouldn’t say “an AI”, just like one don’t say “a biology”. This point should also be quite clear when one try saying something like “we need more artificial intelligences.” That just sounds wrong.

- The use of AI as a countable noun is of course not a big deal if what is being said otherwise makes sense, but it's good to avoid saying "an AI", and instead say "an AI method".

# Related Fields to AI

There are several other closely related topics that come with AI and are good to know at least by name. These include machine learning, data science, and deep learning.

**Machine learning**: Systems that improve their performance in a given task with more and more experience or data.

- Machine learning can be said to be a subfield of AI, which itself is a subfield of computer science.
- These categories are often somewhat imprecise and some parts of machine learning could be equally well or better belong to statistics.

**Deep Learning** is a subfield of machine learning concerned with algorithms inspired by the structure and function of the brain called artificial neural networks. It is a class of machine learning algorithms that uses multiple layers to progressively extract higher-level features from the raw input.

- For example, in image processing, lower layers may identify edges, while higher layers may identify the concepts relevant to a human such as digits or letters or faces.
- Deep learning is a subfield of machine learning, which itself is a subfield of AI, which itself is a subfield of computer science.

**Umbrella term** is a term that covers several subdisciplines.
**Data science** is a recent umbrella term that includes machine learning and statistics, certain aspects of computer science including algorithms, data storage, and web application development.

- Data science solutions often involve at least a pinch of AI.

**Robotics** means building and programming robots so that they can operate in complex, real-world scenarios.

- Robotics is the ultimate challenge of AI since it requires a combination of virtually all areas of AI. For example: - _Computer vision_ and _speech recognition_ for sensing the environment - _Natural language processing_, _information retrieval_, and _reasoning under uncertainty_ for processing instructions and predicting consequences of potential actions - _Cognitive modeling_ and _affective computing_ (systems that respond to expressions of human feelings or that mimic feelings) for interacting and working together with humans
  A **robot** is a machine comprising _sensors_ (which sense the environment) and _actuators_ (which act on the environment) that can be programmed to perform sequences of actions.

- FUN FACT: Any kind of vehicles that have at least some level of autonomy and include sensors and actuators are also counted as robotics. On the other hand, software-based solutions such as a customer service chatbot, even if they are sometimes called “software robots”, aren’t counted as (real) robotics.

A **taxonomy** is a scheme for classifying many things that may be special cases of one another.

- A convenient way to visualize a taxonomy is an Euler diagram.
  - An Euler diagram consists of shapes that corresponds to concepts, which are organized so that overlap between the shapes corresponds to overlap between the concepts like Venn Diagrams.
- Note: A taxonomy does not need to be strictly hierarchical. A discipline can be a subfield of more than one more general topic.
  - eg. machine learning can also be thought to be a subfield of statistics.

# Philosophy of AI

The very nature of the term _artificial intelligence_ brings up philosophical questions whether intelligent behavior implies or requires the existence of a mind, and to what extent is consciousness replicable as computation.

**Turing Test**: Alan Turing (1912-1954) known as the father of computer science, was fascinated by intelligence and thinking, and the possibility of simulating them by machines. Turing’s most prominent contribution to AI is his imitation game, which later became known as the [Turing test](https://en.wikipedia.org/wiki/Turing_test).

- Turing’s test says, an entity is intelligent if it cannot be distinguished from another intelligent entity by observing its behavior.
- One criticism of the Turing test as a test for intelligence is that it may actually measure whether the computer behaves like a human more than whether it is intelligent.
- The idea that intelligence is the same as intelligent behavior is best challenged by John Searle’s [Chinese Room](http://www.iep.utm.edu/chineser/) thought experiment.
  - Searle describes an experiment where a person who doesn’t know Chinese is locked in a room. Outside the room is a person who can slip notes written in Chinese inside the room through a mail slot. The person inside the room is given a big manual where she can find detailed instructions for responding to the notes she receives from the outside.
  - Searle argued that even if the person outside the room gets the impression that he is in a conversation with another Chinese-speaking person, the person inside the room does not understand Chinese.
  - Likewise, even if a machine behaves in an intelligent manner, for example, by passing the Turing test, it doesn’t follow that it is intelligent or that it has a “mind” in the way that a human has. The word “intelligent” can also be replaced by the word “conscious” and a similar argument can be made.

The definition of intelligence, natural or artificial, and consciousness appears to be extremely evasive and leads to apparently never-ending discourse.

The philosophy of AI is unlikely to have any more effect on the practice of AI research than philosophy of science generally has on the practice of science.

**General vs Narrow AI**: Narrow AI refers to AI that handles one task. General AI, or Artificial General Intelligence (AGI) refers to a machine that can handle any intellectual task.

- All the AI methods we use today fall under narrow AI, with general AI being in the realm of science fiction. In fact, the ideal of AGI has been all but abandoned by the AI researchers because of lack of progress towards it in more than 50 years despite all the effort. In contrast, narrow AI makes progress in leaps and bounds.

**Strong vs weak AI**: A related dichotomy is _strong_ and _weak_ AI. This boils down to the philosophical distinction between being intelligent and acting intelligently, which was emphasized by Searle.

- Strong AI would amount to a “mind” that is genuinely intelligent and self-conscious. Weak AI is what we actually have, namely systems that exhibit intelligent behaviors despite being “mere“ computers.

AI can be defined as:

1.  "cool things that computers can't do".
2.  machines imitating intelligent human behavior.
3.  autonomous and adaptive systems.

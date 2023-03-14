# Introduction

Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence **concerned with the interactions between computers and human language**, in particular how to program computers to process and analyze large amounts of natural language data.

A natural language or ordinary language is any language that has evolved naturally in humans through use and repetition without conscious planning or premeditation.

Natural languages can take different forms, such as speech or signing.

## Application of NLP

Real World Applications of NLP:

- Contextual Advertisements (Different Advertisement for different person)
- Email Client - spam filtering and smart reply
- Social Media - removal of adult content, opinion mining
- Search Engines
- Chatbots

Common NLP task:

- Text/Document classification
- Sentiment Analysis
- Information Retrival
- Parts of Speech Tagging
- Language detection and Machine translation
- Conversational Agents
- Knowledge graph and QA systems
- Text Summarization
- Topic Modelling
- Text Generation
- Spell Checking and Grammer Correction
- Text Parsing
- Speech to Text

## Approaches to NLP

Rules and Heuristic Methods

- Regular Expressions
- Wordnet
- Open Mind Common Sense

Machine Learning Based Methods

- Naive Bayes
- Logistic Regression
- SVM
- LDA
- Hidden Markov Models

Deep Learning Based Methods

- RNN
- LSTM
- GRU/CNN
- Transformers
- Autoencoders

## Challenges in NLP

Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation due to:

- ambiguity
- contextual words
- colloquialisms and leg
- synonyms
- irony sarcasm and tonal difference
- spelling errors
- creativity
- diversity

# Basic End to End NLP Pipeline

NLP Pipeline is a set of steps followed to build an end to end NLP software.

The steps involved in building an end to end NLP software are:

- Data Acquisition
- Text Preparation
  - Text Cleanuo
  - Basic Preprocessing
  - Advanced Preprocessing
- Feature Engineering
- Model Building and Evalutation
- Deployment, Monitoring and Model Updates

This pipeline is not universal, Deep Learning Pipelines are slightly different and this pipeline is non-linear.

## Data Acquisition

Data Acquisition is gathering of data.

In data acquisition step three possible situation can happen.

1. Data is already available:

- Data available on local Machine: If data is available on local machine then we can directly go to next step i.e. Data Preprocessing.
- Data available on Database: If Data is available on database then we have to communicate to data engineering team then they gives data from database.
- Less Data Available: If Data is available but it is not enough then we use **Data Augmentation**.
  - Data augmentation is to making fake data.
  - Here we can use techniques like Synonyms, Bigram flip, Back translate or adding additional noise to data.

2. Data not available in our company but outside is available. Then we can use this approaches.

- Public Dataset
- Web Scrapping: Scrapping competitor data using beautiful soup or other library
- API: eg. Rapid API
- Other sources can be there like PDFs, audio, video

3. Data Not Available: Here we have to do survey for collecting data and then manually giving label to data.

## Data Preparation

After data collection step we have some data but it can not be used for model building.

Now we do text preparation. Steps involved in this are:

1. Text Cleaning: Here we do HTML tag removing (in case data contains them), emoji handling (**unicode normalization**), spelling check etc.
2. Basic Preprocessing: Here we almmost always do word or sentence tokenization, and sometimes some optional steps like stop word removal, stemming, lemmatization, removing punctuations and digit, lower casing, language detection etc.
3. Advance Preprocessing: Here we do Parts of Speech tagging, Chunking, Parsing, Coreference resolution etc.

## Feature Engineering

Feature Engineering means converting text data to numerical data.

- It is also known as text representation.

This is done because our machine learning model doesn't understand text data then we have do feature engineering.

In this step we use multiple techniques to convert text to numerical vectors. Some of the techniques are:

1. One Hot Encoding
2. Bag Of Word(BOW)
3. Tf-Idf (Term Frequency-Inverse Document Frequency)
4. N-grams/Bi-grams/Tri-grams
5. Word2vec

What technique to chose when is not fixed and it is upto the developer to chose in case of ML based NLP.

## Model Building and Evaluation

In modelling we try to make model based on data, here also we can use multiple approaches based on problem statement.

1. Rules and Heuristic Approach
2. Machine Learning Approach
3. Deep Learning Approach
4. Cloud API

What approach to chose is based on two thing Amount of data and Nature of problem.

- If we have very less data then we can not use ML or DL approach then we have to use heuristic approach.
- If we have good amount of data then we can use machine learning approach.
  - Sometimes with more data heuristic approach is used along with ML approach where the heuristic approach acts as a feature.
- If we have large amount of data then we can use deep learning approach.
  - Sometimes with DL transfer learning is also used.
- Based on nature of problem we have to check which approach gives best solution.

In evaluation we can use two metrics:

- Intrinsic evaluation where we use multiple metrics to check our model such as Accuracy, Recall, Confusion Metrics, Perplexity etc.
- Extrinsic evaluation which is done after deployment.
  - This is business centric approach.

## Deployment, Monitoring and Model Updates

In deployment we deploy model on cloud.

In monitoring we have to watch model.

- Here we create dashboard to show evaluation metrics.

Model update is retraining on new data.

# Text Preparation

It is process of deriving the meaningful information from the natural languages text that is required before giving the data to the model.

Mostly we start with **Lowercasing**, if Ram and ram word present in our data then these two words will be processed separately that's why we convert all data in lower case.

Next we need to remove some unimportant things from the text which are not required for machine.

- **Remove HTML Tags**: HTML tags are not important in model building they are neccessary for browser but not for the model so we have to use regex to remove them.
- **Remove URLs**: URLs is not important in model building so we have to remove them using regex.
- **Removing Punctuation**: If we don't remove punctuation then punctuation is also consider one word which is not the case, for this situation we remove punctuation.
- **Slang and Chat word treatment**: In normal chatting we use short abbreviation of words or some slang words so we have to change this short form to full form and slang to their respective meaning.
- **Removing Stop Words**: Stop words is only for sentence formation but in meaning of sentence stop words not help much so they are also removed.
  - They are sometimes not removed is we are about to do things like Parts of Speech tagging.
- **Handling Emojis**: Emojis not understand by machine learning model. We can either remove them or change them with their meaning.

We also sometimes have to do some optional extra steps like:

- **Spelling Correction**: As the text are written by humans they are prone to errors like spelling mistakes so we have to do spelling correction as well.
- **Tokenization**: Here we break data into smaller parts called tokens which can be done on word or sentence.
- **Stemming/Lemmitization**: In grammar, inflection is the modification of a word to express different grammatical categories such as case, voice, aspect, person, number, gender, and mood.

  - Both of the techniques are used to reduce inflection in a word i.e. reduce multiple words with same meaning into a single common root word.

  - Stemming means mapping a group of words to the same stem by removing prefixes or suffixes without giving any value to the _grammatical meaning_ of the stem formed after the process.

    - In simple word stemming remove suffix and prefix from word.
    - It is important to note that the stem (root word) is not always meaningful.
    - Stemmer is the algorithm to do stemming.

      1. Porter Stemmer which is specific for English language.
      2. Snowball Stemmer that is used for multiple language.
      3. Lancaster Stemmer.

  - Lemmatization also does the same thing as stemming and try to bring a word to its base form, but unlike stemming it do keep in account the actual meaning of the base word called Lemma.

    - In Lemmatization we search word in wordnet.
    - Lemma is the canonical form, dictionary form or citation form of a set of words.
    - Stemming is faster and Lemmatization is comparatively slower.

# Text Representation/Feature Extraction

Machine learning algorithms often use numerical data, so when dealing with textual data or any natural language processing (NLP) task, a sub-field of ML/AI dealing with text, that data first needs to be converted to a vector of numerical data by a process known as **vectorization**.

## TF-IDF

TF-IDF stands for term frequency-inverse document frequency and it is a measure, used in the fields of information retrieval (IR) and machine learning, that can quantify the importance or relevance of string representations (words, phrases, lemmas, etc) in a document amongst a collection of documents (also known as a corpus).

Term frequency works by looking at the frequency of a particular term you are concerned with relative to the document.

There are multiple measures, or ways, of defining frequency:

- Number of times the word appears in a document (raw count).
- Term frequency adjusted for the length of the document (raw count of occurences divided by number of words in the document).
- Logarithmically scaled frequency (e.g. log(1 + raw count)).
- Boolean frequency (e.g. 1 if the term occurs, or 0 if the term does not occur, in the document).

Inverse document frequency looks at how common (or uncommon) a word is amongst the corpus.

IDF of a term (t) in corpus (D) with N documents (d) is calculated as `idf(t, D) = log(N/df(t))` where df(t) is simply the number of documents in which the term, t, appears in.

- It can be possible for a term to not appear in the corpus at all, which can result in a divide-by-zero error.
- One way to handle this is to take the existing count and add 1 to both numerator and denominator.

The reason we need IDF is to help correct for words like “of”, “as”, “the”, etc. since they appear frequently in an English corpus.

- Thus by taking inverse document frequency, we can minimize the weighting of frequent terms while making infrequent terms have a higher impact.

The key intuition motivating TF-IDF is the importance of a term is inversely related to its frequency across documents.

- TF gives us information on how often a term appears in a document and IDF gives us information about the relative rarity of a term in the collection of documents.
- By multiplying these values together we can get our final TF-IDF value i.e. `tf-idf(t, d, D) = tf(t,d) * idf(t, D)`.
- The higher the TF-IDF score the more important or relevant the term is; as a term gets less relevant, its TF-IDF score will approach 0.

There are three main applications for TF-IDF.

- Machine learning
- Information retrieval
- Text summarization/keyword extraction

TF-IDF can be used to vectorize text into a format more agreeable for ML & NLP techniques.

- TF-IDF vectorization involves calculating the TF-IDF score for every word in your corpus relative to that document and then putting that information into a vector.
- Thus each document in your corpus would have its own vector, and the vector would have a TF-IDF score for every single word in the entire collection of documents.
- Once you have these vectors you can apply them to various use cases such as seeing if two documents are similar by comparing their TF-IDF vector using cosine similarity.

It is simple to calculate, it is computationally cheap, and it is a simple starting point for similarity calculations (via TF-IDF vectorization + cosine similarity).

TF-IDF cannot help carry semantic meaning.

- It considers the importance of the words due to how it weighs them, but it cannot necessarily derive the contexts of the words and understand importance that way.

TF-IDF ignores word order so sometimes it won't consider compound nouns as a single unit.

- This way compound nouns like “Queen of England” will not be considered as a “single unit”.
- This also extends to situations like negation with “not pay the bill” vs “pay the bill”, where the order makes a big difference.
- Using NER tools and underscores are ways to handle treating the phrase as a single unit.

It can suffer from memory-inefficiency since TF-IDF can suffer from the **curse of dimensionality** as the length of TF-IDF vectors is equal to the size of the vocabulary.

- In some classification contexts this may not be an issue but in other contexts like clustering this can be unwieldy as the number of documents increases.
- Thus looking into some of the alternatives like BERT, Word2Vec etc may be necessary.

## Bag of Words

Bag of Words (BoW) simply counts the frequency of words in a document. Thus the vector for a document has the frequency of each word in the corpus for that document.

The key difference between bag of words and TF-IDF is that the former does not incorporate any sort of inverse document frequency (IDF) and is only a frequency count (TF).

## Word2Vec

## BERT

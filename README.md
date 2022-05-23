# Automatic-Resume-Ranking-with-dataset-and-model

# Introduction

This project enables recruiters to wade through an ocean of resumes (especially during high-volume recruiting) to find the perfect candidates that match the job requirements. 
It filters applications based on skills, education, experience, or anything that is a requirement for an open role.
The result achieved by assigning a score to each CV by intelligently comparing them against the corresponding Job Description.
The project uses techniques in Machine Learning and Natural Language Processing to automate the procedure.

## Division of the report
The report has been divided into 4 sections.
## 1. Data Collection
**Mainly used three datasets:-**
- StackExchange Network Posts dataset
- Job Descriptions dataset 
- Resumes Collection 

**StackExchange Network Posts dataset**
- This dataset was required to be trained and load to the word2vec model.StackExchange network dumps it's data in xml format under Creative Commons License. One can find a download link for the dataset(80 GB) 


- This is an anonymized dump of all user-contributed content on the Stack Exchange network. Each site is formatted as a separate archive consisting of XML files zipped via 7-zip using bzip2 compression. Some portions of dataset contents i mentioned bellow, click below link to view or download the dataset.
- - Dataset link [on Internet Archive.](https://archive.org/details/stackexchange)

![dataset](https://user-images.githubusercontent.com/76810003/169806535-45c86e40-f407-4159-90d0-9a63e64debfe.png)



**Job Description Dataset**
- A Kaggle dataset ontaining Job Descriptions for several job openings was used.
- We used NLP to filter out the Job Descriptions related to IT industry.
- Kaggle Dataset can be found [here](https://www.kaggle.com/c/job-salary-prediction/data)
- Finally, 5000+ JDs including JDs for positions like 'Web devloper', 'C++ software developer', 'Software developer', 'Enbedded Software Engineer' were filtered out and saved as ***jd.csv***.

**Rusumes**
- So, a Python Script(collectCV.py) was used to collect around 250 resumes of applicants for positions like 'Software Developer' , 'Data Scientist', 'Web Developer' etc.
- You can collect more Cvs from any free websites in text format using ( **collect.py**) python files.
- This dataset was required to test the trained word2vec model. Among these resumes, best matching resumes should be filtered out.

**2. Data Extraction**
- unzip all the downloaded dataset of stackexchange network Posts dataset using **zipextract.py** and place the unzipped files inside a directory named **stackexchage**.
- Each  subdirectory inside stackexchange folder includes Posts, Users, Votes, Comments, PostHistory and PostLinks (all in .xml files).


# How to use
## steps
1. Download and unzip the StackExchange Network Posts dataset( Follow the above instruction)
2. Each subdirectory of  dataset conatins posts.xml therefore  Generate text file named (**paras.txt**) using **Extraction_from_posts.ipynb** file.
3. Generate another text file named (**sentences.txt**) using **Sentence_Extraction.ipynb** file.
4. Train the model using **Model_Training.ipynb** file after successfully run it will generate a trained model named **stackexchange_model** in CWD.

## How to use trained model for CV Ranking and word2vec 
1. Generate CSV file named *prc_data.csv* using **Section_Extraction.ipynb**
2. All the model and cleaned data are ready therefore for cv ranking.
3. You can rank the resumes by **CV_ranking.ipynb** file.
4. Run **With Word2Vec.ipynb** to understand better concept of word2vec using trained model **stackexchange_model** model.



# Directory Structure 
## Place the Files and Directories as bellow structure to avoid error
<pre>
.
├── Resumes
│   ├── CVs/
│   ├── collectCV.py
│  
├── Model
│   ├── Model_Training.ipynb
│   ├── Extraction_from_posts.ipynb
│   ├── Sentence_Extraction.ipynb
│   ├── StackExchange/
│   ├── stackexchange_model
│   
├── Filter
│   ├── CV_ranking.ipynb
│   ├── Using Spacy Model.ipynb
│   ├── With Word2Vec.ipynb
│   ├── jd.csv
│   └── prc_data.csv
│   
└── Extract
    ├── Section_Extraction.ipynb
    ├── convertDocxToText.py
    ├── pdf2txt.py
    ├── zipextract.py

    
</pre>

## Note 
Inside **Model** directory the **stackexchange** folder and **stackexchange_model** model will not be available as their huge amount of size(almost 80+ GB) so follow the above instructions carefully to download and unzip dataset and place inside stackexchange folder and train the model. 

# Usage of  Files and Directories 
## Data
- **CVs :** Directory Contains 250 extracted resumes in text format collected from [postjobfree.com](https://www.postjobfree.com/).
- **collectCV.py :** Python script to automate the process of extracting CVs from postjobfree.com. While this program is running, every new text copied to clipboard is saved as a CV in **CVs/** directory. 

## Model

- **Model_Training.ipynb :** Notebook to train and save the word2vec model.After successfully run the model(`stackexchange_model`) will be  saved in ```./Model/``` subdirectory (locally). 

![model tra](https://user-images.githubusercontent.com/76810003/169807656-cba76b63-277a-45db-9340-070a06627070.png)


- **Extraction_from_posts.ipynb :** Notebook for extracting paragraphs(`paras.txt`) from `Posts.xml`.
- **Sentence_Extraction.ipynb :** Notebook for extracting cleaned sentences(`sentences.txt`) from extracted paragraphs (`paras.txt`).
- **paras.txt :** Each and every subdirectory of dataset in stackexchange directory contains this file which is  paragraph in html tags file format, It was extracted from  ```Posts.xml``` using the code ***Extraction_from_posts.ipynb***
- **stackexchange/ :** Its a directory that contains all the unzip stackoverflow datasets.
- **sentences.txt :** Each and every subdirectory of dataset in stackexchange directory contains this file, It was extracted from the corresponding paras.txt which generated earlier using the code ***sentence_Extraction.ipynb***. The process took around 24.5 hours to complete.

**Note**
- For testing purpose you can download a small portion (3 or 4 GB) of StackExchange Network Posts dataset [Download.](https://archive.org/details/stackexchange) and preform the above procedures along with trainig your own model  if you get enough confidence  so do it with all the dataset.

## Filter
- **CV_ranking.ipynb :** Notebook for ranking the CVs according to Job Description.

![rank](https://user-images.githubusercontent.com/76810003/169807480-fef89a88-bc1d-4667-997b-8ed418f5300f.png)


- **Using Spacy Model.ipynb :** Demonstrates the need for a custom Word2Vector model rather than a general model trained otherwise. The similarity values generated by ``` en_core_web_md ``` spaCy model trained on Google News articles, do not reflect the `technological sharpness` required for the project.
- **With Word2Vec.ipynb :** Demonstrates how to use word2vec to get similar words by words and similar words by vector. It also implements sent2vec() function.  This function takes a sentence as a argument and returns a average vector for the sentence. Root Mean Square is used to average the vectors.  The advantage of this function is to use it to find similar words for phrases which makes more sense while searching for roles etc.

For example:
```
'web developer' will give 'developer' as a similar word
``` 
![word2vec](https://user-images.githubusercontent.com/76810003/169807255-e9c00a68-44de-42ad-beac-276df4854cc0.png)



- **jd.csv :** CSV file containing cleaned job descriptions from Kaggle. Dataset can be found [here](https://www.kaggle.com/c/job-salary-prediction/data)
- **prc_data.csv :** CSV file storing processed sections of different resumes.


## Extract
- **Section_Extraction.ipynb :** Notebook for extracting main sections from different resumes.

![section](https://user-images.githubusercontent.com/76810003/169807357-196bc31e-3e71-4aaf-8f67-c8aeae44ffb3.png)


- **convertDocxToText.py :** Python script for converting a `.docx` file to `.txt'.
- **pdf2txt.py :** Python scrtpt for converting a `.pdf` file to `.txt`.
- **zipextract.py :** Python script for extracting compressed files in `7z`.

# Summery 

## Training Word2Vec Model

Word2Vec models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words.
Word2vec takes as its input a large corpus of text and produces a vector space, typically of several hundred dimensions, with
each unique word in the corpus being assigned a corresponding vector in the space. Word vectors are positioned in the
vector space such that words that share common contexts in the corpus are located in close proximity to one another in the
space.

# Requirement of training our own models
- There are pre-trained models available both in gensim and spaCy packages in Python. These models are trained over Google News Data. This implies that they are not suitable for the technically aware context distinction required for this project. For e.g. HTML and Ruby may have higher similarity value in these models than the model we trained.

- Therefore,a dataset was required which was both technically aware and also has sufficient amount of unique words present for the non-technical functioning of the model.

- The dataset used to train Word2Vec model becomes more crucial considering the fact that Word2Vec models can be retrained over and over, however, new Vocabulary cannot be added to the model.
- Therefore, stackexchange network data was used and trained my own model.
-
- Run both files **With Word2Vec.ipynb** (used my own trained model) and **Using Spacy Model.ipynb** (used pretrained model) to see the difference and performance of two different models.




## Cleaning and Extracting data
- From the stackexchange/ dataset the Posts.xml for each site was used to extract each Post irrespective of whether
it's a Question or an Answer. These Posts were extracted as HTML para tags and saved as paras.txt in the
corresponding subfolder of the site.
- At this stage, each subdirectory of StackExchange/ which corresponds to the site under StackExchange network, has a
new file called paras.txt .
- For training the Word2Vec model, we required a sequence of sentences to be streamed from the disk. Each sentence is
represented as a list i.e. each element of this list is the word of the sentence.
So, the paras.txt files were used to extract sentences using BeautifulSoup(a Python Library), and saved into
sentences.txt (for each site), such that the final result is free of formatting and mathematics, code etc.
- These sentences were streamed into the Word2Vec train method for training the model.

## Generated Word2Vec Word Embeddings
- Each word is represented as a 300-sized numpy array (vector).
- Collected 1237328 unique words from a corpus of 565919447 raw words and 32701720 sentences.

## Extracting sections
- We have some collection of words that are usually the heading in the resumes. For example 'education', 'academic', 'school', 'study', etc will mark the start of the education section
- We iterate over all lines of all resumes, one by one.
- For each line, first, we remove all the blank lines or the lines containing just symbols. Some resumes have a line denoted
to just asterisks or dashes.
- Next, we categorize each line into one of the four sections. This is done by calculating its similarity to the existing words.
If the similarity is higher than the threshold, we update the section and mark that point, on the other hand, if the similarity
if below the threshold, we continue with the previous section.
- This enables us to separate the sections with good enough accuracy.
- Finally, we write each section of a resume in a .csv file after removing the stop words and doing lemmatization


## Assigning scores for ranking
- For a given Job Description, we remove all the stop words and do lemmatization, to get a selected few keywords.
- For each keyword found, we find 5 similar words and their corresponding similarity.
- Now, we find tf-idf for each word, that we got in step 2.
- The score of the CV is the sum of tf-idf * similarity for all words we got in step 2.

# Resources
- https://spacy.io/
- https://jalammar.github.io/illustrated-word2vec/
- https://github.com/explosion/spaCy/issues
- http://radimrehurek.com/gensim/models/word2vec.html
- https://code.google.com/archive/p/word2vec/
- https://github.com/linanqiu/word2vec-sentiments
- https://stackoverflow.com/
- https://www.kaggle.com/c/job-salary-prediction/data
- https://archive.org/details/stackexchange



## Author

<table>
<tr>
<td>
     <img src="https://avatars.githubusercontent.com/u/76810003?s=400&u=3de867a69316245acd6e93279367fc2a37a6dd14&v=4" width="180"/>
     
     Saifullah Rahimi

<p align="center">
<a href = "https://github.com/saifujasoor"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/saifullahrahimi/"><img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/></a>
</p>
</td>
</tr> 
  </table>


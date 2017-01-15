# text_analytics



Different APIs for text analytics and SEMANTIC ANALYSIS using machine learning were tried including :

Algorithmia - Many text analytics, NLP and entity extraction algorithms are available as part of their cloud based offering
Algorithmia algorithms tried out include: 
- Part of speech tagging using OpenNLP: http://opennlp.apache.org/
The Part of Speech Tagger marks tokens with their corresponding word type based on the token itself and the context of the token. A token might have multiple pos tags depending on the token and the context. The OpenNLP POS Tagger uses a probability model to predict the correct pos tag out of the tag set. To limit the possible tags for a token a tag dictionary can be used which increases the tagging and runtime performance of the tagger. Parts are tagged according to the conventions of the Penn Treebank Project (https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html). For example, a plural noun is denoted NNS, a singular or mass noun is NN, and a determiner (such as a/an, every, no, the,another, any, some, each, etc.) as DT.
- Tokenizer: https://algorithmia.com/algorithms/ApacheOpenNLP/TokenizeBySentence
- Auto tagging of text: Algorithm uses a variant of nlp/LDA to extract tags / keywords - https://algorithmia.com/algorithms/nlp/AutoTag

Aylien - Classification by Taxonomy: https://developer.aylien.com/

Use LDA to Classify Text Documents - LDA is an algorithm that can be used to generate topics to understand a document’s general theme: http://blog.algorithmia.com/lda-algorithm-classify-text-documents/

MonkeyLearn: Taxonomy Classifier: https://app.monkeylearn.com/main/classifiers/cl_b7qAkDMz/tab/tree-sandbox/

Output - Python Dictionary data structure inside Algorithmia

Tesseract OCR in Algorithmia: 
https://algorithmia.com/algorithms/tesseractocr/OCR

Create PDF using ReportLab PLUS: https://www.reportlab.com/reportlabplus/


import Algorithmia
client = Algorithmia.client('sim3x6PzEv6m2icRR+23rqTTcOo1')

#from Algorithmia.acl import ReadAcl, AclType
#Next create a data collection called nlp_directory:

import os
os.listdir(".")

# Set your Data URI
#nlp_directory = client.dir("data://my/ocr")
# Make your newly created data collection
#nlp_directory.create()

#input = "data://shamitb/ocr/text_eng.jpg"
#algo = client.algo('ocr/SmartOCR/0.2.6')
#print algo.pipe(input)

input = {"src":"data://shamitb/ocr/ai.jpg"}

client_algo = Algorithmia.client('sim3x6PzEv6m2icRR+23rqTTcOo1')

#from Algorithmia.algorithm import OutputType
algo = client_algo.algo('tesseractocr/OCR/0.1.0')
#.set_options(output=OutputType.raw, stdout=True)
#response = algo.pipe(input).result
response = algo.pipe(input).result
print response['result']


print '\n*******************************\n TAXONOMY : \n'
# **************** Aylien - Taxonomy ****************
from aylienapiclient import textapi
client_aylien = textapi.Client("a19bb245", "2623b77754833e2711998a0b0bdad9db")
text = response
classifications = client_aylien.ClassifyByTaxonomy({"text": text, "taxonomy": "iab-qag"})
for category in classifications['categories']:
  print category['label']


print '\n*******************************\n AUTO TAGS : \n'
# ************** Algorithmia - Auto - tag *******************
input = text['result']
algo = client.algo('nlp/AutoTag/1.0.0')
response2 = algo.pipe(input)
for category in response2.result:
  print category


print '\n*******************************\n ENTITIES : \n'
# **************** Algorithmia - Entities ****************
text = response['result']
text.encode('ascii', 'ignore')
#entities = client_aylien.Entities({"text": text})
#for type, values in entities['entities'].iteritems():
#  print type,', '.join(values)


algo = client.algo('StanfordNLP/NamedEntityRecognition/0.2.0')
entities = algo.pipe(text)
print entities.result
entities = entities.result


print '\n*******************************\n DOCUMENT SIMILARITY : \n'
# **************** Algorithmia - TextSimilarity ****************
input = {"files": [["doc1", "the document about tigers"], ["doc2", "the movie about cars"], ["doc3", "the document about cats"]]}
print input
algo = client.algo('PetiteProgrammer/TextSimilarity/0.1.2')
print algo.pipe(input).result

print '\n*******************************\n SENTENCE PARSING : \n'
# **************** Algorithmia - SENTENCE PARSING ****************
input = {
  "src":"Algorithmia is the best online platform available for machine learning and text analytics.",
  "format":"conll",
  "language":"english"
}
algo = client.algo('deeplearning/Parsey/1.0.2')
print algo.pipe(input).result

print '\n*******************************\n CO-REFERENCE : \n'
# ****************** CO REFERENCE **********************
algo = client.algo('StanfordNLP/DeterministicCoreferenceResolution/0.1.1')
print algo.pipe(text).result

print '\n*******************************\n PART-OF-SPEECH (POS) TAGGER : \n'
# ****************** PART-OF-SPEECH (POS) TAGGER **********************
algo = client.algo('ApacheOpenNLP/POSTagger/0.1.1')
print text
print algo.pipe(text)

print '\n*******************************\n TOKENIZE : \n'
# ****************** TOKENIZE **********************
algo = client.algo('ApacheOpenNLP/TokenizeBySentence/0.1.0')
print algo.pipe(text)

print '\n*******************************\n LDA : \n'
# ****************** LDA **********************
algo = client.algo('ApacheOpenNLP/SentenceDetection/0.1.0')
sentences = algo.pipe(text)
print sentences
algo = client.algo('nlp/LDA/1.0.0')
input = {
  "docsList": sentences.result,
  "mode": "quality"
}

print input
print algo.pipe(input).result

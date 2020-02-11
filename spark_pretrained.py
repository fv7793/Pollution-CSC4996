import sparknlp
from sparknlp.pretrained import PretrainedPipeline
import os
import sys
# Path for spark source folder
os.environ['JAVA_HOME'] = 'C:\Program Files\Java\jre1.8.0_241'
#create or get Spark Session
print("before start")
spark = sparknlp.start()
print("after start")
#download, load, and annotate a text by pre-trained pipeline

pipeline = PretrainedPipeline('analyze_sentiment_ml', 'en')
print("after pipeline creation")
result = pipeline.annotate('Harry Potter is a great movie')

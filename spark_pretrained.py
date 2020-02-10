import sparknlp
from sparknlp.pretrained import PretrainedPipeline

#create or get Spark Session

spark = sparknlp.start()

sparknlp.version()
spark.version

#download, load, and annotate a text by pre-trained pipeline

pipeline = PretrainedPipeline('recognize_entities_dl', 'en')
result = pipeline.annotate('Harry Potter is a great movie')

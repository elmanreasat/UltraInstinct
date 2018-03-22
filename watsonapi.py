import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='[]',
  password='[]',
  version='2017-02-27')

response = natural_language_understanding.analyze(
  text= '<Enter text here>',
  features=Features(
   
	#entities=EntitiesOptions(
     # emotion=True,
     # sentiment=True,
     # limit=2),
	  
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=5)))



watson_output = json.dumps(response, indent=2)


with open("json_output.txt", "w") as file:
	file.write(watson_output)


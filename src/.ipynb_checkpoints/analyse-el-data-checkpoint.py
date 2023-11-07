# Install dependencies
import os
from elasticsearch import Elasticsearch, NotFoundError, helpers
import csv
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Connect to ElasticSearch
es = Elasticsearch(
  "http://localhost:9200",
  basic_auth=("elastic", os.getenv('ELASTIC_PASSWORD')),
)

# Check if CSV is on Elastic
def check_data():
  try:
    result = es.search(
      index='heart-csv-data',
    )
  except NotFoundError:
    print('Index Not found. Adding to ElasticSearch...')
    with open('./src/data/heart.csv') as f:
      reader = csv.DictReader(f)
      helpers.bulk(es, reader, index='heart-csv-data')
    return False
  else:
    print('Data is OK')
    return True

# Loops until CSV data is added onto Elastic
while (True):
  result = check_data()
  if (result == True):
    break

# Indexing
result = es.index(
 index='lord-of-the-rings',
 document={
  'age': '58',
 })

print(result)

# Searching
result = es.search(
 index='heart-csv-data',
 query={
    'match': {'age': '58'}
  },
)
print(result)

# Updating data
result = es.index(
 index='heart-csv-data',
 document={
  'age': '58',
 })

es.update(
 index='heart-csv-data',
 id=result['_id'], 
 doc={'age': '67'}
)

print(es.get(index='heart-csv-data', id=result['_id']))
from elasticsearch import Elasticsearch
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

es = Elasticsearch(
    cloud_id=config['ELASTIC']['cloud_id'],
    api_key=(config['ELASTIC']['apikey_id'], config['ELASTIC']['apikey_key']),
)

# Index a document
es.index(
 index='webapplogs',
 document={
        "timestamp": "2023-07-11T18:37:49.123Z",
        "level": "INFO",
        "message": "User logged in successfully",
        "user_id": "123",
        "ip_address": "192.168.1.10",
        "http_status": 200
    })


# Refresh the index
es.indices.refresh(index='webapplogs')

# Search data
result = es.search(
 index='webapplogs',
  query={
    'match': {'user_id': '123'}
  }
 )

# Get data - Use id from previous result
result = es.get(index='webapplogs', id='PyvNMOkBtwZ6ch-vvdSy')

# Update data
result= es.update(
 index='webapplogs',
 id='PyvNMOkBtwZ6ch-vvdSy', 
 doc={'timestamp': '2023-07-11T18:37:49.123Z', 'level': 'INFO', 'message': 'User login Failed', 'user_id': '123456', 'ip_address': '192.168.1.10', 'http_status': 500}
 )

# Verify data update
result = es.get(index='webapplogs', id='PyvNMOkBtwZ6ch-vvdSy')

# Delete document
result = es.delete(index="webapplogs", id='PyvNMOkBtwZ6ch-vvdSy')

# Verify document deletion.
result = es.get(index='webapplogs', id='PyvNMOkBtwZ6ch-vvdSy')
# elasticsearch.NotFoundError: NotFoundError(404, "{'_index': 'webapplogs', '_id': 'PyvNMOkBtwZ6ch-vvdSy', 'found': False}")

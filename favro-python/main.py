import requests
import os

session = requests.Session()
session.auth = (os.environ.get('FAVRO_USER'), os.environ.get('FAVRO_API_KEY'))
session.headers.update({'organizationId': os.environ.get('FAVRO_ORGANIZATION')})

def getCollectionIdByName(collectionName, session):
    collectionsResponse = session.get('https://favro.com/api/v1/collections')
    collections = collectionsResponse.json()['entities']

    collectionId = None

    for collection in collections:
        if collection['name'] == collectionName:
            collectionId = collection['collectionId']

    return collectionId

collectionId = getCollectionIdByName(os.environ.get('FAVRO_COLLECTION'), session)

print(collectionId)

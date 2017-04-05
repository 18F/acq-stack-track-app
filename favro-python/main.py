import requests
import os
from IPython import embed
import time

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

# collectionId = getCollectionIdByName(os.environ.get('FAVRO_COLLECTION'), session)

def getColumns(commonWidgetId, session):
    columnsResponse = session.get('https://favro.com/api/v1/columns',
                                  params={'widgetCommonId': commonWidgetId})
    columns = columnsResponse.json()['entities']
    return columns

# columns = getColumns(os.environ.get('FAVRO_WIDGET_ID'), session)

# for column in columns:
#     print("Column id: {}".format(column['columnId']))
#     print("Column name: {}".format(column['name']))
#     print()

def createCard(name, commonWidgetId, columnId, customFields, session):
    data = {
        'name': name,
        'widgetCommonId': commonWidgetId,
        'columnId': columnId,
        'customFields': []
    }
    for customField in customFields:
        data['customFields'].append(customField)

    headers = {'Content-Type': 'application/json'}
    createCardResponse = session.post('https://favro.com/api/v1/cards',
                                      json=data,
                                      headers=headers)
    return createCardResponse

# createCardResponse = createCard('The Robot Created Me',
#                                 os.environ.get('FAVRO_WIDGET_ID'),
#                                 '2dqzxZbYJGCGK5rsD',
#                                 [],
#                                 session)


def getCards(commonWidgetId, session):
    cardsResponse = session.get('https://favro.com/api/v1/cards',
                                params={'widgetCommonId': commonWidgetId})
    cards = cardsResponse.json()['entities']
    return cards

# cards = getCards(os.environ.get('FAVRO_WIDGET_ID'), session)

def moveCard(cardId, columnId, widgetCommonId, session):
    url = 'https://favro.com/api/v1/cards/{}'.format(cardId)
    data = {
        'columnId': columnId,
        'widgetCommonId': widgetCommonId
    }
    headers = {'Content-Type': 'application/json'}
    moveCardResponse = session.put(url, json=data, headers=headers)
    return moveCardResponse

# Sample columns:
# Column id: 2dqzxZbYJGCGK5rsD
# Column name: Done
#
# Column id: e652175808a0c3d1f5cbd3c9
# Column name: Backlog
#
# Column id: t6ecQ4a7crTSaKRxw
# Column name: Doing

# cardId = 'c673b8ff2a4c4e3401f35b31'
# backlog = 'e652175808a0c3d1f5cbd3c9'
# doing = 't6ecQ4a7crTSaKRxw'
# done = '2dqzxZbYJGCGK5rsD'
#
# for _ in range(10):
#     time.sleep(0.2)
#     moveCard(cardId,
#              backlog,
#              os.environ.get('FAVRO_WIDGET_ID'),
#              session)
#
#     time.sleep(0.2)
#     moveCard(cardId,
#              doing,
#              os.environ.get('FAVRO_WIDGET_ID'),
#              session)
#
#     time.sleep(0.2)
#     moveCard(cardId,
#              done,
#              os.environ.get('FAVRO_WIDGET_ID'),
#              session)

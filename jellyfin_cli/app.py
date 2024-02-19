import asyncio
import jellyfin_client.JellyfinClient as JellyfinClient
import jellyfin_client.data_classes.Items as Items
import pprint


def async_to_sync(awaitable):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(awaitable)

client =  JellyfinClient.HttpClient(server='https://jelly.vid.gaffinet.lu')


async_to_sync(client.login('yves', 'yvesyves'))


view =  async_to_sync(client.get_views())

for v in view:
    print(v)

#view =  async_to_sync(client.get_recommended())

#for v in view:
#    print(v)

#Items.Item()

#eps = async_to_sync(client.())

#print(len(eps))

#detail = async_to_sync(client.get_show())

#print(detail)
    
json = async_to_sync(client.getItem('740061745a626a75ee81fcb403655a34'))

if json['type'] == "Serie":


pprint.pprint(json)



# libfreehackquest-client-py

FreeHackQuest Python Client Library for fhq-server: [https://github.com/freehackquest/fhq-server.git](https://github.com/freehackquest/fhq-server.git)

## Install
```
pip3 install libfreehackquestclient --upgrade
```

## Example code

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from libfreehackquestclient import FreeHackQuestClient

fhq = FreeHackQuestClient("ws://freehackquest.com:1234/ws-api/")

q = fhq.quest({"questid": 148})
print("quest: " + str(q))

# or "ws://freehackquest.com:1234" or "ws://freehackquest.com/ws-api/"
resp = fhq.login({"email": "admin", "password": "admin"})
if resp == None:
    print('Could not login as user (1)')

if resp['result'] == 'FAIL':
    print('Could not login as user (1)')

print("user info: " + str(resp))
```

Full description API here: [API.md](./API.md)

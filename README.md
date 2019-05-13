# libfhqcli-py

FreeHackQuest Python Client Library for fhq-server: [https://github.com/freehackquest/fhq-server.git](https://github.com/freehackquest/fhq-server.git)

## Install
```
pip install libfhqcli --upgrade
```

## Example code

```
import libfhqcli

fhq = None
try:
  fhq = libfhqcli.FHQCli("ws://localhost:1234/") # or "ws://freehackquest.com:1234" or "ws://freehackquest.com/ws-api/"
  resp = fhq.login({"email": "admin", "password": "admin"})
  if resp == None:
    print('Could not login as user (1)')

  if resp['result'] == 'FAIL':
    print('Could not login as user (1)')

  print("user info: " + str(resp))
  q = fhq.quest({"questid": 148})
  print("quest: " + str(q))

finally:
  if fhq != None:
    fhq.close()
```

Full description API here: [API.md](./API.md)

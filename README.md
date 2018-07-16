# libfhqcli-py

FreeHackQuest Python Client Library for fhq-server: [https://github.com/freehackquest/backend.git](https://github.com/freehackquest/backend.git)

## Install
```
pip install libfhqlib
```


## Example usage

```
import libfhqcli

fhq = libfhqcli.FHQCli("ws://localhost:1234/") // or "ws://freehackquest.com:1234" or "ws://freehackquest.com/ws-api/"
fhq.login({"email": "user@mailussr.su", "password": "user"})
if resp == None:
  print('Could not login as user (1)')
  
if resp['result'] == 'FAIL':
  print('Could not login as user (1)')
  
print("user info: " + str(resp));
q = fhq.quest({"questid": 148})
print("quest: " + str(q));
fhq.close();
```

Full description API here: [API.md](./API.md)

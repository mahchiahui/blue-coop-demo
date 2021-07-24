# blue-coop-demo
Blackhat blue coop demo code

## Usage

use this to run demo blue coop server

```
export FLASK_APP=bluecoop && flask run --host=0.0.0.0 --port=80
```

## Test

use this to test if server is up

```
curl --header "Content-Type: application/json" --request POST --data '{"username":"xyz","password":"xyz"}' http://<replace with server ip>/
```
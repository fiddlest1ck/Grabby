# Grabby REST API

### Runs at localhost:5000...

# GET /api/v1/records/
### Saved responses list:
```sh
  "records": [
    {
      "id": 1, 
      "response_date": "Mon, 13 Nov 2017 11:35:46 GMT", 
      "status_code": 200, 
      "url": "http://wp.pl"
    }, 
    {
      "id": 2, 
      "response_date": "Mon, 13 Nov 2017 11:51:21 GMT", 
      "status_code": 200, 
      "url": "http://wp.pl"
    }
    ]
```    
# GET /api/v1/records/<id>
### Saved response by id:
```sh
  "records": [
    {
      "id": 1, 
      "response_date": "Mon, 13 Nov 2017 11:35:46 GMT", 
      "status_code": 200, 
      "url": "http://wp.pl"
    }
    ]
```
# DELETE /api/v1/records/<id>
### Delete record by id:
```sh
"Record http://wp.pl id 1 deleted"
```

# GET /api/v1/backup/
### Download database:
```sh
"grabby.db"
```
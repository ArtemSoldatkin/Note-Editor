# Note editor api (python / Flask)

-- To start: --
docker-compose up -d --build

## API Documentation

#### Get notes

Returns all saved notes.

- URL
  /get-notes
- Method
  GET
- URL Params
  None
- Data Params
  None
- Success Response:
  - Code: 200 OK
    Content: {notes: [{
    text: "text",
    ID: "6b87d44f-d563-4ed5-961a-c5d67504e066",
    date: {
    year: 2020,
    month: 5,
    day: 8,
    hour: 13,
    minute: 26
    },
    changed: false
    }]}
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR
    Content: { message: "Server error, try later" }

#### Add note

Add note to list.

- URL
  /add-note
- Method
  POST
- URL Params
  None
- Data Params
  text=[string]
- Success Response:
  - Code: 200 OK
    Content: { message: "OK" }
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR
    Content: { message: "Server error, try later" }

#### Edit note

Edit node by id.

- URL
  /edit-note/:id
- Method
  PUT
- URL Params
  id=[string]
- Data Params
  text=[string]
- Success Response:
  - Code: 200 OK
    Content: { message: "OK" }
- Error Response:
  - Code: 400 BAD REQUEST
    Content: { message: "Note is not found" }
    OR
  - Code: 500 INTERNAL SERVER ERROR
    Content: { message: "Server error, try later" }

#### Remove note

Remove note from list.

- URL
  /remove-note/:id
- Method
  DELETE
- URL Params
  id=[string]
- Data Params
  None
- Success Response:
  - Code: 200 OK
    Content: { message: "OK" }
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR
    Content: { message: "Server error, try later" }

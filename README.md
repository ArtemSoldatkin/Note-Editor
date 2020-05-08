# Note editor api (python / Flask)

**To start:**

docker-compose up -d --build

## API Documentation

#### Get notes

Returns all saved notes.

- URL <br />
  /get-notes
- Method <br />
  GET
- URL Params <br />
  None
- Data Params <br />
  None
- Success Response:
  - Code: 200 OK <br />
    Content: {notes: [{ <br />
    text: "text", <br />
    ID: "6b87d44f-d563-4ed5-961a-c5d67504e066", <br />
    date: { <br />
    year: 2020, <br />
    month: 5, <br />
    day: 8, <br />
    hour: 13, <br />
    minute: 26 <br />
    }, <br />
    changed: false <br />
    }]}
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR <br />
    Content: { message: "Server error, try later" }

#### Add note

Add note to list.

- URL <br />
  /add-note
- Method <br />
  POST
- URL Params <br />
  None
- Data Params <br />
  text=[string]
- Success Response: <br />
  - Code: 200 OK <br />
    Content: { message: "OK" }
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR <br />
    Content: { message: "Server error, try later" }

#### Edit note

Edit node by id.

- URL <br />
  /edit-note/:id
- Method <br />
  PUT
- URL Params <br />
  id=[string]
- Data Params <br />
  text=[string]
- Success Response:
  - Code: 200 OK <br />
    Content: { message: "OK" }
- Error Response:
  - Code: 400 BAD REQUEST <br />
    Content: { message: "Note is not found" } <br />
    OR <br />
  - Code: 500 INTERNAL SERVER ERROR <br />
    Content: { message: "Server error, try later" }

#### Remove note

Remove note from list.

- URL <br />
  /remove-note/:id
- Method <br />
  DELETE
- URL Params <br />
  id=[string]
- Data Params <br />
  None
- Success Response: <br />
  - Code: 200 OK <br />
    Content: { message: "OK" }
- Error Response:
  - Code: 500 INTERNAL SERVER ERROR <br />
    Content: { message: "Server error, try later" }

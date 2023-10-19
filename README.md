
## Mr. Fernandes' Athlete Record

#### This API keeps track of all SMIC athletes and their volleyball records. You can use API to find out the list of athletes or what a specific athlete's record is

In order to access these routes, you need to use an api key.
For all requests, you can use the api key as a query paramter with the key and value pair of:
```api_key=79sfhsieuhsi```

##### GET list of Athletes
Example Path:
```10.6.20.120:8000/athletes?api_key={API_KEY}```

Example Response:
```python
[
    "duke du",
    "hudson jones",
    "paul park",
    "adriaan cilliers",
    "henrik you",
    "samuel wu"
]
```

##### GET a Specific Athlete's Record
Example Path:
```10.6.20.120:8000/athletes/{athlete_name}?api_key={API_KEY}```

Example Response:
```python
{
    "name": "hudson jones",
    "games": "2",
    "points": "5"
}
```

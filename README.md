# Backend REST APIs for Song Data

This project provides a Django-based backend with REST APIs to serve normalized song data. The APIs are designed to fulfill the following use cases:

## Prerequisites

Make sure you have Python and Django installed on your machine. You can install the required packages using:

```bash
pip install -r requirements.txt
```
## Use Cases
#### 1. Get All Songs
Frontend can request all items in the normalized data set. Pagination is implemented for efficient data retrieval.

Endpoint:

GET /api/songs/

Parameters:

None

Response:

```json
{
  "count": 100,  // Total number of songs
  "next": "http://localhost:8000/api/songs/?page=2",  // URL for the next page, if available
  "previous": null,  // URL for the previous page, null if on the first page
  "results": [
    {
      "id": "5vYA1mW9g2Coh1HUFUSmlb",
      "title": "3AM",
      // ... other attributes
    },
    // ... additional songs
  ]
}
```
#### 2. Get Song by Title
Given a title as input, return all the attributes of that song.

Endpoint:

GET /api/song/title/{your_song_title}

Parameters:

title (string): The title of the song to retrieve.

Response:

```json
{
  "id": "5vYA1mW9g2Coh1HUFUSmlb",
  "title": "3AM",
  // ... other attributes
}
```

#### 3. Rate a Song
Users can rate a song using star rating (5 stars being the highest). This requires the normalized data to have an additional column for star rating.

Endpoint:

PUT /api/song/id/{song-id}

Parameters:

id (string): The ID of the song to be rated.
rating (integer): The star rating given by the user (1 to 5).

Response:

```json
{
  "id": "5vYA1mW9g2Coh1HUFUSmlb",
  "title": "3AM",
  "rating": 4,
  // ... other attributes
}
```

#### 4. Unit Tests
Unit tests are included to ensure the correctness of the API functionality.

Running the Server

To run the Django development server, execute the following command:

```bash
python manage.py runserver
```
The server will start at http://127.0.0.1:8000/.

Running Unit Tests

To run the unit tests, use the following command:

```bash
python manage.py test
```
This will execute the test cases and provide feedback on the test coverage and results.

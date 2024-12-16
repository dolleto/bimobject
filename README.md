# Wine Manager

Simple backend API with a datastore to service a frontend for a wine collection management application.
Project is implemented using Python and Django as it was the easiest for me.

## Pre-requisites

- Docker

## Set local environment

1. Build and start Docker containers:
```
docker-compose up --build
```
2. Run migrations:
```
docker-compose exec web python manage.py migrate
```

## Run tests

```
docker-compose exec web python manage.py test
```

## Further improvement ideas for the project

### API logic

- Implement permissions controls (admin, read only, ...).
- Improve requests validation messages (currently will return Django default validation messages).
- Consider a Cellar relation (a winemaker may have multiple cellars).

### Architecture

- Add NGINX reverse proxy (for load balancing, caching, traffic control, security).
- Cache endpoints (winemakers and wine bottles will not be updated frequently).
- Add Elasticsearch for improved search features and latency.
- Consider distributed DB for improved availability (and latency if multiple physical locations).

### Others

- Create API specification

## Example requests

The app is served locally on port 8000 (```http://localhost:8000/api/```).

1. Create a new winemaker:
```
curl -X POST http://localhost:8000/api/winemakers/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Château Margaux",
  "address": "Margaux, France"
}'
```

2. Get all winemakers:
```
curl -X GET http://localhost:8000/api/winemakers/
```

3. Update a winemaker:

```
curl -X PUT http://localhost:8000/api/winemakers/1/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Updated Château Margaux",
  "address": "Updated Address, France"
}'
```

4. Delete a winemaker:
```
curl -X DELETE http://localhost:8000/api/winemakers/1/
```

5. Create a new wine bottle (winemaker with provided ID must exist):

```curl -X POST http://localhost:8000/api/winebottles/ \
-H "Content-Type: application/json" \
-d '{
  "winemaker": 1,
  "name": "Margaux 2015",
  "year": 2015,
  "size": "750ml",
  "count_in_winecellar": 10,
  "style": "dry",
  "taste": "plum, tobacco",
  "description": "A full-bodied red wine.",
  "food_pairing": "Red meat, cheese",
  "link": "https://example.com/margaux-2015"
}'
```

6. Get All Wine Bottles
```
curl -X GET http://localhost:8000/api/winebottles/
```

7. Filter Wine Bottles by Style
```
curl -X GET "http://localhost:8000/api/winebottles/?style=dry"
```

8. Get Wine Bottles by Winemaker

```
curl -X GET "http://localhost:8000/api/winebottles/by_winemaker/?winemaker_id=1"
```

# StarNavi

## Installation

Build and run container in detach mode

```sh
docker-compose up --build -d
```
To run tests firstly we need to enter into django docker container.
```sh
docker-compose exec django bash
```
Then inside container run `pytest` command
```sh
pytest
```

If all tests passed then open swagger with all APIs and documentation
# [Swagger](http://0.0.0.0:8000/swagger/)
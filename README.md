# Build your own Jupyter Notebook Image

Taken from https://github.com/bcottman/dockerSeasons/tree/master/dev

## Compose all containers into one image
```bash
$ docker-compose build
```

## Run docker-compose image
```bash
$ docker-compose up
```

Open up the Jupyter Notebook in a browser
```bash
http://127.0.0.1:8888/?token=jkfdsuaire874312389ufdu894373yfdy8934 (example)

## Shut down docker-compose image
```bash
$ docker-compose down
```

Show all docker images
```bash
$ docker ps -a
```

Show all containers that can make images
```bash
$ docker images
```

Stop all docker images
```bash
$ docker rm $(docker ps -a -q)
```

Remove all stopped docker images
```bash
$ docker rm $(docker ps -a -q)
```

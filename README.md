# Project: Car plates detection 

## Build

```
docker build --pull --rm -f "Dockerfile" -t "carplatedetection:latest" "."
```

## Run

For debugging 
```
docker run -it carplatedetection:latest /bin/bash
```

For production:

```
docker run   -p 8508:8501 -d --name project1 carplatedetection:latest 
```

# Stop and remove 
Stop:
```
docker stop project1
```

Cleanup:

```
docker rm project1
```



# CONTRIBUTING

## How to run the Dockerfile locally

```
docker run -dp 5000:5000 --mount type=bind,src=$(pwd),target=/app IMAGE-NAME sh -c "flask run"
```

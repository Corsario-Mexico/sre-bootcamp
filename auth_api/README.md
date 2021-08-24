# Implementation Checklist
- [X] API Code
- [X] Services Code
- [X] Unit-tests
- [X] Dockerfile
- [X] It Compiles
- [X] It runs

# Api Services
- Receives a valid username and password and returns a JWT.
- Returns protected data with a valid token, otherwise returns unauthenticated.

# Docker image

```shell
docker build -t davidsol/public:wize-david-sol:latest .
```

# Execute docker

```shell
docker run -it --rm -p 8000:8000/tcp --name sre-app davidsol/public:wize-david-sol:latest
```

# Publish to docker

```shell
docker push davidsol/wize-david-sol
```

I didn't understand the instructions at first, until I found the Dockerfile stub

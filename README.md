# Portfolio Optimizer

This project is a portfolio optimization tool that consists of several services:

- **React Frontend**: Located in the `ui` folder, this is the user interface of the application.
- **Mutual Fund Scraper**: A Python service that scrapes mutual fund data.
- **Golang Backend Server**: The main backend server written in Go.
- **Brain Service**: A Python service responsible for performing analytics.

## Project Structure


### Run the data-service for development
Make sure redis is running in background using docker on host localhost:6379 with container name my-redis

```bash
docker run -d -p 6379:6379 --name my-redis redis:latest
```

```bash
flask --app main run --debug
```

Visualise redis 
```bash
docker run -d --name redisinsight -p 5540:5540 redis/redisinsight:latest
```

Get redis container ip for redisinsight
```bash
docker container inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" my-redis
```

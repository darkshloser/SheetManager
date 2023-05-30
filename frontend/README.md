# Frontend Client

## About technology stack

The User Interface is built with `Vue.js` one of the popular JavaScript frameworks. 
This UI Client is using also `router` to improve overall UX along with mitigating some of the unnecessary requests to the Backend. <br/>
It used `Vuex` as a state management pattern and library for VueJS.  It allows the developer to manage the state of the application in a centralized and predictable way, making it easier to reason about the code and make it more maintainable. With `Vuex`, the developer can store and manage data that needs to be shared between multiple components, as well as perform asynchronous operations and manage application-wide state.<br/>



## How to run the application

Developer can run the UI docker container separately from the rest of the containers or to run entire Docker composition.

1. Start frontend container individually
```sh
$ cd FullStack-OnePlatform-Challenge-Dobromir-Kovachev/frontend
$ docker build -t adverity-transformer-challenge-frontend -f Dockerfile.development .
$ docker run -it -p 8080:8080 --rm --name dockerize-vuejs-app-1 adverity-transformer-challenge-frontend
```

2. Start the entire Docker composition for the entire application
```
docker-compose up --build
```
In that case it will run the UI on http://127.0.0.1:8080/




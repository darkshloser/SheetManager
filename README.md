# Solution

## Design
![](./docs/images/Initial_Design.png "CSV Web App Design")

**Figure 1: Design overview**

The goal of that project is to prepare a simple application that will comply with the requirements below but also be well-designed in regard to simplicity, maintainability, and performance. 


The initial setup will be used for that solution with only one difference, which will be the additional Docker container for the Frontend (GUI) part of the project. The orchestration of the containers will be extended and improved with automatic procedures for a better development experience.


Users will be able to perform all the mentioned actions in the requirements below and more, but the backend will have a caching mechanism that will prevent unnecessary calls to the database and will improve the response time of `GET` requests to the backend. Caching will offload the backend and the application automatically will be able to handle more user requests without the introduction of load balancing.
If it’s necessary to reduce latency and maximize the throughput of the application at some point we could easily implement load balancing in the NGINX configuration which also serves the UI and can play as a reverse proxy.

The figure above illustrates how celery works with the Django backend, where the backend acts as a producer and workers as consumers waiting for tasks to be put in a queue so they can be consumed. For storage of tasks until consumed and to persist results of the task we use Redis.


## Implementation approach

### Steps
* Design data flow (what type of information will be stored and where)
* Specifications about models and views
* Implement REST API with Django REST Framework
* Integration with Redis via Celery
* Testing backend implementation
* Create new Docker container for Frontend Client (GUI)
* Implement initial structure, state management, and routing
* Implement a client to handle HTTP requests to Redis
* Finalize UI/UX 
* Simplify docker composition and orchestration

_NOTE: Dockerizing the application makes it more suitable for faster CI/CD implementation_

<hr/>

## Solution

### Setup
The application can be started by `docker-compose up` or use a `make` command for cleaning and a fresh start of the application like `make docker-reset-dev` which cleans only the containers and volumes related to that project.


### Functionality
There is additional functionality to the already defined and implemented requirements from the section below:
* Users can work with any *.csv content (not limited to the structure which was given at the beginning)
* *.csv documents can also be updated from the Table view
* *.csv documents can be removed from the application
* Enrichment of *.csv documents was extended to be able to handle also up to two Key Field pairs (it’s demonstrated also in the demo below)





<br/>


---
# Adverity Full-stack challenge

Hi! It's nice to see you here and all the best luck solving the challenge!
It based on simplified version of one of the day-to-day tasks we encounter at Adverity. 

To make the coding more pleasant for you, we've taken care of basic app bootstrap, please see `docker-compose.yaml` for details.
Feel free to use different setup, add additional packages, libraries, images as you wish.

We're interested in a clean solution for the problems described in the requirements list. Besides that, we'd be looking at your whole approach to applications development: performance, code & file structure, architecture & API design, etc.

The task is supposed to take around 8 hours to complete. Do not hesitate to prioritize functionality and/or adjust the complexity of your solution. We expect you to cover all the requirements. We'd ask you to complete the challenge within 14 days. Should that not work for you (vacation/workload/other obligations - life happens, right?), please inform our recruiter, and we'll find a tailor-made solution.

Please publish your solution as a github repository and send us a link.

## Running the app
In order to start the example application please use `docker-compose up` and visit http://localhost:8000 in your browser.

As we like Docker and simplicity, it would be great if your solution could be started with the same `docker-compose up`.

However, if you chose not to use Docker or running your app requires extra steps like running scripts, installing extra dependencies etc. please make sure to include clear instructions and requirements. **Please keep it as simple as possible.**

## App requirements

We would like you to create a simple application that would allow the users to upload, enrich and preview `.csv` files. 
The requirements are kept simple but please feel free to extend them and show us your skill as you please. 
You are given a freedom in structuring the UI and the number of views you develop - we love creativity!

---
### Requirement #1

*As a user I need to upload `.csv` file and be able to preview its content in a table*

Please use `users_posts_audience.csv` file for testing, it contains users' posts views data

### Requirement #2

*As a user I would like to see the list of all files I've uploaded, so I can choose the file I want to preview*

### Requirement #3

*As a user I would like to enrich my data file with additional details fetched from API endpoint*

- User should be able to input API endpoint for fetching external data, you can use following endpoints for testing:
https://jsonplaceholder.typicode.com/posts/, https://jsonplaceholder.typicode.com/users/
- User should be able to select key column name from data file that would be used for joining data, by default first column should be pre-selected
- User should be able to input key name for API response that would be used for the other side of join
- Based on selected keys, enriching should add all keys from the API response for each matching row as new columns  
- Enriching existing file should create a new file accessible in the listing from **Requirement #2**, original file should not be modified

## Extra hints
- We've prepared a basic setup including Django, Celery, Postgres and Redis but feel free to use different stack that you are more familiar with
- We encourage you to use a frontend framework of your choice, i.e. React, Vue
- How to start new React app: https://reactjs.org/docs/create-a-new-react-app.html
- How to start new Vue app: https://cli.vuejs.org/guide/creating-a-project.html#vue-create

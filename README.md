# URL Shortener Django App
* This Django application allows users to shorten URLs and retrieve the original URL using the shortened version. It's built using Django and Django Rest Framework.

## Installation
Clone this repository to your local machine:
> git clone https://github.com/ismcagilci/url_shortener_v2.git

Navigate to the project directory:
> cd url_shortener_v2

You can change url_shortener_value over from .env file, it is "ism.ca" as default

Run docker code
> docker-compose up --build

After docker started, you can reach to the app over port 8000

- We have two endpoints: base one "" (shorten_url,get all shorten_urls,delete all urls) and "/<shorten_url_value>"(you can get original url via using shortened url value and delete it).

- To test the app, you can use Postman or directly access it from the Django Rest Framework (DRF) panel

### In the project directory, you will find a Postman collection that includes all schemas necessary for using endpoints. Just import this collection to your postman.



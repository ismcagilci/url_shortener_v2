# URL Shortener Django App
* This Django application allows users to shorten URLs and retrieve the original URL using the shortened version. It's built using Django and Django Rest Framework.

## Installation
Clone this repository to your local machine:
> git clone https://github.com/ismcagilci/url_shortener_v2.git

Navigate to the project directory:
> cd url_shortener_v2

Run docker code
> docker-compose up --build

After docker started, you can reach the app over port 8000

- We have two endpoints: /url_shortener(you can shorten your url via this) and url_shortener/original_url(you can get original url via using shortened url).

- To test the app, you can use Postman or directly access it from the Django Rest Framework (DRF) panel

### In the project directory, you will find a Postman collection that includes all schemas necessary for using endpoints. Just import this collection to your postman.

<img width="938" alt="Screenshot 2024-02-13 000433" src="https://github.com/ismcagilci/url_shortener_v2/assets/50598846/08361b01-c8ee-4c6d-8110-d911b734e418">
<img width="944" alt="Screenshot 2024-02-13 000512" src="https://github.com/ismcagilci/url_shortener_v2/assets/50598846/c0f8ab5a-34ff-43d3-b813-3e0db1e7dd46">
<img width="953" alt="Screenshot 2024-02-13 000551" src="https://github.com/ismcagilci/url_shortener_v2/assets/50598846/1dec66db-aab9-497a-bd38-7ac1a9c69be8">
<img width="995" alt="Screenshot 2024-02-13 000727" src="https://github.com/ismcagilci/url_shortener_v2/assets/50598846/804a5a36-69a6-4327-bad1-3879caa730b7">
<img width="961" alt="Screenshot 2024-02-13 000745" src="https://github.com/ismcagilci/url_shortener_v2/assets/50598846/40909c1a-b14e-406e-a863-d0b4be1ccb5d">



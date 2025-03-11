## Notes:

* In a commercial setting I believe Alembic might be more useful to handle migrations, but in this simple scenario SQLAlchemy alone is great and easy.

* Generally speaking I like the ease of FastAPI but more recently have preferred aiohttp (mainly because I'm good friends with one of their leading open source contributors).

* I have added get by id and also an update user method, essentially completing generic crud operations, feels a little bare/useless without.

* Also added a logger, to inform the user what is happening, e.g. for issues/info.

* Added Postman collection & environment for ease of testing

* Added 1 unit test as an example. TBH, they're so simple I kinda think they're a waste of time for this exercise?

* Would also usually add some form of auth. But as this is for a 'non-technical' person, maybe they would struggle with
making requests a little. Simple API key could be useful, I suppose.

## To Run:

1. Ensure python is installed (I use 3.12)
2. Ensure docker is installed (use brew on mac for example)
3. Ensure docker daemon is running (e.g. on mac use docker desktop app)
4. Use `docker compose up`, which will pull pg image and run fastapi app locally.

## Tests

Wasn't sure what type of 'testing' would be preferred, so there is an example of a unit test which can be run with`pytest`. 
 As I mentioned above, feels a little futile to write them all, we can use our imagination.

Also added a postman collection for a more manual way of testing, but can visualise API functionality. To use,
download postman, import the collection + environment, then just make requests. Works like a curl would but with a ui.
The ID from the latest create user req will auto import into environment so you can instantly find original user or delete.

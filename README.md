# acq-stack-track-app
a tool for requesting and tracking acquisitions >$3500

* [journey map](https://docs.google.com/spreadsheets/d/1rRX4XlfVLRLJKiiyn5TvjDLAaOeiv8C2U5fh5O5HmvA/edit#gid=0)
* we're using "projects" feature for issue tracking
* slack channel is #acq-tts-intake
* team: Leah is product and design, Alan is dev, Steven is our boss
* stand up is 8:45am/11:45am daily

## Development

This is a Django app.

So far, we're using plain Django tests for unit testing and `behave` for feature specs.

### Running locally

Clone the repo and `cd` into it.

Then run:

```
$ docker-compose build
```

To spin up a local server:

```
$ docker-compose up
```

If using authentication, create a superuser:
```
docker-compose run web python manage.py createsuperuser --email example@whatever.gov --username example --noinput
```

To run tests and feature specs:

```
$ docker-compose run web ./bin/test
```

To run just unit tests:

```
$ docker-compose run web python manage.py test
```

To run just feature specs:

```
$ docker-compose run web python manage.py behave
```

## Deployment

This app runs on cloud.gov and is deployed via Travis CI. There are three env vars involved in the build: `CF_USERNAME`, `CF_PASSWORD`, and `CODECLIMATE_REPO_TOKEN`, all of which are stored via the Travis interface.

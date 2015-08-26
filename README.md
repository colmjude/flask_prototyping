# flask_prototyping

A simple flask prototyping tool.

### Dependencies

* Python 2.7
* Ruby 2.1.3+
* Sass 3.3.9+

### Building blocks

At the core it is a flask app so for those with python skills and if you are that way inclined you can add and extend to your heart's content.

For the rest of us looking to get some pages up and running quickly we can make use of the 3 govuk frontend building blocks.

* [govuk_template](https://github.com/alphagov/govuk_template) - template containing the GOV.UK header and footer, and associated assets
* [govuk_frontend_toolkit](https://github.com/alphagov/govuk_frontend_toolkit) - collection of Sass & JS 
* [govuk_elements](https://github.com/alphagov/govuk_elements) - design guide and example (adds some Sass components)

### Setup

I like to run things using virtualenv so the rest of my machine is kept decluttered so I always being by running

```
virtualenv flask
```

Next up install Flask and Flask-assets with the commands

```
flask/bin/pip install flask
flask/bin/pip install flask-assets
flask/bin/pip install gunicorn
```

Also run this so that ruby sass is installed

```
bundle install
```

If you are using virtualenv then `activate` that by entering:

```
source flask/bin/activate
```

And finally to run use the command

```
foreman start
```

Follow the instructions to view it in the browser


### Deploying to Heroku

For basic heroku instructions [see here](https://github.com/alphagov/govuk_prototype_kit/blob/master/docs/deploying.md)

There are a couple of additional steps required to deploy this project.

Because it is a python app that also requires ruby to compile the .scss files it needs multiple buildpacks. Luckily someone has made this easy for us, we just need to use the [heroku-buildpack-multi](https://github.com/ddollar/heroku-buildpack-multi)

Add a `.buildpack` file containing the 2 buildpacks

And then let Heroku know we are using this. We do that by entering this on the commandline

```
heroku buildpacks:set https://github.com/ddollar/heroku-buildpack-multi.git
```



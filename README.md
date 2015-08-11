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
```

Also run this so that ruby sass is installed

```
bundle install
```

And finally to run use the command

```
./run.py
```

Visit `http://127.0.0.1:5000/` to see the results



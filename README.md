## Problems encountered with this app:

1. Raise UndefinedValueError('{} not found. Declare it as envvar or define a default value.'

Solution: https://stackoverflow.com/questions/49216958/heroku-declare-it-as-envvar-or-define-a-default-value
You can set local env vars by adding them to a .env file, and then starting your development server via heroku local. This will convert all NAME=value lines from .env to env vars and make then available to your app. You can then add .env to your .gitignore, as this is only required on your local machine.

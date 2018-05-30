# reddit-clone

The app will allow any user to create a topic and upvote/downvote any topic.

## Setup

pip install -r requirements.txt

## Steps to run

python runserver.py

## Key features:

* Allow user creation by unique id
* Allow an existing user to create a topic
* Allow an existing user to upvote/downvote a topic
* Returns top 20 topics by upvotes

## Constraints

* All the data is stored in-memory, so app restart will remove previously created data
* User creation can only be done on a unique id
* Topic length should be less than 255 characters.
* Topic creation/upvote/downvote can be done by existing user.
* A user can upvote/downvote a topic any number of times.

## Error log

Logs will be generated in a file service.log. For any incorrect output, please check the error log.

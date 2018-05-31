# reddit-clone

The flask-app allows any user to create a topic and upvote/downvote any topic.

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

## In-memory database design

* There is one DataStore object that stores all the data about users, topics, upvotes and downvotes.
* Users can be created using unique id. A hash_map stores all the users with key as user_id and value as user_object.
* Topics are stored in a hash_map. For each new topic, a unique uuid is generated and is stored in a hash_map with key as id and value as topic content. 
* Upvotes and downvotes are stored separately using Counter which keeps the count of upvotes/downvotes against topic_id.
* Top 20 topics are displayed using Counter inbuilt function most_common.

## Curl Requests:

### Create user


### Create topic

### Upvote a topic


### Downvote a topic

### Get a topic by id

### Get most upvoted topics

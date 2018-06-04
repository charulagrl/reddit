# reddit-clone

The flask-app allows any user to create a topic and upvote/downvote any topic.

## Setup

pip install -r requirements.txt

## Steps to run

python runserver.py

## Run test cases

pytest --setup-show tests/

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

## UI Design
* The user should login/signup first before creating a topic/upvote/downvote.
* Logout user will be redirected to login page if they go to login/upvote/downvote/signout page.
* Only user_id is required for signup/login page.
* Home page displays all the topics sorted by upvotes.
* All topics page displays all the topics.

## Curl Requests:

### Create user

curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-Type:application/json" \
   -d \
'{"user_id": <userId>}' \
 'https://reddit-clone1.herokuapp.com/signup'

 e.g.

 curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-Type:application/json" \
   -d \
'{"user_id": "charul"}' \
 'https://reddit-clone1.herokuapp.com/signup'

### Create topic

curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-Type:application/json" \
   -d \
'{"user_id": <userId>, "content": <content>}' \
 'https://reddit-clone1.herokuapp.com/topic'

e.g.
curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-Type:application/json" \
   -d \
'{"user_id": "charul", "content": "test"}' \
 'https://reddit-clone1.herokuapp.com/topic'

### Upvote a topic

curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-type:application/json" \
   -d \
'{"user_id": <userId>}' \
 'https://reddit-clone1.herokuapp.com/upvote/<topicId>'

 e.g.
 curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-type:application/json" \
   -d \
'{"user_id": "a1"}' \
 'https://reddit-clone1.herokuapp.com/upvote/0100de81-b3e2-4785-99d2-29062b699c41'

### Downvote a topic

curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-type:application/json" \
   -d \
'{"user_id": <userId>}' \
 'https://reddit-clone1.herokuapp.com/downvote/<topicId>'

 e.g.
 curl -i -X POST \
   -H "Accept:application/json" \
   -H "Content-type:application/json" \
   -d \
'{"user_id": "a1"}' \
 'https://reddit-clone1.herokuapp.com/downvote/0100de81-b3e2-4785-99d2-29062b699c41'

### Get a topic by id

curl -i -X GET \
   -H "Accept:application/json" \
   'https://reddit-clone1.herokuapp.com/topic/<topicId>'

e.g.

curl -i -X GET \
   -H "Accept:application/json" \
   'https://reddit-clone1.herokuapp.com/topic/c213b408-0db3-45f0-905a-52799d1e1312'

### Get most upvoted topics

curl -i -X GET \
   -H "Accept:application/json" \
   'https://reddit-clone1.herokuapp.com/home'

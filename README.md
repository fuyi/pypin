# pypin
A simple Python client for Pinterest API

## How to use

1. Grab a Pinterest access token from [Access token generator](https://developers.pinterest.com/tools/access_token/)
2. Clone this package, Install it locally
```
git clone git@github.com:fuyi/pypin.git
cd pypin
pip install -e .
```
2. Import module pypin from your code
```
from pypin import PyPin
```

3. Instantiate a PyPin object with your access token from step 1
```
client = PyPin('<your access token>')
```

4. Now you can use this client to interact with Pinterest API
```
client.me()
```

## Feature TODO List

* ~~Get the authenticated user's Pinterest account info~~
* Get the pins that the authenticated user likes
* Get the authenticated user's followers
* Get the boards that the authenticated user follows
* Get the Pinterest users that the authenticated user follows
* Get the interests that the authenticated user follows
* Follow a user
* Unfollow a user
* Follow a board
* Unfollow a board
* Follow an interest
* Unfollow an interest
* Get all of authenticated users's pins
* Get all of authenticated users's boards
* Get the account info for a Pinterest user
* Create a pin on a board

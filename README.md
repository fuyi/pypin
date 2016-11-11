# pypin
A simple Python client for [Pinterest API](https://developers.pinterest.com/docs/api/overview/)

## How to use

1. Grab a Pinterest access token from [Access token generator](https://developers.pinterest.com/tools/access_token/)
2. Clone this package, Install it locally
```
git clone git@github.com:fuyi/pypin.git
cd pypin
pip install -e .
```
3. Import module pypin from your code
```
from pypin import PyPin
```

4. Instantiate a PyPin object with your access token from step 1
```
client = PyPin('<your access token>')
```

5. Now you can use this client to interact with Pinterest API
```
client.me()
```

## Feature TODO List

* ~~Get the authenticated user's Pinterest account info~~

```
client.me()
```

* ~~Get all of authenticated users's boards~~

```
client.get_boards()
```

* ~~Create a new board~~

```
client.create_board({'name': '<board name>'})
```

* ~~Create a pin on a board, only support url, will add image file support soon~~

```
client.create_pin({
    'board': '<board name>',
    'note': '<your note>',
    'link': '<url to be posted>',
    'image_url': '<image url to be posted>'
})
```

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
* Get the account info for a Pinterest user


## Tech TODO List

* Add input data validator
* Add returned fields
* Add tests

# pypin
A simple Python client for <a href="https://developers.pinterest.com/docs/api/overview/" target="_blank">Pinterest API</a>

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
client.get_me()
```

## Feature TODO List

* Get the authenticated user's Pinterest account info

```
client.get_me()
```

* Get all of authenticated users's boards

```
client.get_boards()
```

* Create a new board

```
client.create_board({'name': '<board name>'})
```

* Create a pin on a board, only support url, will add local image file support soon

```
client.create_pin({
    'board': '<board name>',
    'note': '<your note>',
    'link': '<url to be posted>',
    'image_url': '<image url to be posted>'
})
```

* Get the pins that the authenticated user likes

```
client.get_likes()
```

* Get the authenticated user's followers

```
client.get_followers()
```

* Get the boards that the authenticated user follows

```
client.get_following_boards()
```

* Get the Pinterest users that the authenticated user follows

```
client.get_following_users()
```

* Get the interests that the authenticated user follows

```
client.get_following_interests()
```

* Follow a user

```
client.follow_user(user_name)
```

* Unfollow a user

```
client.unfollow_user(user_name)
```

* Follow a board


```
client.follow_board(board_id)
```

* Unfollow a board

```
client.unfollow_board(board_id)
```

* Get all of authenticated users's pins

```
client.get_pins()
```

TODO

## Tech TODO List

* Python2.7 compatibility
* Add input data validator
* Add returned fields
* Add model layer
* Add tests

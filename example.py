"""client script"""
from pypin import PyPin

API_CLIENT = PyPin('AaCHGJ_asIYl_ii3b_gjG5Z9eVadFIM74OdBtXZDgcHF8cA-hAAAAAA')

print API_CLIENT.get_me()

print API_CLIENT.get_boards()

# print API_CLIENT.create_board({'name': 'test3'})

# print API_CLIENT.create_pin({
#     'board': 'yvesfu/test3',
#     'note': 'a new pin',
#     'link': 'https://www.spartasales.com',
#     'image_url': 'http://img.over-blog-kiwi.com/0/86/68/47/20140304/ob_9b442c_baby-115a.jpg'
# })

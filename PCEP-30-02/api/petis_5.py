from requests import Session

s = Session()
url = 'https://jsonplaceholder.typicode.com/comments'

params = {'postId': 1}

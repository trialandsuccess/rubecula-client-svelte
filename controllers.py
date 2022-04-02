from rubecula import web, websocket, static, template, console
from rubecula.config import config
from rubecula.ws import Client


# / is currently just a static index.html,
# but you can change this by naming a method 'index'

@web('get')
def welcome():
    return "Welcome to Rubecula!"

# define your other routes here

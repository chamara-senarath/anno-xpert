from views.collections_view import collections_view
from views.home_view import home_view

frames = {}

def control_frame_init(container):
    frames['collection'] = lambda:collections_view(container,change_frame)
    frames['home'] = lambda:home_view(container,change_frame)
    change_frame('home')

def change_frame(frame_name):
    frames[frame_name]().tkraise()

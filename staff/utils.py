from django.db.models import Count
from datetime import datetime
from os.path import splitext

from .models import *

menu = [{'title': "HOME", 'url_name': 'home'},
        {'title': "ADD", 'url_name': 'add_page'},
        {'title': "FEEDBACK", 'url_name': 'contact'}
        
        
    
]

class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        return context
    


def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
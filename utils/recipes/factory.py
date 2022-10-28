# from inspect import signature
from random import randint
def rand_ratio():
    return randint(840, 900), randint(473, 573)

def make_recipe():
    return {
        'title': 'arroz',
        'description': 'Fazendo arroz',
        'preparation_time': '2',
        'preparation_time_unit': 'Minutos',
        'servings': '4',
        'servings_unit': 'Porção',
        'preparation_steps': 'lorem ksjkapsnjknasdksnajkdsjdhsjk ksdk ksjdks k sdjkas sdkjd skdjsd ksjd skdjskdj ',
        'created_at': '21-05-2021 00:00:00',
        'author': {
            'first_name': 'Wemerson',
            'last_name': 'Gomes',
        },
        'category': {
            'name': 'teste'
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())
import os
import sys

def utils_module():
    """ Add utils module to path """
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('testes', 'utils'))
    import utils
    return utils
module = utils_module()

def email_teste(email_value):
    email = module.Email(email_value)
    print('=================================')
    if email.is_valid():
        print('email Valid')
    else:
        print('email Invalid')


if __name__ == '__main__':
    email_value= 'test@mail.com'
    email_teste(email_value)

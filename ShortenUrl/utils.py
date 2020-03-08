import string
import random

def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_order_id_generator(ShortUrl):
    new_short_url= random_string_generator()
    qs_exists= ShortUrl.objects.filter(short_url= new_short_url).exists()
    if qs_exists:
        return unique_order_id_generator()
    return new_short_url
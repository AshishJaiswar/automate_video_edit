import requests
import textwrap


def quote_generator(quote_length=150):
    '''
        Getting data from the API.
        data: {'_id': 'PbtLxWdzTk7F', 
                'tags': ['famous-quotes'], 
                'content': 'It is easier to live through someone else than to become complete yourself.', 
                'author': 'Betty Friedan', 
                'authorSlug': 'betty-friedan', 
                'length': 75, 
                'dateAdded': '2019-06-27', 
                'dateModified': '2019-06-27'}
    '''
    api = f"https://api.quotable.io/random?maxLength={quote_length}"
    response = requests.get(api)
    data = response.json()
    return data


def quote_formatter(quote):
    '''
        This function will format the text.
        Convert long single line text into multiple lines
        Ex: 
        text: A quick brown fox jump over the lazy cat
        output: A quick brown fox
                jump over the lazy
                cat
    '''
    wrapper = textwrap.TextWrapper(width=35)
    word_list = wrapper.wrap(text=quote)

    result = "\n".join(word_list)
    return result

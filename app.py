from src.quotes import *
from src.edit import video_editor


# -------------------------- Quotes -----------------------------------
# default length of quote is 150. Can pass length argument into
# quote_generator
data = quote_generator()
quote = data['content']
formated_quote = quote_formatter(quote)
author = data['author']

video_editor(formated_quote, author)
print("Sucessfull :)")

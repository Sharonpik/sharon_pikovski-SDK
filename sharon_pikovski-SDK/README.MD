# Overview
This is a basic SDK for [The One API](https://the-one-api.dev). The API is an open-source API for Lord of The Rings and The Hobbit information, including movies, books, quotes and characters information.

The SDK creates an easy way to communicate with the API. It does most of the heavy lifting for you.
If the API was the ring, this SDK would be Frodo and Sam carrying it for you.

# Getting started
## First Step
You will not be able to use this sdk if you do not obtain a bearer token from the API site.
Make sure to get it here: [https://the-one-api.dev/sign-up](https://the-one-api.dev/sign-up)

## Compatibility
Your project needs to use a Python version of 3.9.2 or later.

## Installation
To install, use `pip`:
> pip install my-name-sdk

## Initialize Token
Before you start anything, make sure to call initToken() with your token. This will initialize the SDK with you token.

>from lotr_sdk import init_token

And then call initToken("your-token-here")
Now we're set to go!

## Logging
Logs are being sent to sdk.log. If you're stuck, take a look there!

# Examples Of How To Use
## Books

To return all available books, you can just call getAllBooks() like so:
```python
from lotr_sdk import books
print(books.getAllBooks())
```
To get a book by it's name:
```python
from lotr_sdk import books
print(books.getBookByName("The Fellowship Of The Ring"))
```

And to get all the chapters for this book:
```python
from lotr_sdk import book
books.getBookChapters(books.getBookByName("The Fellowship Of The Ring"))
```
# List of All Functions
You can import 5 modules: books, chapters, characters, movies, quotes

## Books Functions:
```python
Book(str id, str name, list chapters) #returns Book object
getBookChaptersById(str id) #returns a Book object
getAllBooks(params={}) #returns a list of Book objects
getBookByName(str name) #returns a Book object
getBookChaptersById(str id) #returns {"status" : str, "total" : int, "chapters": list of Chapters}
getBookChapters(Book book) #returns {"status" : str, "total" : int, "chapters": list of Chapters} and updates book.chapters
getBooksByRegex(str option, str regex) #returns a list of Book objects
```

## Chapters Functions:
```python
Chapter(str id, str chapterName, str bookid) # returns Chapter object
getAllChapters(params={}) # returns a list of Chapter objects
getChapterById(str id): # returns Chapter object
getChapterByName(str name) # returns Chapter object
getSortedChapters(str sortBy, str sortType) # returns a list of Chapter objects
getChapterByRegex(option, regex) #returns a list of Book objects
```

## Characters Functions
```python
Character(str id, str height, str race, str gender, str birth, str spouse, str death, str realm, str hair, str name, str wikiUrl) #returns Character Object
getAllCharacters(params={}) # returns a list of Character objects
getCharacterByName(str name) # returns Character object
getCharacterById(str id) # returns Character object
getCharacterQuotes(Character character, params={}) # returns a list of Quotes 
getCharacterQuotesById(str id, params={}) # returns a list of Quotes 
getCharacterQuotesByName(str name, params={}) # returns a list 
getAllCharacterWithoutSome(list names) # returns a list without the list of names provided
getAllCharactersByOption(str option, str option_value) # returns a list of Chapter objects
getSortedCharacters(str sortBy, str sortVal) # returns a list of Chapter objects. Ex sortBy="name", sortVal = "asc"
getCharacterByRegex(str option,str regex) # returns a list of Chapter objects. Ex option = "name", regex="/foot/i"
```

## Movies Functions
```python
Movie(str id, str name, int run_time_minutes, int budget_millions,
        int box_office_revenue_millions, int academy_award_nominations,
        int academy_award_wins, float rotten_tomatoes_score) #returns Movie Object
getAllMovies(params = {}) #returns a list of Movie Object
getAllMoviesSorted(str sortBy,str sortType) # returns a list of Movie objects. Ex sortBy="name", sortVal = "asc"
getMovieById(str id) #returns Movie Object
getMovieByName(str name) #returns Movie Object
getMoviesByComparison(str option, str symbol, str val) # Ex option = "rotten_tomatoes_score", symbol = "<", val= "90"
getMoviesByRegex(option, regex) # returns a list of Movie objects. Ex option = "name", regex="/foot/i"
```

## Quotes Functions
```python
Quote(str id, str dialog, str movieid, str characterid) #returns Quote Object
getAllLotrQuoates(params={}) #returns a list of Quote Objects
getQuoteById(str id) #returns Quote Object
getQuotesSorted(sortBy, sortType) # returns a list of Quote objects. Ex sortBy="dialog", sortVal = "desc"
getQuotesByRegex(option, regex) # returns a list of Quote objects. Ex option = "dialog", regex="/foot/i"
getLimitedQuotes(int limit)# returns a list of Quote objects that is limited amount
```


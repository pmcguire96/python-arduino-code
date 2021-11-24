print("Testing using the Matrix")

from imdb import IMDb

# create an instance of the IMDb class
movieDB = IMDb()

# get a movie and print its director(s)
the_matrix = movieDB.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(movieDB.get_movie_infoset())

# update a Movie object with more information
movieDB.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))
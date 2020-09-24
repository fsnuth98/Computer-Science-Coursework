'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 13
Part 4: Top 50 Movies List
April 28 2017
'''

movies = [
    "2782275172,Avatar,2009",
    "2186772302,Titanic,1997",
    "1518594910,Marvel's The Avengers,2012",
    "1341511219,Harry Potter and the Deathly Hallows _ Part 2,2011",
    "1215439994,Iron Man 3,2013",
    "1169229000,Frozen,2013",
    "1123794079,Transformers: Dark of the Moon,2011",
    "1119929521,The Lord of the Rings: The Return of the King,2003",
    "1108561013,Skyfall,2012",
    "1084439099,The Dark Knight Rises,2012",
    "1066179725,Pirates of the Caribbean: Dead Man's Chest,2006",
    "1063171911,Toy Story 3,2010",
    "1045713802,Pirates of the Caribbean: On Stranger Tides,2011",
    "1029153882,Jurassic Park,1993",
    "1027044677,Star Wars Episode I: The Phantom Menace,1999",
    "1024299904,Alice in Wonderland,2010",
    "1017003568,The Hobbit: An Unexpected Journey,2012",
    "1004558444,The Dark Knight,2008",
    "987483777,The Lion King,1994",
    "974755371,Harry Potter and the Philosopher's Stone,2001",
    "970761885,Despicable Me 2,2013",
    "963420425,Pirates of the Caribbean: At World's End,2007",
    "960283305,Harry Potter and the Deathly Hallows _ Part 1,2010",
    "953066855,The Hobbit: The Desolation of Smaug,2013",
    "939885929,Harry Potter and the Order of the Phoenix,2007",
    "936743261,Finding Nemo,2003",
    "934416487,Harry Potter and the Half-Blood Prince,2009",
    "926047111,The Lord of the Rings: The Two Towers,2002",
    "919838758,Shrek 2,2004",
    "896911078,Harry Potter and the Goblet of Fire,2005",
    "890871626,Spider-Man 3,2007",
    "886686817,Ice Age: Dawn of the Dinosaurs,2009",
    "878979634,Harry Potter and the Chamber of Secrets,2002",
    "877244782,Ice Age: Continental Drift,2012",
    "871530324,The Lord of the Rings: The Fellowship of the Ring,2001",
    "864565663,The Hunger Games: Catching Fire,2013",
    "848754768,Star Wars Episode III: Revenge of the Sith,2005",
    "836303693,Transformers: Revenge of the Fallen,2009",
    "829685377,The Twilight Saga: Breaking Dawn _ Part 2,2012",
    "825532764,Inception,2010",
    "821708551,Spider-Man,2002",
    "817400891,Independence Day,1996",
    "798958162,Shrek the Third,2007",
    "796688549,Harry Potter and the Prisoner of Azkaban,2004",
    "792910554,E.T. the Extra-Terrestrial,1982",
    "788679850,Fast & Furious 6,2013",
    "786636033,Indiana Jones and the Kingdom of the Crystal Skull,2008",
    "783766341,Spider-Man 2,2004",
    "775398007,Star Wars,1977",
    "769679473,2012,2009"]

count = 0
search_title = input("Enter partial title  of the movie: ")
for i in range(len(movies)):
    movie_info = movies[i].split(',')
    if movie_info[1].startswith(search_title):
        print(movie_info[1])
        count += 1

if count == 0:
    print("No movies found.")
else:
    print("Found", count, "matches.")
    

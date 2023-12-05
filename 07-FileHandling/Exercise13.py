movie_titles=["Frozen", "Fast&Furious", "Top Gun", "Avengers", "Pirates of Caribbean"]

file = open("movies.txt", "w")
for name in movie_titles:
    file.write(name+"\n")

file.close()
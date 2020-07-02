import wikipedia

what_do_u_want = input("What do you want to search on Wikiepdia? ")
query = wikipedia.page(what_do_u_want)
print(query.summary)

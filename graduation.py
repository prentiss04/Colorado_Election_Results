#graduation

invitees = ['jaNe thoPson'', SOREN Blief', 'jimmy', 'bill watErs', 'rachel']

# First use list comprehensions to creat a new list that contains the lowercase
# version of each of the anmes your user provided

lower_case = []
lower_case = [invitee.lower() for invitee in invitees]

print (lower_case)

# Then, use list comprehensions to creat a new list that contains the title-cased 
#versions of each of the anmes in your lower-cased list. 

titlecase = [guest.title() for guest in invitees]
print (titlecase)


# bonus
fulltitleCase = [letter.title() for letter in invitees]
print (fulltitleCase)
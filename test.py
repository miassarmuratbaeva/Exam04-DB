from datetime import date
from library.create_tables import init_db
from datetime import datetime
from library.crud import create_author , get_author_by_id, get_all_authors, update_author, delete_author, create_book







init_db()



#new_author = create_author(name="Abdullo", bio="Oripov")
#print( new_author.id, new_author.name, new_author.bio)


# new_author = create_author(name="Abdullo", bio="Oripov")

#found_author = get_author_by_id(new_author.id)
#if found_author:
 #   print("Author topildi!")
  #  print("ID:", found_author.id)
   # print("Name:", found_author.name)
    #print("Bio:", found_author.bio)
#else:
 #   print("Author topilmadi.")

#create_author(name="Abdullo", bio="Oripov")
#create_author(name="Ali", bio="Valiyev")

#authors = get_all_authors()


#for author in authors:
 #   print(f"ID: {author.id}, Name: {author.name}, Bio: {author.bio}")
#new_author = create_author(name="Abdullo", bio="Oripov")
#author = create_author("Abdullo", "Oripov")
#print("Oldingi:", author.name, author.bio)


#updated_author = update_author(author.id, bio="Yangilangan bio")
#print("Yangilangan:", updated_author.name, updated_author.bio)
 


#author = create_author("Abdullo", "Oripov")
#print("Yaratilgan author ID:", author.id)

#result = delete_author(author.id)
#print("Ochirildi:", result)
#author_check = get_author_by_id(author.id)
#print("Author topildi:", bool(author_check))

author = create_author("Abdullo", "Oripov")

book = create_book(
    title="Shohnoma",
    author_id=author.id,
    published_year=2023,
    isbn="1234567890"
)

print("Book ID:", book.id)
print("Title:", book.title)
print("Author ID:", book.author_id)
print("Year:", book.published_year)
print("ISBN:", book.isbn)
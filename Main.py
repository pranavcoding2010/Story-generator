import random
When = ['A few years ago','Yesterday','Few days ago','Last night','On 20th jan']
Who = ['Cat','Dog','turtel','Elephent','Tiger','crocodile']
Name = ['Jack','Tom','Alex','Brent','Andrew','Alen']
Residence = ['India','London','Usa','United Kingdom','Singapore']
Went=['Park','Cinema','Laundry','Resturant','Hotel','office']
Happened = ['Made a lot of friends','Ate a burger','Found a secret key','Solved a mystry','Wrote a book']
print(random.choice(When) + ', ' + random.choice(Who) + ' that lived in ' + random.choice(Residence) +
', went to the ' + random.choice(Went) + ' and ' + random.choice(Happened))

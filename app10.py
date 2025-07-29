import pandas as pd
df = pd.read_csv(r'C:\Users\KANNAN\Downloads\Netflix\netflix_titles.csv')
df = df.fillna('Unknown')
try:
 def Netflix(df):
     print("Hi! I'm Your Personal Netflix Filteration System")
     print("Here You can Filter A Variety of Movies Or TV Shows According To your Liking or Leave Blank.\nLets Get Started!")
     video_type = input("Which Type would You Like, Movie Or TV Show: ") or None
     director = input("Which Director would You Like it to be Directed By: ") or None
     actor = input("Which Actor would You Like To Be In It: ") or None
     country = input("Which Country would You Like It To be From: ") or None
     year = input("Which Year Should It be Released On: ") or None
     age_rating = input("Which Age Rating Should It Be For: ").upper() or None
     genre = input("Which Genre would You Like It: ") or None
     if video_type:
         df = df[df['type'].str.contains(video_type, case=False)]
     if director:
         df = df[df['director'].str.contains(director, case=False)]
     if actor:
         df = df[df['cast'].str.contains(actor, case=False)]
     if country:
         df = df[df['country'].str.contains(country, case=False)]
     if year:
         df = df[df['release_year'] == year]
     if age_rating:
         df = df[df['rating'].str.contains(age_rating, case=False)]
     if genre:
         df = df[df['listed_in'].str.contains(genre, case=False)]
     if df.empty:
         print("No Movies Found With These Filters")
     else:
         print(f"Found {len(df)} Movies With These Filters, Showing Top Ten Results:\n")
         print(df[['show_id', 'title', 'type']].head(10))
 Netflix(df)
except ValueError:
    print("Please Enter A Valid Year")









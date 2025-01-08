class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   
   def __str__(self):
      return(f'Performer: {self.performer}\n'
             f'Album: {self.album}\n'
             f'Title: {self.title}\n' 
             f'Year; {self.year}\n')

# object creation
song1 = Song('Ed Sheran',"Hearts Don't Break Around Here","Divide",2017)
song2 = Song('Queen', 'Bohemian Rhapsody', 'A Night at The Opera', 1975)

## object usage
print(song1)
print()
print(song2)
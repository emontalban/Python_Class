class Language:

    def __init__(self, name, year, type, extension, creator):
        self.name = name
        self.year = year
        self.type = type
        self.extension = extension
        self.creator = creator

    def __str__(self):
        return (f'Language {self.name} was created by {self.creator} in the year {self.year}, it is of type {self.type} and has an extension {self.extension}')
    
    def __repr__(self):
        return(f'Language: {self.name}, {self.creator}, {self.year}, {self.type}, {self.extension}')

language_one = Language('Python', 1991,'interpretado','.py','Guido van Rossum')    
language_two = Language('Ruby', 1995, 'interpretado', '.rb', 'Yukihiro Matsumoto')
print(str(language_one))
print(repr(language_two))
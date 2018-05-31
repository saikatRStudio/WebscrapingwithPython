from requests import get
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250_6'
response = get(url)

print(response.text[:500])

from bs4 import BeautifulSoup

html_soup = BeautifulSoup(response.text, 'html.parser')

type(html_soup)
movie_containers = html_soup.find_all('td', class_='titleColumn')

print(type(movie_containers))

print(len(movie_containers))

first_movie = movie_containers[0]
first_movie

first_movie.div

first_movie.a

first_movie.href

first_movie.title

first_name = first_movie.text.replace("\n","").replace(" ","")
first_name

movie_year = html_soup.find_all('span', class_='secondaryInfo')

movie_year



# Lists to store the scraped data in
names = []
years = []


# Extract data from individual movie container
for container in movie_containers:

    # If the movie has Metascore, then extract:
    if container.find('span', class_ = 'secondaryInfo') is not None:

        # The name
        
        name = container.text.replace("\n","").replace(" ","")
        names.append(name)

        # The year
        year = container.span.text
        years.append(year)

       
import pandas as pd

test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       })
print(test_df.info())
test_df
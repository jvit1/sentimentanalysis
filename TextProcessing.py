import pandas as pd

df = pd.read_csv('Scraped_Tweets.csv')
df = df[['User Location']]

# Australia
australia_cities = "Queensland|Sydney|Australia|Melbourne"
df.loc[df['User Location'].str.contains(australia_cities, case=False, na=False), 'User Location'] = 'Australia'

# Bangledesh
bangladesh_cities = "Satkhira|Bangladesh"
df.loc[df['User Location'].str.contains(bangladesh_cities, case=False, na=False), 'User Location'] = 'Bangladesh'

# Brazil
brazil_cities = "Goiânia|Janeiro|Brasil|Brazil|Sao Paulo"
df.loc[df['User Location'].str.contains(brazil_cities, case=False, na=False), 'User Location'] = 'Brazil'


# Canada
canada_cities = "Toronto|Ontario|Canada|Vancouver|Ottawa|Montréal|Québec|Alberta"
df.loc[df['User Location'].str.contains(canada_cities, case=False, na=False), 'User Location'] = 'Canada'

# Cyprus
cyprus_cities = "Ayia"
df.loc[df['User Location'].str.contains(cyprus_cities, case=False, na=False), 'User Location'] = 'Cyprus'


# France
france_cities = "France|Paris"
df.loc[df['User Location'].str.contains(france_cities, case=False, na=False), 'User Location'] = 'France'


# Indonesia
indonesia_cities = "Jakarta|Indonesia|Bekasi|Java|Jawa"
df.loc[df['User Location'].str.contains(indonesia_cities, case=False, na=False), 'User Location'] = 'Indonesia'

# India
india_cities = "Mumbai|India|bangalore|Nairobi|New Delhi"
df.loc[df['User Location'].str.contains(india_cities, case=False, na=False), 'User Location'] = 'India'

# Kenya
kenya_cities = "Kisumu"
df.loc[df['User Location'].str.contains(kenya_cities, case=False, na=False), 'User Location'] = 'Kenya'

# Nigeria
nigeria_cities = "Nigeria"
df.loc[df['User Location'].str.contains(nigeria_cities, case=False, na=False), 'User Location'] = 'Nigeria'


# Philippines
pilippines_cities = "Caloocan"
df.loc[df['User Location'].str.contains(pilippines_cities, case=False, na=False), 'User Location'] = 'Philippines'

#South Africa
south_africancities = "Midrand|South Africa"
df.loc[df['User Location'].str.contains(south_africancities, case=False, na=False), 'User Location'] = 'South Africa'


# Thailand
thailand_cities = "Bangkok"
df.loc[df['User Location'].str.contains(thailand_cities, case=False, na=False), 'User Location'] = 'Thailand'


# United States
us_cities = "Angeles|York|Greenville|Michigan|Tampa|Fayetteville|Antonio|Manhattan|USA|Boston|Detroit|United States|" \
            "Dallas|Oklahoma|Jersey|Chicago|Albuquerque|Orlando|NYC|San Francisco|Leesburg|Ohio|Miami|Stamford|SEATTLE|" \
            "TX|Gainesville|Denver|Bay Area|Philly|Florida|KY|St Joseph|Vegas|Providence|Myrtle|Pennsylvania|Washington|Richmond|" \
            "Texas|Savannah|Salt Lake|New Orleans|Cary|Long Island|Concrete Jungle|united state|colorado|" \
            "grand rapids|Louisville|Charlotte|Atlanta|Jacksonville|Inglewood|Scottsdale|Palm Beach|Columbus|Kansas City|" \
            "California|Palo Alto|Columbus|Roanoke|Durham|Rochester|Beverly Hills|Utah|America|Madison|Philadelp|Hollywood|" \
            "Boca Raton|Portland|Nashville|Tacoma|Wellington|Bethesda|Roseville|Bristol|Lafayette|San Diego|Night City|" \
            "Lauderdale|Wildwood|NJ|San Jose|TN|Hawaii|Brooklyn|Bethlehem|Orange County|Birmingham|Virginia|FL|Victoria|" \
            "Silicon Valley|Brookline|Allentown|Pasadena|Queens|Nevada|Santa Clara|Lancaster|Bellevue|Marina del|Rockville|" \
            "Darien"
df.loc[df['User Location'].str.contains(us_cities, case=False, na=False), 'User Location'] = 'United States of America'

#United Kingdom
uk_cities = "London|Liverpool|England|Scotland|UK|Ireland|United Kingdom|Wales"
df.loc[df['User Location'].str.contains(uk_cities, case=False, na=False), 'User Location'] = 'United Kingdom'


df.to_csv("LOCTEST.csv", header=False)

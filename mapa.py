#%% Imports
import requests
# %%

response = requests.get("https://restcountries.com/v3.1/region/europe")
response.status_code
# %%
europe = {
    c['cca3']:{
        'name': c['name']['common'],
        'borders': c['borders'],
    }
    for c in response.json()
    
    if 'borders' in c
}

##comprehensions - přepis smyčky
europe
# %% Save

import pickle

with open('europe.pkl', mode='bw') as f:
    pickle.dump(europe, f)

# %%
#.....
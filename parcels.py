#%% imports

from typing import NamedTuple
from random import sample

# %%

class Parcel(NamedTuple):
    location: str
    destination: str

Parcel('CZE', 'DEU')

# %% random parcels

def randomParcels(n: int, codes: list[str]) -> list[Parcel]:
    return[
        Parcel(*sample(codes, 2))
        for _ in range(n)
    ]
        
randomParcels(10, ['A', 'B', 'C', 'D'])


# %%

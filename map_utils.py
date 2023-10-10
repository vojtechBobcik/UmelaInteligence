
#%% 
def neigbour(code: str, maps:dict) -> list:
    try:
        borders = maps[code]['borders']
        return{
            k:c 
            for k,c in maps.items()
            if k in borders
        }
    except:
        raise ValueError()
    
    

# %%

if __name__=="__main__":
    import pickle
    with open('europe.pkl', mode='br') as f:
        maps = pickle.load(f)
        
    
# %%
print(neigbour('CZE', maps))
# %%

#%%
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x,2)
        self.y = round(y,2)

#%%
vector = Vector(-2.343, 8.008)

# %%
vector.x
vector.y
import pandas as pd
players = {
    "player":["prashant", "patti","messi","haaland"],
    "goles":[9,8,0,0]
}


df = pd.DataFrame(players)
print(df)
print(df["player"])
print(df["goles"].mean())
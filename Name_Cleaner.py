
messy = input("entyer ur name ")
clean = "_".join(messy.lower().split())
print(f"""Messy: {messy!r}
Clean: {clean!r}
Length {len(messy)}
Display {clean.title()}
Removed: {len(messy)-len(clean)}""")

import os
def genTables(n):
 tables = ""
 for i in range(1,21):

   tables += f"{n} x {i} = {n*i}\n"
   os.makedirs("mulTables", exist_ok=True)
   with open(f"mulTables\Table_{n}.txt","w") as f:
     f.write(tables)




for i in range(1, 21):
 genTables(i)
    
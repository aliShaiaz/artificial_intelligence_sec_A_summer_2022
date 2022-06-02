block = ["", "clean", "dirty", "dirty"]

vCleaner = 0

print("\n\n")
for i in range(1, len(block)):
    if block[i] == "clean":
        print("Block ", i, " is clean.\n")
        vCleaner=1
    elif block[i] == "dirty":
      print("Block ", i, " is dirty.")
      block[i]="Clean"
      print("Block ", i, " is now clean.\n")
      vCleaner=0

print("\n\n")
    

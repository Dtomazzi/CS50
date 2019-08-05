from cs50 import get_int

def main():

   height=get_height("What is the height?:")
   space=height-1
   hash=1
   for x in range(height):
    spaces(space)
    hashes(hash)
    space=space - 1
    hash=hash + 1

def get_height(height):
    while True:
        n = get_int(height)
        if n > 0 and n < 9:
            break
    return n

def spaces(y):
  for y in range(y):
   print(" ", end="")

def hashes(z):
  for z in range(z):
   print("#", end="")
  print()

if __name__ == "__main__":
 main()
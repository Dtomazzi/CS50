from cs50 import get_float

def main():
 Q=25
 D=10
 N=5
 P=1
 coins=0
 change=get_change("Change: ")
 while True:
  if change >= Q:
    change= change-Q
    coins+=1
  elif change >= D:
    change=change-D
    coins+=1
  elif change >= N:
    change=change-N
    coins+=1
  elif change >= P:
    change=change - P
    coins+=1
  else:
      break
 print(coins)


def get_change(change):
 while True:
    n=get_float(change)
    if n >0:
        return n*100


if __name__=="__main__":
    main()
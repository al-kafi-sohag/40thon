def countdown(n):
  if n > 100:
    print("Done!")
  else:
    print(n)
    countdown(n+1)

countdown(1)
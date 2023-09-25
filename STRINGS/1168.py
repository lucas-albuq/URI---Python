n = int(input())
led_ref = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for x in range(n):
  num = input()
  leds = 0
  for char in num:
    leds += led_ref[int(char)]
  print(f'{leds} leds')
    
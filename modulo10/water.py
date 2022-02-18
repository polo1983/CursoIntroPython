water_left(5, 100, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in water_left
RuntimeError: There is not enough water for 5 astronauts after 2 days!

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    alert_navigation_system(err)
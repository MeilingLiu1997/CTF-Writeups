# rev/javascryption

![alt text](question.png)

---

## Strategy
1. check the web [source page](https://github.com/uclaacm/lactf-archive/blob/main/2025/rev/javascryption/src/index.html). there is nothing but a "hidden" script [image];
2. check javascript [cabin.js](https://github.com/uclaacm/lactf-archive/blob/main/2025/rev/javascryption/src/cabin.js). there are clearly five steps to check the flag.

---

## Methology
1. from base64 of JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I=
2. decodeURIComponent get ==QflJX[OLD_DATA]o91csxWY39VespnepJ3[OLD_DATA]f9mb7[OLD_DATA]GdjFGb
3. replace get ==QflJXZo91csxWY39VespnepJ3Zf9mb7ZGdjFGb
4. reverse order and from base64 get lactf{no_grizzly_walls_here}
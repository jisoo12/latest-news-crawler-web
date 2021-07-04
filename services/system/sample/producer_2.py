from tasks import practice
import time


if __name__ == '__main__':

  dic = {
    "fff": "555",
    "ggg": "666",
    "hhh": "777",
    "iii": "888",
    "jjj": "999"
  }

  for i in dic:
    result = practice.delay(i, dic[i])
    print(result)

    time.sleep(5)
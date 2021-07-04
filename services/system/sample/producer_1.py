from tasks import practice
import time


if __name__ == '__main__':

  dic = {
    "aaa": "000",
    "bbb": "111",
    "ccc": "222",
    "ddd": "333",
    "eee": "444"
  }

  for i in dic:
    result = practice.delay(i, dic[i])
    print(result)

    time.sleep(5)
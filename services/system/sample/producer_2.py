from first_celery import multiple


if __name__ == '__main__':
  for i in range(1000+1):
    result = multiple.delay(3, i).get(timeout=3)
    print(result)
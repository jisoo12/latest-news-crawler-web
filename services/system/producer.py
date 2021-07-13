from tasks import request_news


if __name__ == '__main__':
  rst = request_news.delay('ping')
  print(rst)

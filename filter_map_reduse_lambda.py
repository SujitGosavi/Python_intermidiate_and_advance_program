from functools import reduce

normal = [4, 5, 6, 98, 54, 5495541, 84, 54, 54, 54, 541, 545, 45, 5, 4, 8541, 65, 654, 85,
          45, 5, 41, 50, 1541, 54, 6512, 52, 165, 235, 64, 651, 514, 54, 165, 5, 1, 51, 85,
          145, 1, 851, 8514, 851, 485, 14, 8514, 84, 18, 51485, 41, 841, 85, 48, 54, 8741, 85, 418, 41]


filter_content = list(filter(lambda n: n % 3 == 0, normal))
print(filter_content)

map_content = list(map(lambda n: n+1, filter_content))
print(map_content)

reduse_content = reduce(lambda a, b: a + b, map_content)
print(reduse_content)
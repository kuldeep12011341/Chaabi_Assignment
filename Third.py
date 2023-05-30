def sort_dict_list(dict_list, key):
  return sorted(dict_list, key=lambda d: d[key])


def main():
  dict_list = [
      {"fruit": "orange", "color": "orange"},
      {"fruit": "apple", "color": "red"},
      {"fruit": "banana", "color": "yellow"},
      {"fruit": "blueberry", "color": "blue"}
  ]
  key = input("Enter the key to sort by: ")
  sorted_dict_list = sort_dict_list(dict_list, key)
  for dict in sorted_dict_list:
    print(dict)


if __name__ == '__main__':
  main()

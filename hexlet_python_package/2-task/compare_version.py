def compare_version(ver1, ver2):
  [major1, minor1] = ver1.split('.') # [major1, minor1]
  [major2, minor2] = ver2.split('.') # [major2, minor2]
  if int(major1) > int(major2):
    return 1
  elif int(major1) < int(major2):
    return -1
  elif int(major1) == int(major2):
    if int(minor1) > int(minor2):
      return 1
    elif int(minor1) < int(minor2):
      return -1
    else:
      return 0

print(compare_version('1.1', '1.1'))

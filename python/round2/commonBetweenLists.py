def whatsCommon(l1, l2):
  d = {}
  common = []
  for item in l1:
    d[item] = True
  for item in l2:
    if d[item]:
      common.append(item)
  return common

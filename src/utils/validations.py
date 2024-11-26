from datetime import datetime

def isValidDate(date):
  try:
    datetime.strptime(date, "%d/%m/%Y")
    return True
  except ValueError:
    return False

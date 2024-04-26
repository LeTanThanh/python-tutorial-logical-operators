if __name__ == "__main__":
  # The and operator

  """
  a and b
  """

  price = 9.99
  print(price > 9 and price < 10)
  print(price > 10 and price < 20)

  # The or operator

  """
  a or b
  """

  price = 9.99
  print(price > 10 or price < 20)
  print(price > 10 or price < 5)

  # The not operator

  """
  not a
  """

  price = 9.99
  print(not price > 10)
  print(not (price > 5 and price < 10))

  # Precedence of Logical Operators

  """
  When you mix the logical operators in an expression, Python will evaluate them in the order which is called the operator precedence.

  The following shows the precedence of the not, and, or operators

  - not: High
  - and: Medium
  - or: Low

  Based on these precedences, Python will group the operands for the operator with the highest precedence first, then group the operands for the operator with the lower precedence, and so on.

  In case an expression has several logical operators with the same precedence, Python will evaluate them from left to right:

  - a or b and c
  -> a or (b and c)

  - a and b or c and d
  -> (a and b) or (c and d)

  - a and b and c or d
  -> ((a and b) and c) or d

  - not a and b or c
  - ((not a) and b) or c
  """

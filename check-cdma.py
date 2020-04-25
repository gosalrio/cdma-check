def check_cdma(codes):
  bit_length = len(codes[0]) #assuming all the same e.g. '1111' 4 bit
  for i in range(len(codes)-1):
    for j in range(i+1, len(codes)):
      sumTotal = 0
      for k in range(bit_length):
        x, y = 1, 1
        if codes[i][k] == '0':
          x = -1
        if codes[j][k] == '0':
          y = -1
        sumTotal += (x*y)
      print("The sum of ({} XOR {}) is {}".format(codes[i], codes[j],sumTotal))
      if sumTotal != 0:
        print("This isn't a valid/orthogonal CDMA code")
        break

## Assuming the format
## User 1: 1, 1, 1, 1 = 1111
## User 2: 1, 1, -1, -1 = 1100
## User 3: 1, -1, -1, 1 = 1001
## User 4: 1, -1, 1, -1 = 1010
## -1 is represented as 0 in the array/list
      
codes = ["1111", "1100", "1001", "0011"]
check_cdma(codes)

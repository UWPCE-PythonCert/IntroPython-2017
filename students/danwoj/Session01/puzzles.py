def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
      return False


def diff21(n):
  if n <= 21:
    return 21-n
  else:
    return (n-21)*2


 def near_hundred(n):
  if  (90 <= n and 110 >= n):
    return(True)
  elif (190 <= n and 210 >= n):
    return(True)
  else:
    return(False)


 def missing_char(str, n):
  str = str[:n] + str[(n+1):]
  return(str)


  def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile):
    return True
  elif (not a_smile and not b_smile):
    return True 
  else:
    return False 


 def parrot_trouble(talking, hour):
  if (hour < 7 and talking):
    return True
  elif (hour > 20 and talking):
    return True
  else:
    return False


 def pos_neg(a, b, negative):
  
  if not negative:
    if(a<0 and b>0):
      return True
    elif(b<0 and a>0):
      return True
    else:
      return False

  if negative:
    if (a<0 and b<0):
      return True
    else:
      return False


def front_back(str):
  
  if len(str) <= 1:
    return str
  
  a=str[0]
  b = str[1:-1]
  c=str[len(str)-1]
  d=c+b+a
  return d


  def sum_double(a, b):
  if (a==b):
    return ((a+b)*2)
  else:
    return (a+b)


    def makes10(a, b):
  if (a==10):
    return True
  elif (b==10):
    return True
  elif (a+b==10):
    return True
  else:
    return False


    def not_string(str):
  b = str[0:3]
  if (b=='not'):
      return str
  else:
    c='not '
    str=c+str
    return str


    def front3(str):
  x=len(str)
  if (x<=3):
    return str+str+str
  else:
    z=str[0:3]
    return z+z+z


    def string_times(str, n):
  if (n==0):
    str=""
    return str 
  else:
    y=str
    for x in range(0, n-1):
      str=y+str
    return str


    def string_splosion(str):
  x=""
  for i in range(len(str)):
    x=x+str[:i+1]
  return x


  def array_front9(nums):
  x=len(nums)
  if x>4:
    x=4
  for i in range(x):
    if nums[i]==9:
      return True
  return False


  def last2(str):
  if len(str)<2:
    return 0
  end=str[len(str)-2:]
  count=0
  for i in range(len(str)-2):
    sstr=str[i:i+2]
    if sstr==end:
        count=count+1
  return count


  def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
        return True
  return False


  def string_bits(str):
  word=""
  for i in range(len(str)):
    if i % 2==0:
      word=word+str[i]
  return word


  def array_count9(nums):
  count=0
  for i in nums:
    if i==9:
      count=count+1
  return count


  def string_match(a, b):
  x=min(len(a), len(b))
  count=0
  for i in range(x-1):
    y=a[i:i+2]
    z=b[i:i+2]
    if y==z:
      count=count+1
  return count


  def hello_name(name):
  greet='Hello '+name+'!'
  return greet
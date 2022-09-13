class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def convert_to_binary(self):
    curr = head
    # start compiling the number by using a string
    num = str(curr.val)
    while curr.next:
      curr = curr.next
      # append existing number by the next value
      num = num + str(curr.val)
      
    # convert string to decimal expression of a binary number (101 becomes 5)
    answer = int(num, 2)
      
    return answer
  
  
  

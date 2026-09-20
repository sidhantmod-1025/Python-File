# i will give you cordinate of one cell you will tell which color it is
"""
def chess (row,column):
  row_num = ord(row.upper()) - ord('A')+1
  if(row_num + column)%2==0:
    print("Black")
  else:
    print("White")

row = input("Enter a row : ");
column = int(input("Enter a column : "));
chess(row,column);  
 """
# 2 -> Given coordinates, whether Rook can attack or not

def rook(row1,col1,row2,col2):

  if row1.upper() == row2.upper() or col1==col2:
    print("yes it will be attack")
  else:
    print("not")  


row1= input("Enter First row : ")
col1= int(input("Enter First col : "))

row2= input("Enter second row : ")
col2= int(input("Enter second col : "))




rook(row1,col1,row2,col2)  

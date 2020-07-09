#uses Python3
def main():
      #STRING INPUT
      Input_array=input().strip().lower().split(" ")
      
      if len(Input_array)>1000:
            return

      #Validation Array Input(i.e)
      """foodn face the donation coalition economy sector"""
      rejected_items=input().strip().split(" ")

      if len(rejected_items)>100:
            return

      #RESULT LIST for accepted items in Input String
      result=[]

      for i in rejected_items:
            if i in Input_array:
                  Input_array.remove(i)

      print(Input_array)
main()


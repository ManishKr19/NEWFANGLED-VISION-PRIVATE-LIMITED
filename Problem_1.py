#uses Python3
def main():
      #STRING INPUT
      Input_str=input().strip().lower()

      if len(Input_str)<10 or len(Input_str)>10000:
            return

      #Validation Array Input(i.e)
      """foodn face the donation coalition economy sector"""
      Validation_Array=input().strip().split(" ")

      if len(Validation_Array)>1000:
            return

      #Dictionary for Word & Frequency in String
      result={}

      for i in Validation_Array:
            result.update({i:Input_str.count(i)})

      for j in result:
            print(j,":",result[j])
main()

































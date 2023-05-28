import Input
import output

print("""
      1.input
      2.output
      3.exit
      """)
a=int(input("Choose: "))

while (True):
    if a==1:
        Input.type()
    if a==2:
        output.show()
    if a==3:
        exit
    else:
        print("Wrong, re-choose:")
        a=int(input("Choose: "))


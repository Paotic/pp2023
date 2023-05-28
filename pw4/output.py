student = []
course = []
mark = []
credit = []
n = 0
k = 0
def show():
    for idx, std in enumerate(student):
        print("--------------------------")
        print(f"{std}")
        for jdx, crs in enumerate(course):
            print(f"""{crs}
                    Mark: {mark[n]}""")
            n +=1
        # print(f"GPA: {GPA[k]}")
        # k+=1
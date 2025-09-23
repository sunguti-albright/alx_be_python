#Function definitions

def calculate_area(length, width):
    """ calculates the area of a rectangle"""
    area = length * width
    return area

print(calculate_area(7,10))

# Local vs Global Scope
# count = 0
# def increment():
#     count+=1

# increment()
# print(count)

#Global and nonlocal keywords
counts = 1
def increment_global():
    global counts
    counts += 3

increment_global()
print(counts)
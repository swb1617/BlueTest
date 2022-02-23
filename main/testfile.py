import prestool
from prestool.Tool import Tool

if __name__ == '__main__':

    tool = Tool()
    for i in range(20000):
        a = tool.random_name()
        b = tool.random_ssn()
        print(a +"  "+ b)


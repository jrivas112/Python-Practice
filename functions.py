
#this function make "world" its default argument
def hello(name="World"):
    print("Hello,",name)

def main():
    hello()
    name = input("What's your name? ")
    hello(name)
main()
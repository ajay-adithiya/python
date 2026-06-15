def with_gst(func):

    def wrapper():
        print("before bill function")
        func()
        print("after bill function")

    return wrapper

@with_gst
def bill():
    print("bill executed")

bill()

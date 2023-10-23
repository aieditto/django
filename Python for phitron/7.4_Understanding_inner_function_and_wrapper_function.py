#function is a first class object
def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        # return 3000
    return inner_fun

def func(double_decker):
    print('Alpha Alpha')
    double_decker()
    print('Beta')

def pentu():
    print('decorator way or wrapper function')
#print(double_decker()()) #calling the inner fucntion using double ()
func(pentu)

#decorator
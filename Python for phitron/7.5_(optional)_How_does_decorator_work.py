def functionn(hbd):
    def innerfunc():
        print('Alif Laila')
        hbd()
        print('Chomolokko')
    return innerfunc
@functionn  #easy mehtod to use decorator
def get_factorial():
    print('factorial starting')

get_factorial()

"""Without decorator if i call
    the below function it will give
    the out put of himself. But when using @and_mention_the_main_function
    then the main function will call and a argument pass from the second_function()
    after that the main fucntion will receive as parameter then it will show the result. 
"""    
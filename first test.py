# NONLOCAL and GLOBAL

#Example 6: Create a nonlocal variable
#nonlocal allows us to assign values to an outer (but non-global) scope.
#for assigning values to the global scope, we can use global keyword instead.
def outer():
    x = "local"

    def inner():
        #nonlocal x
        
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
########################################


# YIELD in Python

# Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and # when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword # is termed a generator. Hence, yield is what makes a generator.27-May-2021


# Decorators in Python

#-------- orig_func already given ----------
def orig_func():
   print("Wheee!")

#------ write decorator ------------
def my_decorator(some_function):
    def my_wrapper():
        print ("do something before")   #do something before, if you want to
        some_function()
        print ("do something after")    #do something after, if you want to
    return my_wrapper

#------ create decorator and call orig func --------
orig_func = my_decorator(orig_func)   #create decorator, modify functioning 
orig_func()  


# Closures in Python
 #the inner_func has the full access to the environment (variables) in it’s enclosing scope. That is closure.
 
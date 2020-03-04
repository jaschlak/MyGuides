# Memory

    Managing Memory in Python
    
## Useful Commands

    id(<var>)                                               # get variables reference
    hex(id(<var>))                                          # get variables hex reference value
    sys.getrefcount(<var>)                                  # count number of references (creates a new reference)
    ctypes.c_long.from_address(<address>).value             # more exact way of counting references, note if set variable to none, address might be handed to other things
        example:
        a=[1,2,3]
        def ref_count(address: int):
            return ctypes.c_long.from_address(address).value
        ref_count(id(a))
        
## Garbage Collection Example (circular definition)

    import ctypes, gc

    # Get reference to object
    def ref_count(address: int):
        return ctypes.c_long.from_address(address).value
        
    # See if object exists
    def object_by_id(object_id):
        for obj in gc.get_objects():
            if id(obj == object_id:
                return "Object eists"
        return "Not Found"
        
    class A:
        def __init__(self):
            #3 pass A to B
            self.b = B(self)
            #print addresses associated
            print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))
            
    class B:
        def __init__(self, a):
            self.a = a 
            print('B: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.a))))
            
    # Disable garbace collection to show circular reference and not allow Pythont to clean it up        
    gc.disable()
    
    # prints addresses of B and A
    my_var = A()
    
    # Confirm my_var and A are at the same address
    hex(id(my_var))
    
    # Confirm memory address b and a are both found in b (circular reference)
    print(hex(id(my_var.b)))
    print(hex(id(my_var.b.a)))
    
    # hold references to a and ab
    a_id = id(my_var)
    b_id = id(my_var.b)
    
    # confirm hex address of the 2
    print(hex(a_id))
    print(hex(b_id))
    
    # 2 references because b is refering to a
    ref_count(a_id)
    
    # 1 reference because a is not refering to b
    ref_count(b_id)
    
    # are the objects there? object exists
    object_by_id(a_id)
    
    # are the objects there? object exists
    object_by_id(b_id)
    
    # destroy reference to my_var
    my_var = None
    
    # 1 reference (2nd gone because my_var was removed)
    ref_count(a_id)
    
    # 1 reference 
    ref_count(b_id)
            
    # are the objects there? object exists
    object_by_id(a_id)
    
    # are the objects there? object exists
    object_by_id(b_id)
    
    # still there but not cleaned up
    
    # Run garbage collector manually
    gc.collect()
# Make Simple Object and Call it

    This was the first way I found to make objects
    
## Object File ("Object.py")

    class Obj:
        def __init__(self, Element1=[], Element2 =[]):
            self.Element1 = Element1;
            self.Element2 = Element2;
            
        def get_Element1(self):
            return self.Element1;
        
        def get_Element2(self):
            return self.Element2;
        
        
## Main File

    from Object import Obj;

    Obj = Obj(Element1 = [1,2,3], Element2 = [5,6,7]);
    print("Element1 = " + str(Obj.get_Element1()) + " Element2 = " + str(Obj.get_Element2()));
       
# Constructors

    How to make Constructors. 
    
    Examples 
    https://github.com/jaschlak/c-_udemy_intermediate/blob/master/008_Constructors/Customer.cs
    https://github.com/jaschlak/c-_udemy_intermediate/blob/master/011_Fields/Customer.cs
    
Example #1

    public class Customer
    {
        List<Order> Orders = new List<Order>();
    }
    
Example #2

    public class Customer
    {
        readonly List<Order> Orders 
        
        public Customer()
        {
            Orders = new List<Order>();
        }
    }
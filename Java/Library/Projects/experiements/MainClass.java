package experiements;

/*
 * The purpose of this project is to show how inheritance works:
 * - passes along method to child
 * - overrides child method with new value
 * - adds new method to child method
 */

public class MainClass 
{

	public static void main(String[] args) 
	{
		
		Parent obj1 = new Parent();
		obj1.Show();
		
		Child obj2 = new Child();
		obj2.Show();
		
		System.out.println(obj2.newMethod());

	}

}

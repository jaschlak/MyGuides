package methodoverloading;

public class BaseClass 
{
	public void calling()
	{
		System.out.println("No parameters called.");
	}

	public void calling(int a)
	{
		System.out.println("Integer "+a+" called.");
	}
	
	public void calling(String a)
	{
		System.out.println("String "+a+" called.");
	}
}

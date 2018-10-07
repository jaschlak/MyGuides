package methodoverloading;

public class MainClass 
{
	/* Method Overloading
	 * The purpose of this example is to showcase the ability to define a constructor
	 * with the same name using different parameter types and how the Java Compiler
	 * decides which constructor to run. 
	 */

	public static void main(String[] args)
	{
		
		BaseClass noPar = new BaseClass();
		noPar.calling();
		noPar.calling(32);
		noPar.calling("Pickles");

	}

}

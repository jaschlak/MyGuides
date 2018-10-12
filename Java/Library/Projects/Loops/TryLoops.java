package loops;

public class TryLoops 
{
	public static void main(String[] args)
	{
		
		try 
		{
			System.out.println("This line worked fine\n");
		}
		catch(Exception e) {}
		
		try
		{
			int a = 3/0;
		}
		catch (Exception e)
		{
			System.out.println(" \n Text can go between the error and throwing the exception like this ");
			throw e;
			
		}

		/*
		 * 
		 * This is an alternative
		 * 
		 * 
		 
		try
		{
			System.out.println("This loop is about to fail, why devide by 0?");
			int a = 3/0;
		}
		catch (Exception e)
		{
			e.printStackTrace();
			
			System.out.println("See I told you it would error: \n");
			
			System.out.println("\n\n");
		}
		
		*/

		
	}

}

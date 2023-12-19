package loops;

public class DoWhile 
{
	// The purpose of this class is to show the proper structure of a Do While Loop

	public static void main(String[] args) 
	{
		
		int i = 0;
		int Sum = 0;
		
		do 
		{
			Sum += i;
			i++;
		} while (i<10);
		
		System.out.println(Sum);
		
	}

}

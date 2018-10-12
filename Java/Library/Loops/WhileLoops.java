package loops;

public class WhileLoops 
{
	// The purpose of this clas is to show the structure of the While Loop
	
	public static void main(String[] args) 
	{
		int i = 0;
		int Sum = 0;
		
		while(i<10)
		{
			Sum+=i;
			i++;
		}
		
		System.out.println(Sum);
		
	}
}

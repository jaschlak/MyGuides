package statements;

public class SwitchStatements 
{

	public static void main(String[] args)
	{
		// What numerical day of the week is it today?
		int a = 3;
		String today="";
		
		switch (a)
		{
		case 1: 
		today = "Sunday";
		break;
		
		case 2:
		today = "Monday";
		break;
			
		case 3:
		today = "Tuesday";
		break;
		
		case 4:
		today = "Wednesday";
		break;		
		
		case 5:
		today = "Thursday";	
		break;	
		
		case 6:
		today = "Friday";
		break;

		case 7:
		today = "Saturday";
		break;
		}
		
		System.out.println(today);
	
	}
	
}

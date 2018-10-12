package statements;

public class IfStatement {
	
	// The purpose of this class is to properly show If/Else/Else If statements

	public static void main(String[] args) 
	
	{
		
		if(0 != 0)
		{
			System.out.println("Weird this didn't print, I guess 0 does equal 0.");
		}
		
		else if( 3 == 3)
		{
			System.out.println("I guess this printed and 3 = 3");
		}
		
		else if (3 == 3)
		{
			System.out.println(" This wouldn't have printed because the second statement already tripped");
		}
		else
		{
			System.out.println("Of course this printed");
		}

	}

}

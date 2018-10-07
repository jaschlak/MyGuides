package inheritance;

public class MainClass 
{

	public static void main(String[] args) 
	{
		// base class- class is being inherited (can be inherited x times)
		// derived class- class being defined by base class (can only inherit one base class)
		// you can call the constuctors as well by using a "super"
		
		PartTimeProfessor ptp = new PartTimeProfessor("John","Doe",2108961931, "john.doe@hotmail.com","3245 Valdez Drive","finance",2);


		FullTimeProfessor ftp = new FullTimeProfessor("Jane", "Doe,", 2108961931, "janeblinky@hotmail.com", "4501 Pleasant St", "Engineering", 210, "11-1 MWF", 210, 4);
		
		
		ptp.info();
		System.out.print("\n\n\n");
		ftp.info();
		// Note the new lines in full time professor are not showing up, how to handle this will be shown later.
		// For now, ghetto rig with getters and setters
		
		System.out.println("Room:              " + ftp.getOfficeNumber() + 
						 "\nOffice Hours:      " + ftp.getOfficeHours() +
						 "\nOffice Phone:      " + ftp.getOfficePhone() +
						 "\nNumber of Courses: " + ftp.getNumberOfCourses());
		
		

	}
	
	
}

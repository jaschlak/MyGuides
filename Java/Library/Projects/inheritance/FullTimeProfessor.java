package inheritance;

public class FullTimeProfessor extends Staff
{
	private int officeNumber;
	private String officeHours;
	private int officePhone;
	private int numberOfCourses;
	
	public FullTimeProfessor(String firstName, String lastName, int phoneNumber, String email, String address,
			String department, int officeNumber, String officeHours, int officePhone, int numberOfCourses) 
	{
		super(firstName, lastName, phoneNumber, email, address, department);
		this.officeNumber = officeNumber;
		this.officeHours = officeHours;
		this.officePhone = officePhone;
		this.numberOfCourses = numberOfCourses;
	}

	public int getOfficeNumber() {
		return officeNumber;
	}

	public void setOfficeNumber(int officeNumber) {
		this.officeNumber = officeNumber;
	}

	public String getOfficeHours() {
		return officeHours;
	}

	public void setOfficeHours(String officeHours) {
		this.officeHours = officeHours;
	}

	public int getOfficePhone() {
		return officePhone;
	}

	public void setOfficePhone(int officePhone) {
		this.officePhone = officePhone;
	}

	public int getNumberOfCourses() {
		return numberOfCourses;
	}

	public void setNumberOfCourses(int numberOfCourses) {
		this.numberOfCourses = numberOfCourses;
	}
	
	
	
}


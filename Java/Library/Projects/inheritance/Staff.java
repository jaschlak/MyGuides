package inheritance;

public class Staff 
{

	private String firstName;
	private String lastName;
	private int phoneNumber;
	private String email;
	private String address;
	private String department;
	
	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public int getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(int phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}

	public Staff(String firstName, String lastName, int phoneNumber, String email, String address, String department)
	{
		this.firstName = firstName;
		this.lastName = lastName;
		this.phoneNumber = phoneNumber;
		this.email = email;
		this.address = address;
		this.department = department;
	}
	
	public void info()
	{
		System.out.println("first name:  " + getFirstName()
					   + "\nlast name:   " + getLastName()
					   + "\nphone number:" + getPhoneNumber()
					   + "\ne-mail:      " + getEmail()
					   + "\naddress:     " + getAddress()
					   + "\ndepartment:  " + getDepartment());	
	}
	
}

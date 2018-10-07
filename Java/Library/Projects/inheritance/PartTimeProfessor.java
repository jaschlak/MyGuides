package inheritance;

public class PartTimeProfessor extends Staff
{
	private int numberOfLecutres;

	public PartTimeProfessor(String firstName, String lastName, int phoneNumber, String email, String address,
								String department, int numberOfLecutres) 
	{
		super(firstName, lastName, phoneNumber, email, address, department);
		this.numberOfLecutres = numberOfLecutres;
	}

	public int getNumberOfLecutres() {
		return numberOfLecutres;
	}

	public void setNumberOfLecutres(int numberOfLecutres) {
		this.numberOfLecutres = numberOfLecutres;
	}
	
	

}

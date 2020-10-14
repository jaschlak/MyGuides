# Classes and Inheritance

    This holds the progress for the codelabs for me. Also, a good reference
    
## Code

    abstract class Dwelling(private var residents : Int){
        abstract val buildingMaterial : String
        abstract val capacity : Int
        
        fun hasRoom(): Boolean {
            return residents > capacity
    }
    }

    fun main() {
        
    }


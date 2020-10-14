# Classes and Inheritance

    This holds the progress for the codelabs for me. Also, a good reference
    
## Code


    fun main() {
        
        var squareCabin = SquareCabin(6)
        
        // Report Values
        println("Square Cabin\n===========================")
        println("Capacity: ${squareCabin.capacity}")
        println("Material: ${squareCabin.buildingMaterial}")
        println("Has Room?: ${squareCabin.hasRoom()}")
        
        
        // Quicker Report
        with(squareCabin){
            println("\n\nSquareCabin\n==========================")
            println("Capacity: ${capacity}")
            println("Material: ${buildingMaterial}")
            println("Has Room?: ${hasRoom()}")
        }
        
        var roundHut = RoundHut(3)
        
        //Report Hut (quicker)
        with(roundHut){
            println("\n\nRound Hut\n===============================")
            println("Capacity: ${capacity}")
            println("Material: ${buildingMaterial}")
            println("Has Room?: ${hasRoom()}")
        }
        
        var roundTower = RoundTower(7, 3)
        //Report Round Tower (quick)
        with(roundTower) {
            println("\n\nRound Tower\n================================")
            println("Capacity: ${capacity}")
            println("Material: ${buildingMaterial}")
            println("Has Room?: ${hasRoom()}")
        }
        
    }

    abstract class Dwelling(private var residents : Int){
        
        abstract val buildingMaterial : String
        abstract val capacity : Int
        
        fun hasRoom(): Boolean {
            return residents < capacity
    }
    }

    class SquareCabin(residents: Int): Dwelling(residents) {
        override val buildingMaterial = "Wood"
        override val capacity = 6
    }

    open class RoundHut(residents:Int): Dwelling(residents){
        override val buildingMaterial = "Straw"
        override val capacity = 4
    }

    class RoundTower(residents: Int, val floors: Int): RoundHut(residents) {
        override val buildingMaterial = "Stone"
        override val capacity = 4 * floors
    }
        

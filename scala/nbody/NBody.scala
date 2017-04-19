import scala.util.Random;

def initBodies(n:Integer): List[Float] = {
   return (for(i <- 1 to n) yield Random.nextFloat()).toList
}



object Main extends App{
    //val bodies = for(i <- 1 to 10) yield Random.nextFloat()
    val bodies = initBodies(10);
    //interactions, simulation


}


println("wtf")
Main.main(Array())

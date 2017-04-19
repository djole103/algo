import akka.actor.Actor;

class MyActor extends Actor{
    def receive = {
        case "test" => println("received test") 
        case _      => println("somethin else!")
    }
}





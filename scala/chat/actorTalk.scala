import akka.actor.Actor;
import akka.actor.Props
import akka.actor.ActorSystem

//import akka.actor.Actor.actorOf

object actorTalk {
    def main(args: Array[String]){
        //val myActor = Actor.actorOf[MyActor]
        //val myActor = actorOf[MyActor]
        //val myActor = new MyActor();
        //val myActor = Props[MyActor]


        val system = ActorSystem("mySystem")
        val myActor = system.actorOf(Props[MyActor], name = "money")
//        myActor.start()

        myActor ! "test"
        myActor ! "whaat"        
    }
}



import akka.actor.Actor
import akka.actor.ActorSystem
import akka.actor.Props

class HelloActor extends Actor {
  def receive = {
    case "hello" => println("hello!!!")
    case _       => println("No way")
  }
}

object Main extends App {
  val system = ActorSystem("HelloSystem")
  // default Actor constructor
  val helloActor = system.actorOf(Props[HelloActor], name = "helloactor")

  println("Started!")

  helloActor ! "hello"
  helloActor ! "buenos dias"
}

Main.main(Array())

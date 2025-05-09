using System;

class Program
{
    static void Main()
    {
        // Create a random number generator
        Random randomGenerator = new Random();
        int magicNumber = randomGenerator.Next(1, 101); // random number between 1 and 100

        int guess = -1;

        Console.WriteLine("Welcome to the Guess My Number game!");
        Console.WriteLine("I'm thinking of a number between 1 and 100.");

        // Loop until the user guesses the number
        while (guess != magicNumber)
        {
            Console.Write("What is your guess? ");
            string userInput = Console.ReadLine();
            guess = int.Parse(userInput);

            if (guess < magicNumber)
            {
                Console.WriteLine("Higher");
            }
            else if (guess > magicNumber)
            {
                Console.WriteLine("Lower");
            }
            else
            {
                Console.WriteLine("You guessed it!");
            }
        }
    }
}
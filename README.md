# Excercise-Intive-FDV

#Development Practices

My sequence of steps to develop any piece of code usually starts the same way:

First I get some white board or piece of paper and I began to sketch some first thoughts. Trying to engage the main challenges of the assignment, How big should it be ? Where to start? How many objects, classes, etc should I create? Can I break it into smaller and simple pieces and then integrate all of them ? How could they interact between them? This step frequently arrives at a primitive, very brute idea of how to implement it with a lot of cross out sections.

Second I start coding, initializing by those parts of the problem that I have a much more clear sense of how they are going to be. In this section, while writing it, a lot of possible future bugs are avoided by refining a lot that initial idea within the paper. I tend to implement small functions and classes, testing them and then moving to other sections of the problem, leaving already test it modules for the future integration.

Third and last step, once I had all the separate ingredients for the model I’m building I bring all of them together in the right order, sometimes polishing some interactive problems between the different units and then start a battery of tests to check if the program do as it was supposed to. 

#Desgin

In this particular exercise I spend some time trying to think the best possible way to interact between different types of Rentals and their periodic time differences. It occurs to me to build a standardize measure unit, choosing one of three options (days, hours or weeks), and then work with conversions between one another. But in the spirit of simplicity and a much clearer code (also it wasn’t needed for the implementation) I kept that out of the program. 

One of my optimization goals as programming is always trying to reduce at a minimum level the duplicate lines or storage data. That’s why the Rental_Units subclass just has two attributes that where the only ones necessary to difference between one another. The election of working with dictionaries in the attribute of prices is just habit I imported from some of my recent Machine Learning exercises, where is very common to pass through a list of unrelated parameters between methods and functions and a very clean and neat way to do, it in my opinion, is with dictionaries.

The methods of the Rental class are quite intuitive, in thinking this class as the whole order of rentals of a family or group, it was necessary some operation to add the individual rentals and also keeping record of the quantity of them was needed, later on, for the discount. The other obvious method was the charging price, for closing the order, to make easier the testing face I divided into 2 different problems (adding the Overall_Sum method), the sum with the respective prices for one side and applying the discount if it checks the necessary conditions in the other side.

Last, just for testing purposes (I’m aware it wasn’t asked), I coded a little Api, that helped me debug some minor errors in the classes and gain some final intuition of the behavior of the all the objects created.  

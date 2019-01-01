# Excercise-Intive-FDV

		#Development Practices

My sequence of steps to develop any piece of code usually starts the same way:

First I get some white board or piece of paper and I began to sketch some first thoughts. Trying to engage the main challenges of the assignment, How big should it be ? Where to start? How many objects, classes, etc should I create? Can I break it into smaller and simple pieces and then integrate all of them ? How could they interact between them? This step frequently arrives at a primitive, very brute idea of how to implement it with a lot of cross out sections.

Second I start coding, initializing by those parts of the problem that I have a much more clear sense of how they are going to be. In this section, while coding it, a lot of possible future bugs are avoided by refining a lot that initial idea within the paper. I tend to implement small functions and classes, verify manually that are working properly and then moving on.

Third and last step, once I had all the separate ingredients for the model I’m building I bring all of them together in the right order, sometimes polishing some interactive problems between the different modules and finally starting the testing stage.

		#Desgin

In this particular exercise I spend some time trying to think the best possible way to interact between different types of rentals and their periodic time differences. It occurs to me to build a standardize measure unit, choosing one of three options (days, hours or weeks), and then work with conversions between one another. But in the spirit of simplicity and a much clearer code (also it wasn’t needed for the implementation) I kept that out of the program. 

One of my optimization goals as programming is always trying to reduce at a minimum level the duplicate lines or storage data. That’s why the RentalUnits subclass just has two attributes that where the only ones necessary to difference between one another. The election of working with dictionaries in the attribute of prices is just habit I imported from some of my recent Machine Learning exercises, where is very common to pass through a list of unrelated parameters between methods and functions and a very clean and neat way to do it, in my opinion, is with dictionaries.

The methods of AdministratorOfRentalGroupOrders are quite intuitive, it was necessary some operation to add the individual RentalUnits and also keeping record of them (later on was needed for the discount calculation). The other obvious method was the charging price, for closing the order, to make it easier I divided into 2 different subproblems (adding the OverallSumRental method), the sum with the respective prices for one side and applying the discount if it apllied in the other side.

		#Testing

I don’t have any corporate experience in producing software and in my amateur journey of excercises I was never required, until now, to make a serious testing  module. I was used to do just manual testing with border cases. 

I did a two days google research about thist topic and I understand from the written assignment that unittest was required. From what I grasp in this few days, testing is not to be underestimated, it’s a way of thinking, a coding philosofy in itself with practices like TDD (Test Driven Development). I wasn’t going to incorporate the testing right state of mind from one day to the other.

To conclude, whith the little knowledge I coud learn in this few days, I tried to do a brute and amateur version of some automatted testing. I’m eager to learn more about this trend and subject.




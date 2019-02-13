# Epithet Generator

Serves a randomly generated shakespearean insult from the vocab list at
[Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html).

## Usage

Once you run the program, going to your **/** or root route will serve up one
randomly generated insult.

The **/vocabulary** route will serve up a dictionary of all the words
available to generate an insult.

The **/epithets/<int:quantity>** route will serve up a user specified number
of epithets with the value provided inside the **< >** in the route.
An example would be going to **/epithets/8** would serve you 8 epithets.

The **/unleash_nemesis_rant** route will serve up a random amount of epithets
with a limit based on how many words are in the dictionary.

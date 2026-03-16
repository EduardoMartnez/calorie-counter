# calorie-counter

Inspired by [app-ideas' Calorie Counter](https://github.com/florinpop17/app-ideas/blob/master/Projects/3-Advanced/Calorie-Counter-App.md) by [jdmedlock](https://github.com/florinpop17/app-ideas/commits?author=jdmedlock)

This application will allow a user to search a food database to learn how many calories a specified food has. The user will search this food by typing into the search bar and scroll through the list of foods that will appear as they type. The user can also press 'Enter' to get the list as well.

## User Stories

### 1. User Accounts
- [ ] 1.1 User can register an account in a registration page.
- [ ] 1.2 User can login to their account in a login page.

### 2. Calorie Counter page
- [ ] 2.1 User can see an panel containing a food description input text box, 
a 'Search' button, and a 'Clear' button.
- [ ] 2.2 User can enter search terms into the food description input text box.
- [ ] 2.3 User can click on the 'Search' button to search for the matching food.
- [ ] 2.4 User can see a warning message if no search terms were entered.
- [ ] 2.5 User can see a warning message if no matches were found.
- [ ] 2.6 User can see a list of the matching food items, portion sizes, and
calories in a scrollable results panel that is limited to 25 entries.
- [ ] 2.7 User can click on the 'Clear' button to clear the search terms and 
results list. 
- [ ] 2.8 User can see the count of the number of matching food items adjacent to
the results list.
- [ ] 2.9 User can use a wildcard character in search terms.
- [ ] 2.10 User can see more than 25 entries from a search by clicking a Down
icon button to add more matching food items to the search results list.
- [ ] 2.11 User can see 'Recipes' button to enter a page to manage recipes.
- [ ] 2.12 User can see a star indicating a food is used in a user recipe.

### 3. Recipe Manager page
- [ ] 3.1 User can click on the 'Search' button to access Calorie Counter main page.
- [ ] 3.2 User can click on the 'Create' button to begin creating a recipe in a pop-up window.
  - [ ] 3.2.1 User can click on the 'Name' text box to to change the recipe's name.
  - [ ] 3.2.1 User can click on the 'Add Ingredient' button to add a food from the database.
  - [ ] 3.2.2 User will have access to a copy of the search bar from the Calorie Counter page.
  - [ ] 3.2.3 User can choose a food from the list to add to the recipe.
  - [ ] 3.2.4 User can type in the 'Description' text box to explain further details for the recipe.
  - [ ] 3.2.5 User can click on the 'Save' button to store the recipe ingredients and description.
- [ ] 3.3 User can click on the 'Edit' button next to a recipe to edit its' ingredients and description.
- [ ] 3.4 User can click on the 'Delete' button next to a recipe to remove the recipe.
- [ ] 3.5 User can click on the 'View' button to view the recipe ingredients and description in a pop-up window.
- [ ] 3.6 User can click on the 'AI Help' button to have an AI agent create and edit a recipe for the user.

### 4. Backend features
- [ ] 3.7 Developer will create a JSON file containing the food items to be
searched. This will be loaded when the app is started.
- [ ] 3.8 Developer will implement load the MyPyramid data into a database or a
data structure other than an array for faster searching.

Feature: Add a new task
	In order to manage my tasks
	As a user
	I want to be able to add new task

		Scenario: Add new task and see it in the list
			Given I am in the todos page
			When I add new task "Clean my house"
			Then the task "Clean my house" will be added to the list
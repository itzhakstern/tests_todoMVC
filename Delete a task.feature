Feature: Delete a task
	In order to manage my tasks
	As a user
	I want to be able to delete existing task


Scenario: Deleted task will disappear from the list
	Given I am in the todos page
	And there is a task "Wake up" in the list
	When I delete the task "Wake up"
	Then the task list will be empty
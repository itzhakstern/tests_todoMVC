Feature: Clear completed tasks
	In order to delete completed tasks
	As a user
	I want option to clear all completed task


Scenario: Clear completed tasks will delete completed tasks only
	Given I am in the todos page
	And there is a task "Wake up" in the list
	And there is a completed task "Clean the house" in the list
	When I click on Clear completed tasks
	Then the task "Wake up" is not in Completed list
Feature: Mark task as completed
	In order to see only active tasks
	As a user
	I want to be able to mark task as completed


Scenario: Mark active task as completed
	Given I am in the todos page
	And there is a task "Wake up" in the list
	When I make the task "Wake up" completed
	Then the task "Wake up" will appear as completed
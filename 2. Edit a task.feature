Feature: Edit a task
	In order to manage my tasks
	As a user
	I want to be able to edit existing task

	
Scenario: Rename existing task
	Given I am in the todos page
	And there is a task "Wake up" in the list
	When I edit the task "Wake up" to be "Go to sleep"
	Then the task list will be
		| TaskName    | IsCompleted |
		| Go to sleep | False       |
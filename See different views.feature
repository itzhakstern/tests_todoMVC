Feature: See different views
	In order to manage my tasks
	As a user
	I want to see different views, like completed,active and all


Scenario: View all will show active and completed tasks
	Given I am in the todos page
	And there is a task "Wake up" in the list
	And there is a completed task "Clean the house" in the list
	When I switch to view Active
	And I switch to All view
	Then the task list will be
		| TaskName        | IsCompleted |
		| Wake up         | False       |
		| Clean the house | True        |


Scenario: View Active will show only active tasks
	Given I am in the todos page
	And there is a task "Wake up" in the list
	And there is a completed task "Clean the house" in the list
	When I switch to Active view
	Then the task list will be
		| TaskName | IsCompleted |
		| Wake up  | False       |


Scenario: View Completed will show only completed tasks
	Given I am in the todos page
	And there is a task "Wake up" in the list
	And there is a completed task "Clean the house" in the list
	When I switch to Completed view
	Then the task list will be
		| TaskName        | IsCompleted |
		| Clean the house | True        |
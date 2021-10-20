Feature: Mark completed task as active
	In order to reopen completed task
	As a user
	I want to be able to make completed task active


Scenario: Create task, make it completed and then active
	Given I am in the todos page
	And there is a task "Wake up" in the list
	When I make the task "Wake up" completed
	And I make the task "Wake up" active
	Then "Wake up" task mot in IsCompleted list
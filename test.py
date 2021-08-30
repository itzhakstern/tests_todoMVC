from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

TASK1 = 'Clean my house'
TASK2 = 'Wake up'
WAITING_TIME = 1

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://todomvc.com/examples/angularjs/#/")
    driver.implicitly_wait(WAITING_TIME)
    return driver


def add_task_to_edit(msg):
    t1 = None
    flag = False
    driver = init_driver()
    msg_task = driver.find_element_by_css_selector('input[ng-model="newTodo"]')
    msg_task.send_keys(f"{msg}\n")
    todo_list = driver.find_elements_by_class_name('todo-list')
    for task in todo_list:
        if task.text == msg:
            flag = True
            t1 = task
            break
    if not flag: print(f"ERROR: the task {msg} not add to the todo list")
    return driver, t1


def test1_add_a_new_task():
    driver = init_driver()
    driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys(f"{TASK1}\n")
    driver.implicitly_wait(WAITING_TIME)

    elements = driver.find_elements_by_css_selector('label[ng-dblclick="editTodo(todo)"]')
    for elem in elements:
        if elem.text == TASK1:
            print("test1_add_a_new_task is passed successfully")
    print("ERROR - the task not found in the todo list")


def test2_edit_a_task():
    driver_and_task = add_task_to_edit(TASK2)
    driver = driver_and_task[0]
    task = driver_and_task[1]
    action = ActionChains(driver)
    edit_task = "Go to sleep"

    element_to_edit = driver.find_element_by_css_selector('label[ng-dblclick="editTodo(todo)"]')
    action.double_click(element_to_edit).perform()
    edition_task = driver.find_element_by_css_selector('input[todo-focus="todo == editedTodo"]')
    edition_task.send_keys(Keys.CONTROL, 'a')
    driver.implicitly_wait(WAITING_TIME)
    edition_task.send_keys(f'{edit_task}\n')
    driver.implicitly_wait(WAITING_TIME)

    print('test2_edit_a_task is passed successfully') if task.text == edit_task else print('test2_edit_a_task is fail')


def test3_delete_a_task():
    driver_and_task = add_task_to_edit("Wake up")
    driver = driver_and_task[0]
    task = driver_and_task[1]
    action = ActionChains(driver)
    element_to_edit = driver.find_element_by_css_selector('label[ng-dblclick="editTodo(todo)"]')
    action.double_click(element_to_edit).perform()
    edition_task = driver.find_element_by_css_selector('input[todo-focus="todo == editedTodo"]')
    edition_task.send_keys(Keys.CONTROL, 'a')
    driver.implicitly_wait(WAITING_TIME)
    edition_task.send_keys(Keys.BACKSPACE + '\n')
    driver.implicitly_wait(WAITING_TIME)

    print('test3_delete_a_task is passed successfully') if task.text == '' \
        else print('test3_delete_a_task is fail')


def test4_Mark_task_as_completed():
    driver_and_task = add_task_to_edit(TASK2)
    driver = driver_and_task[0]
    task_complete = driver.find_element_by_css_selector('input[ng-model="todo.completed"]')
    driver.implicitly_wait(WAITING_TIME)
    task_complete.click()
    driver.implicitly_wait(WAITING_TIME)
    list_complete = driver.find_elements_by_css_selector('input[ng-model="todo.completed"]')
    for elem in list_complete:
        if elem == task_complete:
            print('test4_Mark_task_as_completed is passed successfully')
            return
    else:
        print("test4_Mark_task_as_completed is fail")



def test5_Mark_completed_task_as_active():
    driver_and_task = add_task_to_edit(TASK2)
    driver = driver_and_task[0]
    task_complete = driver.find_element_by_css_selector('input[ng-model="todo.completed"]')
    driver.implicitly_wait(WAITING_TIME)
    task_complete.click()
    driver.implicitly_wait(WAITING_TIME)
    task_complete.click()
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[2]/a').click()
    check_task = driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    print('test5_Mark_completed_task_as_active is passed successfully') if check_task.text == TASK2 \
        else print('test5_Mark_completed_task_as_active is fail')



def test6_clear_completed_tasks():
    driver_and_task = add_task_to_edit(TASK2)
    driver = driver_and_task[0]
    driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys("Clean the house\n")
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_xpath("/html/body/ng-view/section/section/ul/li[2]/div/input").click()
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_class_name("clear-completed").click()
    driver.implicitly_wait(WAITING_TIME)
    elements = driver.find_elements_by_css_selector('li[ng-repeat="todo in todos | filter:statusFilter track by $index"]')
    print("test6_clear_completed_tasks is passed successfully") if len(elements) == 1 and elements[0].text == TASK2 \
        else print('test6_clear_completed_tasks is fail')


def test7_see_different_views():
    driver_and_task = add_task_to_edit(TASK2)
    driver = driver_and_task[0]
    driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys(f"{TASK1}\n")
    driver.implicitly_wait(WAITING_TIME)
    driver.find_element_by_xpath("/html/body/ng-view/section/section/ul/li[2]/div/input").click()
    driver.implicitly_wait(WAITING_TIME)
    # the active list
    driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[2]/a").click()
    driver.implicitly_wait(WAITING_TIME)
    # the completed list
    driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[3]/a").click()
    driver.implicitly_wait(WAITING_TIME)
    # all list
    driver.find_element_by_xpath("/html/body/ng-view/section/footer/ul/li[1]/a").click()
    driver.implicitly_wait(WAITING_TIME)

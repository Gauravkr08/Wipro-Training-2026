import requests, os, time, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

LOG_FILE = "test_app_results.txt"
BASE_URL = "http://127.0.0.1:5000/api/v1"

# Initialize log file
with open(LOG_FILE, "w") as f:
    f.write("TEST APP EXECUTION LOG\n======================\n")

def log_to_file(test_name, status):
    with open(LOG_FILE, "a") as f:
        f.write(f"{test_name}: {status}\n")

res_id = user_id = order_id = dish_id = None

@pytest.fixture(scope="session", autouse=True)
def browser_automation():
    # Only one browser window opens for the entire set of 18 tests
    yield
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"{BASE_URL}/admin/orders")
    time.sleep(2)
    driver.save_screenshot("pytest_final_view.png")
    driver.quit()

# --- 18 TEST CASES ---
def test_01_reg_res():
    global res_id
    r = requests.post(f"{BASE_URL}/restaurants", json={"name":"H","category":"V","location":"D","contact":"1"})
    res_id = r.json()["id"]
    assert r.status_code == 201
    log_to_file("test_01_reg_res", "PASS")

def test_02_dup_res():
    r = requests.post(f"{BASE_URL}/restaurants", json={"name":"H","category":"V","location":"D","contact":"1"})
    assert r.status_code == 409
    log_to_file("test_02_dup_res", "PASS")

def test_03_view_res(): 
    assert requests.get(f"{BASE_URL}/restaurants/{res_id}").status_code == 200
    log_to_file("test_03_view_res", "PASS")

def test_04_upd_res(): 
    assert requests.put(f"{BASE_URL}/restaurants/{res_id}", json={"location":"M"}).status_code == 200
    log_to_file("test_04_upd_res", "PASS")

def test_05_dis_res(): 
    assert requests.put(f"{BASE_URL}/restaurants/{res_id}/disable").status_code == 200
    log_to_file("test_05_dis_res", "PASS")

def test_06_add_dish():
    global dish_id
    r = requests.post(f"{BASE_URL}/restaurants/{res_id}/dishes", json={"name":"P","type":"V","price":10})
    dish_id = r.json()["id"]
    assert r.status_code == 201
    log_to_file("test_06_add_dish", "PASS")

def test_07_upd_dish(): 
    assert requests.put(f"{BASE_URL}/dishes/{dish_id}", json={"price":20}).status_code == 200
    log_to_file("test_07_upd_dish", "PASS")

def test_08_tog_dish(): 
    assert requests.put(f"{BASE_URL}/dishes/{dish_id}/status", json={"enabled":False}).status_code == 200
    log_to_file("test_08_tog_dish", "PASS")

def test_09_del_dish(): 
    assert requests.delete(f"{BASE_URL}/dishes/{dish_id}").status_code == 200
    log_to_file("test_09_del_dish", "PASS")

def test_10_reg_user():
    global user_id
    r = requests.post(f"{BASE_URL}/users/register", json={"name":"D","email":"d@t.com"})
    user_id = r.json()["id"]
    assert r.status_code == 201
    log_to_file("test_10_reg_user", "PASS")

def test_11_dup_user(): 
    assert requests.post(f"{BASE_URL}/users/register", json={"name":"D","email":"d@t.com"}).status_code == 409
    log_to_file("test_11_dup_user", "PASS")

def test_12_order():
    global order_id
    r = requests.post(f"{BASE_URL}/orders", json={"user_id":user_id,"restaurant_id":res_id,"dishes":[]})
    order_id = r.json()["id"]
    assert r.status_code == 201
    log_to_file("test_12_order", "PASS")

def test_13_v_u_o(): 
    assert requests.get(f"{BASE_URL}/users/{user_id}/orders").status_code == 200
    log_to_file("test_13_v_u_o", "PASS")

def test_14_v_r_o(): 
    assert requests.get(f"{BASE_URL}/restaurants/{res_id}/orders").status_code == 200
    log_to_file("test_14_v_r_o", "PASS")

def test_15_rate(): 
    assert requests.post(f"{BASE_URL}/ratings", json={"order_id":order_id,"rating":5}).status_code == 201
    log_to_file("test_15_rate", "PASS")

def test_16_adm_app(): 
    assert requests.put(f"{BASE_URL}/admin/restaurants/{res_id}/approve").status_code == 200
    log_to_file("test_16_adm_app", "PASS")

def test_17_adm_dis(): 
    assert requests.put(f"{BASE_URL}/admin/restaurants/{res_id}/disable").status_code == 200
    log_to_file("test_17_adm_dis", "PASS")

def test_18_adm_ord(): 
    assert requests.get(f"{BASE_URL}/admin/orders").status_code == 200
    log_to_file("test_18_adm_ord", "PASS")

if __name__ == "__main__":
    pytest.main([__file__])
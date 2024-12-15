import pyautogui
import keyboard
import time

# Define the steps in multiple groups
step_groups = {
    "click_add_session": [
        {"action_type": "click", "location": (965, 274)},
    ],
    "14_00": [
        {"action_type": "click", "location": (433, 229)},
        {"action_type": "key_press", "keys_to_press": "14:00"},
        {"action_type": "click", "location": (433, 229)}
    ],
    "16_00": [
        {"action_type": "click", "location": (584, 222)},
        {"action_type": "key_press", "keys_to_press": "16:00"},
        {"action_type": "click", "location": (584, 222)}
    ],
    "11_30": [
        {"action_type": "click", "location": (433, 229)},
        {"action_type": "key_press", "keys_to_press": "11:30"},
        {"action_type": "click", "location": (433, 229)}
    ],
    "13_30": [
        {"action_type": "click", "location": (584, 222)},
        {"action_type": "key_press", "keys_to_press": "13:30"},
        {"action_type": "click", "location": (584, 222)}
    ],
    "03_30pm": [
        {"action_type": "click", "location": (433, 229)},
        {"action_type": "key_press", "keys_to_press": "03:30"},
        {"action_type": "click", "location": (433, 229)}
    ],
    "5_30pm": [
        {"action_type": "click", "location": (584, 222)},
        {"action_type": "key_press", "keys_to_press": "05:30"},
        {"action_type": "click", "location": (584, 222)}
    ],
    "seats": [
        {"action_type": "click", "location": (865, 227)},
        {"action_type": "key_press", "keys_to_press": "10"},
        {"action_type": "click", "location": (865, 227)}
    ],
    "calender_31_august": [
        {"action_type": "click", "location": (700, 365)},
        {"action_type": "click", "location": (615, 410)},
        {"action_type": "click", "location": (780, 565)}
    ],
    "trade_button": [
        {"action_type": "click", "location": (567, 290)},
    ],
    "car_body_repair": [
        {"action_type": "click", "location": (539, 327)}
    ],
    "automotive_primary_service": [
        {"action_type": "click", "location": (527, 362)}
    ],
    "tiling": [
        {"action_type": "click", "location": (485, 577)}
    ],
    "carpentry": [
        {"action_type": "click", "location": (454, 398)}
    ],
    "automotive_electrician": [
        {"action_type": "click", "location": (532, 423)}
    ],
    "heating_ventilation": [
        {"action_type": "click", "location": (546, 457)}
    ],
    "welding": [
        {"action_type": "click", "location": (550, 481)}
    ],
    "automotive_mechanics": [
        {"action_type": "click", "location": (512, 514)}
    ],
    "plumbing": [
        {"action_type": "click", "location": (483, 552)}
    ],
    "painting": [
        {"action_type": "click", "location": (512, 621)}
    ],
    "plasterer": [
        {"action_type": "click", "location": (429, 648)}
    ],
    "2_shuttering_carpenter": [
        {"action_type": "click", "location": (654, 632)},
        {"action_type": "click", "location": (502, 556)}
    ],
    "2_blacksmith": [
        {"action_type": "click", "location": (654, 632)},
        {"action_type": "click", "location": (502, 589)}
    ],
    "2_construction_and_building": [
        {"action_type": "click", "location": (654, 632)},
        {"action_type": "click", "location": (482, 625)}
    ],
    "2_electrician": [
        {"action_type": "click", "location": (654, 632)},
        {"action_type": "click", "location": (533, 644)}
    ],
    "ending": [
        {"action_type": "click", "location": [910, 290]},
        {"action_type": "click", "location": [777, 450]},
        {"action_type": "click", "location": [565, 209]},
        {"action_type": "click", "location": [549, 279]},
        {"action_type": "click", "location": [837, 207]},
        {"action_type": "click", "location": [563, 293]},
        {"action_type": "click", "location": [600, 290]},
        {"action_type": "click", "location": [644, 293]},
        {"action_type": "click", "location": [684, 293]},
        {"action_type": "click", "location": [730, 293]},
        {"action_type": "click", "location": [770, 293]}
    ]
}

# Sequence of execution for step groups
execution_sequence = ["click_add_session", "14_00", "16_00", "seats", "trade_button", "ending", "calender_31_august"]

# Time interval between actions
interval_between_actions = 0.3  # seconds

def perform_click_action(location):
    pyautogui.click(location)
    time.sleep(interval_between_actions)

def perform_key_press_action(keys_to_press):
    if keys_to_press:
        pyautogui.typewrite(keys_to_press)
        time.sleep(interval_between_actions)

def autoclick_and_keypress(step_group):
    for step_entry in step_group:
        if keyboard.is_pressed('q'):  # Check if 'q' was pressed to exit
            print("Stopping the autoclicker.")
            return True

        action_type = step_entry["action_type"]

        if action_type == "click":
            location = step_entry["location"]
            perform_click_action(location)
        elif action_type == "key_press":
            keys_to_press = step_entry["keys_to_press"]
            perform_key_press_action(keys_to_press)

    print("Completed one iteration of autoclicking and key pressing.")
    return False

if __name__ == "__main__":
    '''trades = ["car_body_repair", "automotive_primary_service", "tiling", "carpentry", 
              "automotive_electrician", "heating_ventilation", "welding", 
              "automotive_mechanics", "plumbing", "painting", "plasterer", 
              "2_shuttering_carpenter", "2_blacksmith", "2_construction_and_building", 
              "2_electrician"]'''
    trades = [ "plasterer", 
              "2_shuttering_carpenter", "2_blacksmith", "2_construction_and_building", 
              "2_electrician"]

    

    for trade in trades:
        print(f"Starting the autoclicker and key presser for trade: {trade}. Press 'q' to stop.")

        execution_sequence_with_trade = execution_sequence[:]
        trade_index = execution_sequence_with_trade.index("trade_button") + 1
        execution_sequence_with_trade.insert(trade_index, trade)

        # Execute step groups in the specified sequence
        for group_name in execution_sequence_with_trade:
            print(f"Executing {group_name}...")
            stop = autoclick_and_keypress(step_groups[group_name])
            if stop:
                print("Stopping the autoclicker.")
                quit()

        print(f"Completed all steps for trade: {trade}. Press 'n' to move to the next trade or 'q' to stop the script.")
        while True:
            if keyboard.is_pressed('n'):
                print("Moving to the next trade.")
                break
            elif keyboard.is_pressed('q'):
                print("Stopping the script.")
                quit()
            time.sleep(0.1)

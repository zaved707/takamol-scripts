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
execution_sequence = ["click_add_session", "11_30", "13_30", "seats","trade_button","2_shuttering_carpenter", "ending","calender_31_august"]

# Time interval between actions
interval_between_actions = 0.3  # seconds

# Specify the group after which to pause
pause_after_group = "2_shuttering_carpenter"

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
            return

        action_type = step_entry["action_type"]

        if action_type == "click":
            location = step_entry["location"]
            perform_click_action(location)
        elif action_type == "key_press":
            keys_to_press = step_entry["keys_to_press"]
            perform_key_press_action(keys_to_press)

    print("Completed one iteration of autoclicking and key pressing.")

if __name__ == "__main__":
    while True:
        print("Starting the autoclicker and key presser. Press 'q' to stop or 'r' to repeat.")
        # Execute step groups in the specified sequence
        for group_name in execution_sequence:
            print(f"Executing {group_name}...")
            autoclick_and_keypress(step_groups[group_name])

            # Pause after the specified group
            if group_name == pause_after_group:
                print("Paused after group:", pause_after_group)
                print("Press 'z' to continue or 'q' to stop...")
                while True:
                    if keyboard.is_pressed('z'):
                        print("Resuming...")
                        break
                    elif keyboard.is_pressed('q'):
                        print("Stopping the autoclicker.")
                        quit()
                    time.sleep(0.1)
        print("Completed all steps. Press 'q' to stop or 'r' to repeat.")
        while True:
            if keyboard.is_pressed('r'):
                break
            elif keyboard.is_pressed('q'):
                print("Stopping the autoclicker.")
                quit()
            time.sleep(0.1)

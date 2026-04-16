import time
import random

def pause(counter):
    if counter % 3 == 0:
        time.sleep(2)

def generate_random_dob():
    year = random.randint(1980, 2012)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    # Format: M/D/YYYY
    return f"{month}/{day}/{year}"

def safe_tap(adb, config, key):
    coords = config['actions'].get(key)

    print(f"{key} -> {coords}")

    if not coords:
        print(f"❌ Missing: {key}")
        return False

    try:
        adb.tap(int(coords[0]), int(coords[1]))
        return True
    except:
        print(f"❌ Tap failed: {key}")
        return False

def add_member(adb, config, row):
    count = 0

    def step():
        nonlocal count
        count += 1
        pause(count)

    print("\n=== START NEW ENTRY ===")

    # Add Member
    print("STEP: Add Member")
    safe_tap(adb, config, 'add_member')
    time.sleep(1)

    # Open DOB
    print("STEP: Open DOB")
    safe_tap(adb, config, 'dob')
    time.sleep(1)

    # Click Edit
    print("STEP: Click Edit")
    safe_tap(adb, config, 'dob_edit')
    time.sleep(1)

    # Type DOB
    print("STEP: Type DOB")
    dob_value = generate_random_dob()
    print("DOB VALUE:", dob_value)

    adb.input_text(dob_value.replace("/", "\\/"))
    time.sleep(1)

    # Click OK
    print("STEP: Click OK")
    safe_tap(adb, config, 'dob_ok')
    time.sleep(1)

    step()

    # First Name
    print("STEP: First Name")
    safe_tap(adb, config, 'first_name')
    time.sleep(0.5)
    adb.input_text(row['first_name'])
    step()

    # Last Name
    print("STEP: Last Name")
    safe_tap(adb, config, 'last_name')
    time.sleep(0.5)
    adb.input_text(row['last_name'])
    step()

    # Gender
    print("STEP: Gender")
    if row['gender'].lower() == 'male':
        safe_tap(adb, config, 'gender_male')
    else:
        safe_tap(adb, config, 'gender_female')
    step()

    # Hide keyboard
    print("STEP: Hide Keyboard")
    adb.run("shell input keyevent 4")
    time.sleep(1)

    # Scroll Down slightly
    print("STEP: Scroll DOWN")
    adb.swipe(500, 1800, 500, 600)
    time.sleep(1)

    # Relationship
    print("STEP: Relationship")
    safe_tap(adb, config, 'relationship')
    time.sleep(1)
    safe_tap(adb, config, 'relationship_option')
    step()

    # Pincode
    print("STEP: Pincode")
    safe_tap(adb, config, 'pincode')
    time.sleep(0.5)
    adb.input_text(row['pincode'])
    step()

    # Hide keyboard
    print("STEP: Hide Keyboard")
    adb.run("shell input keyevent 4")
    time.sleep(1)

    # Submit
    print("STEP: Submit")
    safe_tap(adb, config, 'submit')
    time.sleep(12)

    # Click Ok
    print("STEP: OK")
    safe_tap(adb, config, 'ok')
    time.sleep(12)
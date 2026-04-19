# --- Data Collection ---
site_name = "Nairobi HQ - Floor 3"
num_of_aps = 4
best_signal = -45.55368
worst_signal = -87.2
survey_complete = True
notes = None

# --- Type Checking ---
print(type(site_name))       
print(type(num_of_aps))
print(type(best_signal))
print(type(worst_signal))
print(type(survey_complete))
print(type(notes))

# --- Summary ---
print("--- Site Survey Summary ---")
print(f"Site: {site_name}")
print(f"Access Points: {num_of_aps}")
print(f"Best Signal: {best_signal:.1f} dBm")
print(f"Worst Signal: {worst_signal} dBm")
print(f"Survey complete: {survey_complete}")
print(f"Notes: {notes}")
